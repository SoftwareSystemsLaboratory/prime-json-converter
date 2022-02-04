# Software Systems Laboratory JSON Converter Project

> A `pandas` interface into converting `.json` files into other filetypes

![[https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)
[![DOI](https://zenodo.org/badge/406267900.svg)](https://zenodo.org/badge/latestdoi/406267900)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-json-converter/actions/workflows/release.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-json-converter/actions/workflows/release.yml)
![[https://img.shields.io/badge/license-BSD--3-yellow](https://img.shields.io/badge/license-BSD--3-yellow)](https://img.shields.io/badge/license-BSD--3-yellow)

## Table of Contents

- [Software Systems Laboratory JSON Converter Project](#software-systems-laboratory-json-converter-project)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Developer Tooling](#developer-tooling)
    - [Operating System](#operating-system)
    - [Python Software](#python-software)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) JSON Converter Project is an interface into the `pandas` libraries ability to convert `.json` files into other filetypes.

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## Developer Tooling

To maximize the utility of this project the following software packages are **required**:

### Operating System

This tool **targets** Mac OS and Linux. SSL Metrics software is not supported or recommended to run on Windows *but can be modified to do so at your own risk*.

It is recomendded to run this tool on Mac OS or Linux. However, if you are on a Windows machine, you can use WSL to develop as well.

### Python Software

> The software listed in this section is meant for developing tools

All listed Python software assumes that you have downloaded and installed **Python 3.9.6** or greater.

- `pandas`
- `progress`

You can install all of the Python software with one of the following one-liners:

- `pip install --upgrade pandas pip progress`
- `pip install --upgrade pip -r requirements.txt`

## How To Use

### Installation

You can install the tool from PyPi with one of the following one liners:

- `pip install ssl-metrics-meta`
- `pip install ssl-metrics-json-converter`

### Command Line Arguements

`ssl-metrics-json-converter -h`

```shell
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
