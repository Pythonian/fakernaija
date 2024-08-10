# Fakernaija

**Fakernaija** is a Python library designed to help developers generate realistic Nigerian-specific data. With a simple interface and a variety of data, it can be used for creating mock data tailored to the Nigerian context. Whether you're working on testing, development, or educational projects, Fakernaija can help you generate random data to meet your requirements, including a CLI for easy integration.

_This library does not intend to be a drop-in replacement to the popular [Python Faker](https://faker.readthedocs.io/en/master/) package, but should complement it in cases where you need Nigerian contexts for your data generation._

----

``` fakernaija
 _____           _                                    _     _
|  ___|   __ _  | | __   ___   _ __   _ __     __ _  (_)   (_)   __ _
| |_     / _` | | |/ /  / _ \ | '__| | '_ \   / _` | | |   | |  / _` |
|  _|   | (_| | |   <  |  __/ | |    | | | | | (_| | | |   | | | (_| |
| |      \__,_| |_|\_\  \___| |_|    |_| |_|  \__,_| |_|  _/ |  \__,_|
|_|                                                      |__/

```

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Pythonian/fakernaija/.github%2Fworkflows%2Fci.yml)

## Installation

Fakernaija is available on PyPI and can be easily installed using `pip`. The minimum requirement for working with Fakernaija is **Python 3.10**.

```bash
pip install fakernaija
```

## Usage

Fakernaija is designed to be easy to use and integrate into your projects. Below are some basic examples:

### Basic Usage

```python
from fakernaija import Faker

naija = Faker()

print("A random Nigerian full name:", naija.full_name())
# 'A random Nigerian full name: Ugochi Maduike'

print("A random MTN phone number:", naija.phone_number(network="mtn"))
# 'A random MTN phone number: 08161723004'

print("A random state capital:", naija.capital())
# 'A random state capital: Owerri'

print("A random email with specific domain:", naija.email(domain="unn.edu.ng"))
# 'A random email with specific domain: maduike.ugochi@unn.edu.ng'

print("A random federal institution:", naija.federal_school())
# 'A random federal institution: University of Nigeria, Nsukka'
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

## Documentation

Please check our [extended docs](https://fakernaija.readthedocs.io/) for a full list of all available methods and subcommands.

## Contributing

We welcome contributions! Please see the [contributing guide](CONTRIBUTING) for more information on how to contribute to this project.

## Support

Efforts have been made to ensure the accuracy of the data, but there could be slip-ups. If you identify any such oversight, please [raise an issue](https://github.com/Pythonian/fakernaija/issues) as soon as possible. You can also suggest improvements or new features.

## License

Fakernaija is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
