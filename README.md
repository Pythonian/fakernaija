# Fakernaija

**Fakernaija** is a Python library designed to help developers generate realistic Nigerian-specific data like full names, email addresses, phone numbers, bank information, jobs, schools, states, license plate numbers, and much more. Whether you're working on testing, development, or educational projects, Fakernaija can help you generate random data with Nigerian contexts, including a CLI for easy data exports.

The documentation is available on [Read the Docs](https://fakernaija.readthedocs.io).

----

```text
 _____           _                                    _     _
|  ___|   __ _  | | __   ___   _ __   _ __     __ _  (_)   (_)   __ _
| |_     / _` | | |/ /  / _ \ | '__| | '_ \   / _` | | |   | |  / _` |
|  _|   | (_| | |   <  |  __/ | |    | | | | | (_| | | |   | | | (_| |
| |      \__,_| |_|\_\  \___| |_|    |_| |_|  \__,_| |_|  _/ |  \__,_|
|_|                                                      |__/

```

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Pythonian/fakernaija/.github%2Fworkflows%2Fci.yml)](https://github.com/Pythonian/fakernaija/actions)
[![Documentation Status](https://readthedocs.org/projects/fakernaija/badge/?version=latest)](https://fakernaija.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Pythonian/fakernaija/main.svg)](https://results.pre-commit.ci/latest/github/Pythonian/fakernaija/main)
![Codecov](https://img.shields.io/codecov/c/github/Pythonian/fakernaija)

## Features

- Generate culturally accurate Nigerian data — no more `Oyinbo` names that don't gel!
- Quickly generate data from the terminal with our CLI commands, because time na money!
- Export data to JSON, CSV, and plain text formats, like wrapping your suya in the perfect paper.

## Installation

Fakernaija is available on PyPI and can be easily installed using `pip`. The minimum requirement for working with the library is **Python 3.10**.

```bash
pip install -U fakernaija
```

## Quick Start

Fakernaija is designed to be easy to use. Launch your Python shell and run the example below:

```python
>>> from fakernaija import Faker

>>> naija = Faker()

>>> print("A random Nigerian full name:", naija.full_name())
A random Nigerian full name: Ololade Lawal
```

_For more available method calls, please refer to the [Faker API](https://fakernaija.readthedocs.io/en/latest/faker.html)._

## Command Line Interface (CLI)

Fakernaija's CLI allows you to generate Nigerian-specific data directly from your terminal. Launch your favourite terminal and execute the command below:

```bash
$ naija email --domain unn.edu.ng --tribe igbo --gender female --repeat 3
maduike.ugochi@unn.edu.ng
somtochi.mbakwe@unn.edu.ng
mmasinwodo2000@unn.edu.ng
```

_For more detailed usage of the CLI, please refer to the [Commands API](https://fakernaija.readthedocs.io/en/latest/commands.html)._

## Get Involved

We welcome contributions! Visit our [contributing guide](https://fakernaija.readthedocs.io/en/latest/contributing.html) for more information.

## Feedback

Help us improve! If you spot an issue or have suggestions, [raise an issue](https://github.com/Pythonian/fakernaija/issues/new/choose) or contact [Seyi Pythonian](https://twitter.com/Ajibel).

Please, you can also Star the Github repository of this library if you find it useful or worthy of your attention. Thank you.

## Changelog

See the [Changelog](https://fakernaija.readthedocs.io/en/latest/changelog.html) for details on changes made in each version.

## License

Fakernaija is released under the [MIT License](https://fakernaija.readthedocs.io/en/latest/license.html).
