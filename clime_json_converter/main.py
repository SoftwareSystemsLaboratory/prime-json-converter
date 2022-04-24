from argparse import Namespace
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from progress.spinner import MoonSpinner

from clime_json_converter.args import mainArgs
from clime_json_converter.version import version

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
    args: Namespace = mainArgs()

    if args.version:
        print(f"clime-git-commits-extract version {version()}")
        quit(0)

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
