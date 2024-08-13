# Fakernaija

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

## Installation

Fakernaija is available on PyPI and can be easily installed using `pip`. The minimum requirement for working with Fakernaija is **Python 3.10**.

```bash
pip install -U fakernaija
```

## Getting Started

Fakernaija is designed to be easy to use and integrate into your projects. Below are some basic examples:

### Basic Usage

```python
from fakernaija import Faker

naija = Faker()

print("A random Nigerian full name:", naija.full_name())
# 'A random Nigerian full name: Ugochi Maduike'

print("A random state capital:", naija.state_capital())
# 'A random state capital: Owerri'

print("A random email with specific domain:", naija.email(domain="unn.edu.ng"))
# 'A random email with specific domain: maduike.ugochi@unn.edu.ng'

for _ in range(5):
    print("A random MTN Phone number:", naija.phone_number(network="mtn"))
# A random MTN Phone number: 08160189846
# A random MTN Phone number: 09130280890
# A random MTN Phone number: 08065421583
# A random MTN Phone number: 08142772705
# A random MTN Phone number: 08066980070
```

### Command Line Interface (CLI)

Fakernaija also offers a CLI for generating Nigerian-specific data directly from your terminal. The main `naija` command provides access to subcommands for various data. You can generate data in bulk, customize options, and choose your desired output format.

Below are some examples demonstrating how to use the CLI.

```bash
$ naija email --domain unn.edu.ng --tribe igbo
maduike.ugochi16@unn.edu.ng

$ naija phonenumber --repeat 3 --network glo --prefix 0805
08059845756
08053408825
08051024278

$ naija data --repeat 30 --fields fullname,email,phonenumber --output csv
Generated data saved to /home/projectdir/data.csv
```

_For more detailed usage of the CLI, please refer to the [CLI documentation](https://fakernaija.readthedocs.io/en/latest/cli.html)._

## Documentation

Please check our [extended docs](https://fakernaija.readthedocs.io/en/latest/) for a full list of all available methods and subcommands.

## Get Involved

We welcome contributions! Please see the [contributing guide](https://fakernaija.readthedocs.io/en/latest/contributing.html) for more information on how to contribute to this project. Make sure to review our [coding guidelines](https://fakernaija.readthedocs.io/en/latest/contributing.html#coding-guidelines) before submitting your PRs.

## Feedback

Efforts have been made to ensure the accuracy of the data, but there could be slip-ups. If you identify any such oversight, please [raise an issue](https://github.com/Pythonian/fakernaija/issues/new/choose) as soon as possible. You can also suggest improvements or new features or reach out to [Seyi Pythonian](https://twitter.com/Ajibel).

## Changelog

See the [changelog](https://fakernaija.readthedocs.io/en/latest/changelog.html) for details on changes made in each version.

## License

Fakernaija is released under the MIT License. See the [LICENSE](https://fakernaija.readthedocs.io/en/latest/license.html) file for more details.
