from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from progress.spinner import MoonSpinner


def parseArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        # TODO: Add program name
        # TODO: Choose either Computation or Collection
        # TODO: Add program usage
        # TODO: Add program description
        # TODO: Add program epilog
        prog="SSL Metrics JSON Converter Utility",
        usage="This utility converts between .json files and other filetypes",
        description="This utility acts as an interface into pandas datatype conversion to allow for .json files to be converted into a variety of other formats",
        epilog="Program created by Nicholas M. Synovic and George K. Thiruvathukal",
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
    parser.add_argument(
        "--excel",
        help="Convert the input to *.xlsx",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--feather",
        help="Convert the input to *.feather",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--hdf",
        help="Convert the input to *.hdf5",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--html",
        help="Convert the input to *.html",
        action="store_true",
        default=True,
        required=True,
    )
    parser.add_argument(
        "--json",
        help="Convert the input to *.json",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--latex",
        help="Convert the input to *.tex",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--markdown",
        help="Convert the input to *.md",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--parquet",
        help="Convert the input to *.parquet",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--pickle",
        help="Convert the input to *.pkl",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--stata",
        help="Convert input to *.dta",
        action="store_true",
        default=False,
        required=False,
    )
    parser.add_argument(
        "--tsv",
        help="Convert the input to *.tsv",
        action="store_true",
        default=False,
        required=False,
    )

    return parser.parse_args()


def loadDataFrame(filename: str, filetype: str = ".json") -> DataFrame:
    if filetype == ".json":
        return pd.read_json(filename)
    elif filetype == ".csv":
        return pd.read_csv(filename, sep=",")
    elif filename == ".tsv":
        return pd.read_csv(filename, sep="\t")
    else:
        print("Unsupported input filetype")
        return -1


def storeDataFrame(df: DataFrame, stem: str, filetypes: list) -> int:
    with MoonSpinner(
        message=f"Converting {stem} to different filetypes... "
    ) as spinner:
        for ft in filetypes:
            if ft == "clipboard":
                df.to_clipboar
            elif ft == "csv":
                df.to_csv(stem + ".csv", sep=",", index=False)
            elif ft == "excel":
                df.to_excel(stem + ".xlsx", index=False)
            elif ft == "feather":
                df.to_feather(stem + ".feather")
            elif ft == "hdf":
                df.to_hdf(stem + ".hdf5", index=False)
            elif ft == "html":
                df.to_html(stem + ".html", index=False)
            elif ft == "json":
                df.to_json(stem + ".json", index=False)
            elif ft == "latex":
                df.to_latex(stem + ".tex", index=False)
            elif ft == "markdown":
                df.to_markdown(stem + ".md")
            elif ft == "parquet":
                df.to_latex(stem + ".parquet", index=False)
            elif ft == "pickle":
                df.to_pickle(stem + ".pkl")
            elif ft == "stata":
                df.to_stata(stem + ".dta")
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
