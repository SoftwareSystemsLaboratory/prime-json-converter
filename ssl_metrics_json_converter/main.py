# Documentation for the different exporters:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html

from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from progress.spinner import MoonSpinner


def parseArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="SSL Metrics JSON Converter",
        usage="Convert JSON into other datatypes and back again",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="File to be converted to other outputs",
        required=True,
    )
    parser.add_argument(
        "--clipboard",
        help="Copy the data from the file to the system's clipboard",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--csv",
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
        help="Convert the input to *.tsv",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument("--xarray")

    return parser.parse_args()


def loadDataFrame(filename: str, filetype: str = ".json") -> DataFrame:
    if filetype == ".json":
        return pd.read_json(filename)
    elif filetype == ".csv":
        return pd.read_csv(filename, sep=",")
    elif filename == ".tsv":
        return pd.read_csv(filename, sep="\t")
    else:
        print("Unsupported import filetype")
        return -1


def storeDataFrame(df: DataFrame, stem: str, filetypes: list) -> int:
    with MoonSpinner(
        message=f"Converting {stem} to different filetypes... "
    ) as spinner:
        for ft in filetypes:
            if ft == "clipboard":
                df.to_clipboard()
            elif ft == "json":
                df.to_json(stem + ".json", index=False)
            elif ft == "csv":
                df.to_csv(stem + ".csv", sep=",", index=False)
            elif ft == "tsv":
                df.to_csv(stem + ".tsv", sep="\t", index=False)
            else:
                return filetypes.index(ft)
            spinner.next()
    return -1


def main() -> None:
    args: Namespace = parseArgs()
    argsDict: dict = args.__dict__

    file: Path = Path(args.input)
    fn: str = file.stem
    ft: str = file.suffix

    df: DataFrame = loadDataFrame(filename=args.input, filetype=ft)

    fts: list = []
    key: str
    for key in argsDict.keys():
        if argsDict[key] == True:
            fts.append(key)

    store: int = storeDataFrame(df, stem=fn, filetypes=fts)

    if store != -1:
        print(f"Unsupported format: {fts[store]}")


if __name__ == "__main__":
    main()
