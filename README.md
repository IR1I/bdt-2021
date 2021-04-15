# BdT2021 - Lab project

This repository tracks the work performed during the University of Trento, Big Data Technologies - 2021 Lab lessons .

## Project objective

This objective leverages the public data provided by the [Trentino Open Data Hub](https://dati.trentino.it/).
In particular, the project relies on the the data describing the status pf the [Bike sharing stations](https://dati.trentino.it/dataset/stazioni-bike-sharing-emotion-trentino).

The objective of this project is the following:

1. collect the bike sharing station status information
2. create a historical dataset of the status information (this is important because no historical data is available) from the live data provided
3. store the collected data (e.g. memory, file, database)
4. compute some stats and analytics

## Project structure

* `README.md` file: it is the one where this text is written, the starting point for describing the purpose and objective of this repository and provides the instructions on how to use and run the code
* `.gitignore` file: it is the one allowing to list the files (or file patterns) that should not be tracked in the repository (e.g. the Python virtual environment)
* `requirements.txt` file: for listing the Python libraries that should be installed before running the code
* `src` folder, that contains all the Python files

## Usage

### Environment

This project requires Python 3.

It can be run by taking advantage of the system Python.
It can also be run within a Python virtual environment. The following is an example of creation of a virtual environment named _venv3_.

```bash
python3 -m venv venv3
```

### Requirements

The libraries defined in the `requirements.txt` file should be installed.

```bash
pip install -r requirements.tx
```

### Running the code

In order to run the data collection, do the following:

```bash
python3 -m main
```