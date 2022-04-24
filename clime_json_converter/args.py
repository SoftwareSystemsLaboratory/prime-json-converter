from argparse import ArgumentParser, Namespace

name: str = "CLIME"
authors: list = ["Nicholas M. Synovic", "Matthew Hyatt", "George K. Thiruvathukal"]


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{name} JSON Converter",
        description="A tool to convert JSON files between different formats",
        epilog=f"Author(s): {', '.join(authors)}",
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
