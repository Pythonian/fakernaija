# Fakernaija

**Fakernaija** is a Python library that helps developers generate Nigerian-specific data like names, emails, addresses, phone numbers, banks, jobs, schools, states, license plate numbers, and much more. Whether you're working on testing, development, or educational projects, **Fakernaija** helps you generate realistic data, including a CLI for easy exports.

The documentation is available on [Read the Docs](https://fakernaija.readthedocs.io).

---

```text
 _____           _                                    _     _
|  ___|   __ _  | | __   ___   _ __   _ __     __ _  (_)   (_)   __ _
| |_     / _` | | |/ /  / _ \ | '__| | '_ \   / _` | | |   | |  / _` |
|  _|   | (_| | |   <  |  __/ | |    | | | | | (_| | | |   | | | (_| |
| |      \__,_| |_|\_\  \___| |_|    |_| |_|  \__,_| |_|  _/ |  \__,_|
|_|                                                      |__/

```

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Pythonian/fakernaija/ci.yml?style=for-the-badge)
![Read the Docs](https://img.shields.io/readthedocs/fakernaija?style=for-the-badge)
![Codecov](https://img.shields.io/codecov/c/github/Pythonian/fakernaija?style=for-the-badge)

## Features ✨

- Generate culturally accurate Nigerian data — no more _Oyinbo_ data that don't gel!
- Quickly generate data from your favourite terminal with our CLI commands.
- Export your generated data to various formats like JSON, CSV, and plain text.

## Installation 🛠️

**Fakernaija** requires **Python 3.10** or higher. Installation is easy-peasy with `pip`, ensuring you get the latest stable release of the library.

```console
pip install -U fakernaija
```

## Quick Start 🚀

**Fakernaija** is easy to use. Launch your Python shell and try out the example below:

```python
>>> from fakernaija import Faker
>>> naija = Faker()
>>> print("A random Nigerian full name:", naija.full_name())
A random Nigerian full name: Ihuoma Maduabuchi
```

_For more available method calls, please refer to the [Naija API Reference](https://fakernaija.readthedocs.io/en/latest/faker.html)._

## Command Line Usage 💻

**Fakernaija**'s CLI allows you to generate data directly from your terminal. Launch your favourite terminal and try out the example below:

```console
$ naija email --domain unn.edu.ng --gender female --repeat 3
ololade.lawal@unn.edu.ng
kudiratbello@unn.edu.ng
mmasichukwunwodo2000@unn.edu.ng
```

_For more detailed usage of the CLI, please refer to the [CLI API Reference](https://fakernaija.readthedocs.io/en/latest/commands.html)._

## What Next? ➡️

A more comprehensive documentation is available on [Read the Docs](https://fakernaija.readthedocs.io) 📚

If you would like to contribute, please read the [Contributing Guide](https://fakernaija.readthedocs.io/en/latest/contributing.html) 🤝

If you found a bug or have any suggestions, please [Raise an Issue](https://github.com/Pythonian/fakernaija/issues/new/choose) 🐛

If you need to contact the author privately, please reach out on [Twitter](https://twitter.com/Fakernaija) 🐦

If you find this library useful or worthy of your attention, please give it a **Star** ⭐

## License 📜

Fakernaija is released under the [MIT License](https://fakernaija.readthedocs.io/en/latest/license.html).

![Static Badge](https://img.shields.io/badge/Made%20in%20-%20Nigeria%20-%20Green?style=for-the-badge)
