Welcome to Fakernaija's Documentation!
======================================

Overview
--------

**Fakernaija** is a Python library that can help developers generate Nigerian-specific data like names, emails, addresses, phone numbers, bank details, school names, states, license plate numbers, and much more. Whether you're working on testing, development, or educational projects, **Fakernaija** can help you to generate realistic data with Nigerian contexts, and it also comes with a CLI for easy data exports to various file formats.

The source code is available on `GitHub <https://github.com/Pythonian/fakernaija>`_.

.. toctree::
    :hidden:
    :maxdepth: 1

    Home <self>
    naija
    commands

Features
--------

- Generate culturally accurate Nigerian data — no more `Oyinbo` data that don't gel!
- Quickly generate data from your favourite terminal with our CLI commands.
- Export generated data to various formats like JSON, CSV, and plain text.
- Customize your data generation with optional parameters for targeted outputs.

Installation
------------

**Fakernaija** requires **Python 3.10** or higher, and installing it is easy-peasy with ``pip``.

.. code-block:: console

    pip install -U fakernaija

Getting Started
---------------

The primary interface you will interact with is the :doc:`naija`. The ``Naija`` class serves as the main entry point for generating Nigerian-specific data. Import and instantiate it, and start generating data right away. Launch your Python shell and try out these examples:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

    >>> print(naija.full_name())
    Ugochi Maduike

    >>> print(naija.state_capital())
    Damaturu

    >>> print(naija.school_name())
    University of Nigeria, Nsukka

    >>> print(naija.phone_number())
    09039294684

    >>> print(naija.email())
    ololadelawal@hotmail.com

    >>> print(naija.license_plate())
    YLA-435EH

**Fakernaija** tries to ensure that each method call returns different results within the same session until all possible outcomes are exhausted:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

    >>> for _ in range(5):
    ...     print(naija.school_name())
    ...
    University of Nigeria, Nsukka
    Kebbi State University of Science and Technology
    Sa'adatu Rimi College of Education
    Kwara State Polytechnic
    Federal Polytechnic, Ado-Ekiti

You can also control the output with optional parameters to generate specific results. Here are some examples:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

    >>> print(naija.email(tribe="igbo", gender="female", domain="unn.edu.ng"))
    maduike.ugochi@unn.edu.ng

    >>> print(naija.phone_number(network="airtel", prefix="0902"))
    09021234567

    >>> print(naija.school_name(acronym=True, ownership="federal", school_type="university"))
    UNN

You can also generate complete data objects for more complex integrations:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

    >>> print(naija.course())
    {'name': 'Introduction to Computer Science', 'code': 'COS101'}

    >>> print(naija.degree())
    {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}

    >>> print(naija.school())
    {'name': 'Lagos State University', 'acronym': 'LASU', 'state': 'Lagos', 'type': 'university', 'ownership': 'State'}

Command Line Usage
------------------

Once installed, **Fakernaija** can be invoked directly from your command line via the ``naija`` command. The :doc:`commands` command allows you to generate data directly from your terminal. This is powered by the `Click <https://click.palletsprojects.com/>`_ library. Below are some examples:

.. code-block:: console

    $ naija email --domain unn.edu.ng --tribe igbo --gender female
    somtochi.mbakwe@unn.edu.ng

    $ naija phonenumber --network glo --prefix 0805
    08053791792

    $ naija school_name --school_type university --ownership private --state lagos
    Pan-Atlantic University

To generate multiple outputs, use the ``--repeat`` (or ``-r``) flag:

.. code-block:: console

    $ naija email --domain unn.edu.ng --tribe igbo --gender female --repeat 3
    maduike.ugochi@unn.edu.ng
    uzo.chukwu2002@unn.edu.ng
    mmasinwodo25@unn.edu.ng

    $ naija full_name --middlename -r 3
    Tamunoteim Akpobari Erebi
    Ousmane Seydou Ahmed
    Femi Kayode Ajayi

To export the generated data to various formats, use the ``--output`` (or ``-o``) flag:

.. code-block:: console

    $ naija full_name --repeat 1000 --tribe edo --gender female --middle_name --output csv
    Generated full names saved to /path/to/directory/full_name.csv

    $ naija email --repeat 1000 --domain gov.ng -o json
    Generated emails saved to /path/to/directory/email.json

    $ naija phone_number --repeat 1000 --network mtn --prefix 0803 --output text
    Generated phone numbers saved to /path/to/directory/phone_number.txt

Next Steps
----------

Now that you have a basic understanding of **Fakernaija**, you can explore more:

* :doc:`naija`: Reference for all available ``Naija`` methods you can call.
* :doc:`commands`: Reference for all available ``naija`` sub-commands you can execute.

Get Involved
------------

Want to contribute to **Fakernaija**? This section guides you through the development process.

- :doc:`contributing`: No be beans, but we have made contributing as easy as possible.
- :doc:`documentation`: Prefer updating the docs? This guide shows you how.
- :doc:`testing`: Skipping tests is like cooking jollof without pepper — it's just not right.
- :doc:`deployment`: A guide to deploying new versions of the library on PyPI.

.. toctree::
    :caption: Development
    :maxdepth: 1
    :hidden:

    contributing
    documentation
    testing
    deployment

Meta
----

This section provides information about the project:

- :doc:`changelog`: See what has been added or removed over time.
- :doc:`support`: No need to shout `Epp me!` — we've got your back.
- :doc:`credits`: We believe in giving `Kudos` where it's due — because who no like better thing?
- :doc:`license`: Just like free Wi-Fi, our ``MIT License`` makes it available for everyone to enjoy.

.. toctree::
    :caption: Meta
    :maxdepth: 1
    :hidden:

    changelog
    support
    credits
    license

Thank You
---------

If you find this library useful or worthy of your attention, please give it a `Star <https://github.com/Pythonian/fakernaija>`_ on GitHub. Your contributions, feedback, and suggestions are always welcome!

Happy coding!
