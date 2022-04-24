# CLIME JSON Converter Project

> A tool to convert JSON files between different formats

## Table of Contents

- [CLIME JSON Converter Project](#clime-json-converter-project)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Licensing](#licensing)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) CLIME JSON Converter project is a tool to convert JSON files between different formats.

### Licensing

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## How To Use

### Installation

You can install the tool from PyPi with one of the following one liners:

- `pip install clime-metrics`
- `pip install clime-json-converter`

### Command Line Arguements

`clime-json-converter -h`

``` shell
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File to be converted to other outputs
  --clipboard           Copy the data from the file to the system's clipboard
  --csv                 Convert the input to *.csv
  --excel               Convert the input to *.xlsx
  --feather             Convert the input to *.feather
  --hdf                 Convert the input to *.hdf5
  --html                Convert the input to *.html
  --json                Convert the input to *.json
  --latex               Convert the input to *.tex
  --markdown            Convert the input to *.md
  --parquet             Convert the input to *.parquet
  --pickle              Convert the input to *.pkl
  --stata               Convert input to *.dta
  --tsv                 Convert the input to *.tsv
```
