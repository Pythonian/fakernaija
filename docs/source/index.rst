Welcome to Fakernaija's Documentation!
======================================

Overview
--------

`Fakernaija <https://github.com/Pythonian/fakernaija>`_ is a Python library designed to help developers generate Nigerian-specific data like full names, email addresses, phone numbers, bank information, jobs, schools, states, license plate numbers, and much more. When you need some Naija flavour added to your project, **Fakernaija** helps you generate random, realistic data, including a CLI for easy exports.

.. toctree::
    :hidden:
    :maxdepth: 1

    Home <self>
    faker
    commands
    internals

Features
--------

- Generate culturally accurate Nigerian data — no more `Oyinbo` names that don't gel!
- Quickly generate data from the terminal with our CLI commands, because time na money!
- Export data to JSON, CSV, and plain text formats, like wrapping your suya in the perfect paper.

Installation
------------

**Fakernaija** requires **Python 3.10** or higher. Installation is easy-peasy with `pip`, ensuring you get the latest stable release of the library.

.. code-block:: bash

    pip install -U fakernaija

Getting Started
---------------

The primary interface you will interact with is the ``Faker`` class. You will need to import and instantiate it then you can start generating data right away. To whet your appetite, launch your Python shell and try out these examples:

.. code-block:: python

    >>> from fakernaija import Faker
    >>> naija = Faker()

    >>> print(naija.full_name())
    Ugochi Maduike

    >>> print(naija.state_capital())
    Owerri

    >>> print(naija.course_name())
    Introduction to Computer Science

    >>> print(naija.degree_name())
    Bachelor of Pharmacy

    >>> print(naija.faculty_name())
    Pharmaceutical Sciences

**Fakernaija** tries to ensure that each method call returns a different result within the same session until all possible outcomes are exhausted:

.. code-block:: python

    >>> from fakernaija import Faker
    >>> naija = Faker()

    >>> for _ in range(5):
    ...     print(naija.school_name())
    ...
    University of Nigeria, Nsukka
    Kebbi State University of Science and Technology
    Sa'adatu Rimi College of Education
    Kwara State Polytechnic
    Federal Polytechnic, Ado-Ekiti

There is also some flexibility in the data you generate. Many methods accept optional parameters to customize the output. Here are a few examples:

.. code-block:: python

    >>> from fakernaija import Faker
    >>> naija = Faker()

    >>> print(naija.email(tribe="igbo", gender="female", domain="unn.edu.ng"))
    maduike.ugochi@unn.edu.ng

    >>> print(naija.phone_number(network="airtel", prefix="0902"))
    09021234567

    >>> print(naija.school_name(acronym=True, ownership="federal", school_type="university"))
    UNN

You can also generate complete data objects, useful for when you need more than just individual attributes that you can easily integrate into more complex structures for your web applications:

.. code-block:: python

    >>> from fakernaija import Faker
    >>> naija = Faker()

    >>> print(naija.course())
    {'name': 'Introduction to Computer Science', 'code': 'COS101'}

    >>> print(naija.currency())
    {'code': 'NGN', 'name': 'Nigerian naira', 'symbol': '₦'}

    >>> print(naija.degree())
    {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}

    >>> print(naija.school())
    {'name': 'Lagos State University', 'acronym': 'LASU', 'state': 'Lagos', 'type': 'university', 'ownership': 'State'}

Command Line Interface
----------------------

Once installed, **Fakernaija** provides the ``naija`` command-line interface (CLI), powered by the `Click <https://click.palletsprojects.com/>`_ library. This CLI simplifies data generation directly from your terminal. Below are some examples to help you get started:

.. code-block:: bash

    $ naija email --domain unn.edu.ng --tribe igbo --gender female
    somtochi.mbakwe@unn.edu.ng

    $ naija phonenumber --network glo --prefix 0805
    08053791792

To generate multiple outputs, use the ``--repeat`` (or ``-r``) flag:

.. code-block:: bash

    $ naija email --domain unn.edu.ng --tribe igbo --gender female --repeat 3
    maduike.ugochi@unn.edu.ng
    uzo.chukwu2002@unn.edu.ng
    mmasinwodo25@unn.edu.ng

    $ naija full_name --middlename -r 3
    Tamunoteim Akpobari Erebi
    Ousmane Seydou Ahmed
    Femi Kayode Ajayi

You can export the generated data to various formats using the ``--output`` (or ``-o``) flag:

.. code-block:: bash

    $ naija full_name --repeat 1000 --tribe edo --gender female --middle_name --output csv
    Generated full names saved to /home/projectdir/full_name.csv

    $ naija email --repeat 1000 --domain gov.ng -o json
    Generated emails saved to /home/projectdir/email.json

    $ naija phone_number --repeat 1000 --network mtn --prefix 0803 --output text
    Generated phone numbers saved to /home/projectdir/phone_number.txt

Next Steps
----------

Now that you have a basic understanding of **Fakernaija**, you can move onto the :doc:`faker` to find out all available methods.

You can also check out the following sections:

API Reference
^^^^^^^^^^^^^

The API Reference section provides detailed documentation on the modules and classes in the **Fakernaija** library. Here are the key components:

- :doc:`mixins`: Specialized classes handling specific data generation tasks.
- :doc:`providers`: The data providers that work behind the scenes with Mixins to generate data.

.. toctree::
    :caption: API Reference
    :maxdepth: 1
    :hidden:

    mixins
    providers

Get Involved
^^^^^^^^^^^^

If you want to contribute to **Fakernaija**, this section is your guide to the development process. Key sections include:

- :doc:`contributing`: No be beans, but we've made it as easy as possible to contribute to the library.
- :doc:`documentation`: If you'd like to update the docs, this guide will show you the ropes.
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
^^^^

This section provides information about the project itself:

- :doc:`changelog`: Think of this as our `Before and After` story — see what has changed.
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

If you find this project useful or worthy of your attention, please `Star the repository <https://github.com/Pythonian/fakernaija>`_. Your contributions, feedback, and suggestions are always welcome!

Happy coding!
