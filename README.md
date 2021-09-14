# SSL Metrics JSON Converter

> Helper package to convert JSON to other formats and back again

## Table of Contents

- [SSL Metrics JSON Converter](#ssl-metrics-json-converter)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Install](#how-to-install)
    - [Note on Command Line Arguments](#note-on-command-line-arguments)
    - [Required Dependencies](#required-dependencies)
    - [From pip](#from-pip)
    - [Command Line Arguements](#command-line-arguements)
      - [ssl-metrics-json-converter](#ssl-metrics-json-converter-1)

## About

This is a helper package to convert JSON to other data formats and turn those formats into JSON.

While this program can export to many formats, it **does not** allow you to customize how that file is changed from one filetype to another at this time.

## How to Install

### Note on Command Line Arguments

See [Command Line Arguments](#command-line-arguments) for program configuration from the command line

### Required Dependencies

To copy to the clipboard on Linux, it is reccommended that you install:

- xsel (`sudo apt install xsel`)
- xclip (`sudo apt install xclip`)

### From pip

1. Install `Python 3.9.6 +`
2. (Recommended) Create a *virtual environment* with `python3.9 -m venv env` and *activate* it
3. Run `pip install ssl-metrics-json-converter`
4. Convert files with `ssl-metrics-json-converter -i FILENAME.* --*`

### Command Line Arguements

#### ssl-metrics-json-converter

**NOTE:** This list has been concatenated. To view the full list of flags, run `ssl-metrics-json-converter -h`.

- `-h`, `--help`: Shows the help menu and exits
- `-i`, `--input`: The input file to be converted
