import sys
from collections import Counter
from enum import Enum
from typing import Generic, List, TypeVar

import pandas as pd

from exabel_data_sdk.client.api.data_classes.entity import Entity
from exabel_data_sdk.client.api.data_classes.relationship import Relationship
from exabel_data_sdk.client.api.data_classes.request_error import RequestError

TResource = TypeVar("TResource", Entity, Relationship, pd.Series)


class ResourceCreationStatus(Enum):
    """
    Status values for resource creation.
    """

    # Denotes that a resource was created.
    CREATED = 1

    # Denotes that a resource already existed.
    EXISTS = 2

    # Denotes that creation failed.
    FAILED = 3


class ResourceCreationResult(Generic[TResource]):
    """
    The status of the creation of a particular resource.
    """

    def __init__(
        self, status: ResourceCreationStatus, resource: TResource, error: RequestError = None
    ):
        self.status = status
        self.resource: TResource = resource
        self.error = error

    def __repr__(self) -> str:
        return f"ResourceCreationResult{self.status.name, self.resource}"


class ResourceCreationResults(Generic[TResource]):
    """
    Class for returning resource creation results.
    """

    def __init__(
        self, total_count: int, print_status: bool = True, abort_threshold: float = 0.5
    ) -> None:
        """
        Args:
            total_count:     The total number of resources expected to be loaded.
            print_status:    Whether to print status of the upload during processing.
            abort_threshold: If the fraction of failed requests exceeds this threshold,
                             the upload is aborted, and the script exits.
                             Note that this only happens if print_status is set to True.
        """
        self.results: List[ResourceCreationResult[TResource]] = []
        self.counter: Counter = Counter()
        self.total_count = total_count
        self.do_print_status = print_status
        self.abort_threshold = abort_threshold

    def add(self, result: ResourceCreationResult[TResource]) -> None:
        """Add the result for a resource."""
        self.results.append(result)
        self.counter.update([result.status])
        if self.do_print_status and (self.count() % 20 == 0 or self.count() == self.total_count):
            self.print_status()

    def count(self, status: ResourceCreationStatus = None) -> int:
        """
        Number of results with the given status,
        or total number of results if no status is specified.
        """
        return len(self.results) if status is None else self.counter[status]

    def extract_retryable_failures(self) -> List[ResourceCreationResult[TResource]]:
        """
        Remove all retryable failures from this result set,
        and return them.
        """
        failed = []
        rest = []
        for result in self.results:
            if (
                result.status == ResourceCreationStatus.FAILED
                and result.error
                and result.error.error_type.retryable()
            ):
                failed.append(result)
            else:
                rest.append(result)
        self.counter.subtract([result.status for result in failed])
        self.results = rest
        return failed

    def print_summary(self) -> None:
        """Prints a human legible summary of the resource creation results to screen."""
        print(self.counter[ResourceCreationStatus.CREATED], "new resources created")
        if self.counter[ResourceCreationStatus.EXISTS]:
            print(self.counter[ResourceCreationStatus.EXISTS], "resources already existed")
        if self.counter[ResourceCreationStatus.FAILED]:
            print(self.counter[ResourceCreationStatus.FAILED], "resources failed:")
            for result in self.results:
                if result.status == ResourceCreationStatus.FAILED:
                    print("   ", result.resource, ":\n      ", result.error)

    def print_status(self) -> None:
        """
        Prints a status update on the progress of the data loading, showing the percentage complete
        and how many objects were created, already existed or failed.

        Note that the previous status message is overwritten (by writing '\r'),
        but this only works if nothing else has been printed to stdout since the last update.
        """
        fraction_complete = self.count() / self.total_count
        sys.stdout.write(
            f"\r{fraction_complete:.0%} - "
            f"{self.count(ResourceCreationStatus.CREATED)} created, "
            f"{self.count(ResourceCreationStatus.EXISTS)} exists, "
            f"{self.count(ResourceCreationStatus.FAILED)} failed"
        )
        if fraction_complete == 1:
            sys.stdout.write("\n")
        else:
            fraction_error = self.count(ResourceCreationStatus.FAILED) / self.count()
            if fraction_error > self.abort_threshold:
                sys.stdout.write(
                    f"\nAborting - more than {self.abort_threshold:.0%} "
                    "of the requests are failing.\n"
                )
                self.print_summary()
                sys.stdout.flush()
                sys.exit(1)
        sys.stdout.flush()