from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum, unique
from typing import Optional, Sequence

logger = logging.getLogger(__name__)


@unique
class ErrorType(Enum):
    """
    Error types.
    """

    # Resource was not found.
    NOT_FOUND = 0
    # Resource already exists.
    ALREADY_EXISTS = 1
    # An invalid argument was provided.
    INVALID_ARGUMENT = 2
    # The operation was rejected because the system is not in
    # a state required for the operation's execution.
    FAILED_PRECONDITION = 3
    # Missing access to resource.
    PERMISSION_DENIED = 4
    # Not able to connect to Exabel API.
    UNAVAILABLE = 5
    # Timeout.
    TIMEOUT = 6
    # Some resource has been exhausted, e.g. too many concurrent requests.
    RESOURCE_EXHAUSTED = 7
    # Any internal error.
    INTERNAL = 10
    # Any unknown error.
    UNKNOWN = 11

    def retryable(self) -> bool:
        """Return whether it makes sense to retry the request if this error is given."""
        return self in (
            ErrorType.UNAVAILABLE,
            ErrorType.TIMEOUT,
            ErrorType.INTERNAL,
            ErrorType.RESOURCE_EXHAUSTED,
        )

    @classmethod
    def from_precondition_failure_violation_type(cls, violation_type: str) -> ErrorType:
        """Convert a violation type from a precondition failure to an error type."""
        try:
            return ErrorType[violation_type]
        except KeyError:
            logger.error("Unknown error type in precondition violation: %s", violation_type)
            return ErrorType.UNKNOWN


@dataclass
class Violation:
    """
    Violation details.
    """

    type: str
    subject: str
    description: str


@dataclass
class PreconditionFailure:
    """
    PreconditionFailure details.
    """

    violations: Sequence[Violation]


@dataclass
class RequestError(Exception):
    """
    Represents an error returned from the Exabel Api.

    Attributes:
        error_type (ErrorType):                     Type of error.
        message (str):                              Exception message.
        precondition_failure (PreconditionFailure): PreconditionFailure details.
    """

    error_type: ErrorType
    message: Optional[str] = None
    precondition_failure: Optional[PreconditionFailure] = None
