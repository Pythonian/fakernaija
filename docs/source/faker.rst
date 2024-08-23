Faker Class
===========

Overview
--------

The ``Faker`` class is your go-to guy for generating all sorts of Nigerian data. You can think of it as your ultimate data plug — whether you need to generate Nigerian names, email addresses, phone numbers, state information or even school data.

Initialization
--------------

Setting up the ``Faker`` class is as easy as `ABC`. Just import the class and create an instance of ``Faker``, and you're good to go:

.. code-block:: python

    >>> from fakernaija import Faker
    >>> naija = Faker()

In this example, we created an instance of the ``Faker`` class named ``naija``. Now, this ``naija`` has access to all available methods from the ``Faker`` class.

.. code-block:: python

    >>> # Generate a Nigerian currency
    >>> currency = naija.currency()
    >>> print(f"Nigerian currency: {currency}")

    >>> # Generate a Nigerian full name
    >>> name = naija.full_name()
    >>> print(f"Nigerian name: {name}")

Reference
---------

The ``Faker`` class gives you access to a variety of methods, each tied to a specific type of data.

You can explore the list of available Faker methods below to see various data generation options:

.. toctree::
   :maxdepth: 2

   faker/course
   faker/currency
   faker/degree
   faker/email
   faker/faculty
   faker/name
   faker/phonenumber
   faker/school
   faker/state
