# Fakernaija

## Overview

**Fakernaija** is a Python library designed to help developers generate realistic Nigerian-specific data. With a simple interface and a variety of data, it can be used for creating mock data tailored to the Nigerian context. Whether you're working on testing, development, or educational projects, Fakernaija can help you generate random data to meet your requirements, including a CLI for easy data exports.

_This library does not intend to be a drop-in replacement to the popular [Python Faker](https://faker.readthedocs.io/en/master/) package, but should complement it in cases where you need Nigerian contexts for your data generation._

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

## Features

* Tailored specifically to generate culturally accurate Nigerian data.
* Quickly generate data from your terminal with our CLI command.
* Supports exporting data to various formats including JSON, CSV, and plain text.
* Simple, intuitive API that integrates seamlessly into your Python web frameworks.

## Installation

Fakernaija is available on PyPI and can be easily installed using `pip`. The minimum requirement for working with Fakernaija is **Python 3.10**.

```bash
pip install -U fakernaija
```

_For a more detailed installation setup, please refer to our [Installation guide](https://fakernaija.readthedocs.io/en/latest/installation.html)._

## Quick Start

Fakernaija is designed to be easy to use. Launch your Python shell and run the example below:

```python
>>> from fakernaija import Faker

>>> naija = Faker()

>>> print("A random Nigerian full name:", naija.full_name())
A random Nigerian full name: Ololade Lawal
```

_For a more detailed walkthrough, please refer to the [Usage guide](https://fakernaija.readthedocs.io/en/latest/guide.html)._

## Command Line Interface (CLI)

Fakernaija's CLI allows you to generate Nigerian-specific data directly from your terminal. Launch your favourite terminal and execute the command below:

```bash
$ naija email --domain unn.edu.ng --tribe igbo --gender female --repeat 3
maduike.ugochi@unn.edu.ng
somtochi.mbakwe@unn.edu.ng
mmasinwodo25@unn.edu.ng
```

_For more detailed usage of the CLI, please refer to the [CLI documentation](https://fakernaija.readthedocs.io/en/latest/commands.html)._

## Get Involved

We welcome contributions! Visit our [contributing guide](https://fakernaija.readthedocs.io/en/latest/contributing.html) for more information.

## Feedback

Help us improve! If you spot an issue or have suggestions, [raise an issue](https://github.com/Pythonian/fakernaija/issues/new/choose) or contact [Seyi Pythonian](https://twitter.com/Ajibel).

Please, you can also Star the Github repository of this library if you find it useful or worthy of your attention. Thank you.

## Changelog

See the [changelog](https://fakernaija.readthedocs.io/en/latest/changelog.html) for details on changes made in each version.

## License

Fakernaija is released under the MIT License. See the [LICENSE](https://fakernaija.readthedocs.io/en/latest/license.html) for more details.
