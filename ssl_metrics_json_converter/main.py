import pandas as pd
from pandas import DataFrame
from progress.spinner import MoonSpinner

from argparse import ArgumentParser, Namespace


def parseArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics JSON Converter",
        usage="Convert JSON into other datatypes and back again",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="File to be converted to other outputs",
        required=True,
    )
    parser.add_argument("--clipboard")
    parser.add_argument(
        "--csv",
        type=bool,
        help="Convert the input to *.csv",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument("--dict")
    parser.add_argument("--excel")
    parser.add_argument("--feather")
    parser.add_argument("--gbq")
    parser.add_argument("--hdf")
    parser.add_argument("--html")
    parser.add_argument(
        "--json",
        type=bool,
        help="Convert the input to *.json",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument("--latex")
    parser.add_argument("--markdown")
    parser.add_argument("--parquet")
    parser.add_argument("--period")
    parser.add_argument("--pickle")
    parser.add_argument("--records")
    parser.add_argument("--stata")
    parser.add_argument("--string")
    parser.add_argument("--sql")
    parser.add_argument("--timestamp")
    parser.add_argument(
        "--tsv",
        type=bool,
        help="Convert the input to *.tsv",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument("--xarray")


def main() -> None:
    pass
