import argparse
import sys
from typing import Sequence

from exabel_data_sdk import ExabelClient
from exabel_data_sdk.scripts.actions import CaseInsensitiveArgumentAction
from exabel_data_sdk.scripts.csv_script_with_entity_mapping import CsvScriptWithEntityMapping
from exabel_data_sdk.services.csv_loading_constants import DEFAULT_NUMBER_OF_THREADS_FOR_IMPORT
from exabel_data_sdk.services.file_loading_exception import FileLoadingException
from exabel_data_sdk.services.file_time_series_loader import FileTimeSeriesLoader


class LoadTimeSeriesFromFile(CsvScriptWithEntityMapping):
    """
    Processes a time series file and uploads the time series to Exabel.

    Both CSV and Excel files can be imported, and there are three supported file layouts:
     * Signals as columns, with a header like: `entityType`,date,`signal_1`, ... ,`signal_n`
     * Signals as rows, with a header like: `entityType`,date,signal,value
     * Signals and entities as a two level header like:
           signal,`signal_1`,`signal_2`
           brand,`brand1`,`brand_2`

    See the Exabel Help pages for a full documentation, and further examples.

    To import data on companies, set the entity header to one of: isin, factset_identifier,
    bloomberg_symbol, bloomberg_ticker, figi, mic:ticker or cusip, or use the identifier_type
    argument.
    Supported identifier types for security entities are isin, mic:ticker and cusip.

    To import data on generic entities, set it either to the entity type identifier, for example
    `brand`, or set it to the constant `entity`. If set to `entity` the entities must be identified
    by their full resource name, for example `entityTypes/brand/entities/b1`.

    Dates in CSV files should be on ISO format, e.g. 2020-12-31, and Excel date cells should be
    formatted as dates.

    All formats except the one where there is one column per combination of signal and entity
    supports an optional `known_time` column, which specifies the time that the data point(s) of
    that row were known.

    The rows do not have to be sorted in any particular order.
    """

    def __init__(self, argv: Sequence[str]):
        description = "Upload time series file."
        super().__init__(argv, description)
        self.parser.add_argument(
            "--entity-type",
            type=str,
            help=(
                "The entity type of the entities in the file. If not specified, the entity type "
                "will be inferred from the column name."
            ),
            action=CaseInsensitiveArgumentAction,
        )
        self.parser.add_argument(
            "--identifier-type",
            type=str,
            help="The identifier type used to map the entities in the file.",
            action=CaseInsensitiveArgumentAction,
        )
        self.parser.add_argument(
            "--create-missing-signals",
            required=False,
            action="store_true",
            default=False,
            help="Automatically create signals that are not already present in the API.",
        )
        self.parser.add_argument(
            "--pit-current-time",
            required=False,
            action="store_true",
            default=False,
            help=(
                "Set the Known-Time of the uploaded data to be "
                "the time at which it is inserted into the Exabel system."
            ),
        )
        self.parser.add_argument(
            "--pit-offset",
            required=False,
            type=int,
            choices=range(101),
            metavar="[0-100]",
            help=(
                "Set the Known-Time of the uploaded data to be the timestamp of each data point, "
                "plus the specified number of days as an offset. For instance, if the data is "
                "available to the user the day after, one would set --pit-offset 1"
            ),
        )
        self.parser.add_argument(
            "--no-create-library-signal",
            dest="create_library_signal",
            required=False,
            action="store_false",
            default=True,
            help="Set to not create library signal DSL expressions.",
        )
        self.parser.set_defaults(threads=DEFAULT_NUMBER_OF_THREADS_FOR_IMPORT)
        self.parser.add_argument(
            "--batch-size",
            type=int,
            help=(
                "The number of rows in each batch to read and upload from the file. If not "
                "specified, defaults to reading the entire file into memory before uploading."
            ),
        )
        self.parser.add_argument(
            "--skip-validation",
            required=False,
            action="store_true",
            default=False,
            help="If set, the time series are not validated before uploading.",
        )
        self.parser.add_argument(
            "--case-sensitive-signals",
            required=False,
            action="store_true",
            default=False,
            help="If set, signal names are treated as case sensitive. Note that this will disable "
            "lowercasing of other column headers as well, as entities, 'date', and "
            "'known_time'. Take care to maintain correct casing in the file when using this "
            "option.",
        )
        self.parser.add_argument(
            "--replace-existing-time-series",
            required=False,
            action="store_true",
            default=False,
            help="Replace any existing time series when importing",
        )
        self.parser.add_argument(
            "--replace-existing-data-points",
            required=False,
            action="store_true",
            default=False,
            help="Replace any existing data points on the specified dates when importing",
        )
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument(
            "--optimise",
            required=False,
            action="store_true",
            help="Enable time series storage optimisation. If neither this nor --no-optimise is "
            "set, optimisation is at the discretion of the server.",
        )
        group.add_argument(
            "--no-optimise",
            required=False,
            action="store_true",
            help="Disable time series storage optimisation. If neither this nor -optimise is set, "
            "optimisation is at the discretion of the server.",
        )

    def run_script(self, client: ExabelClient, args: argparse.Namespace) -> None:
        try:
            FileTimeSeriesLoader(client).load_time_series(
                filename=args.filename,
                entity_mapping_filename=args.entity_mapping_filename,
                separator=args.sep,
                entity_type=args.entity_type,
                identifier_type=args.identifier_type,
                pit_current_time=args.pit_current_time,
                pit_offset=args.pit_offset,
                create_missing_signals=args.create_missing_signals,
                create_library_signal=args.create_library_signal,
                threads=args.threads,
                dry_run=args.dry_run,
                retries=args.retries,
                batch_size=args.batch_size,
                skip_validation=args.skip_validation,
                case_sensitive_signals=args.case_sensitive_signals,
                abort_threshold=args.abort_threshold,
                replace_existing_time_series=args.replace_existing_time_series,
                replace_existing_data_points=args.replace_existing_data_points,
                should_optimise=(
                    True if args.optimise is True else False if args.no_optimise is True else None
                ),
            )
        except FileLoadingException as e:
            print("ERROR: Loading time series failed.")
            print(e)
            sys.exit(1)


if __name__ == "__main__":
    LoadTimeSeriesFromFile(sys.argv).run()
