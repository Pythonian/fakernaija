Naija Class
===========

Overview
--------

The ``Naija`` class is your go-to guy for generating all sorts of Nigerian data. You can think of it as your ultimate data plug — whether you need to generate Nigerian names, email addresses, phone numbers, state information or even school data.

Initialization
--------------

Setting up the ``Naija`` class is as easy as `ABC`. Just import the class and create an instance of ``Naija``, and you're good to go:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

In this example, we created an instance of the ``Naija`` class named ``naija``. Now, this ``naija`` has access to all available methods from the ``Naija`` class.

.. code-block:: python

    >>> # Generate an email address
    >>> email = naija.email()
    >>> print(f"Email: {email}")

    >>> # Generate a Nigerian full name
    >>> name = naija.full_name()
    >>> print(f"Nigerian name: {name}")

Reference
---------

The ``Naija`` class gives you access to a variety of methods, each tied to a specific type of data.

You can explore the list of available ``Naija`` methods below to see various data generation options:

.. toctree::
   :maxdepth: 2

   naija/course
   naija/degree
   naija/email
   naija/faculty
   naija/marital_status
   naija/name
   naija/phonenumber
   naija/religion
   naija/school
   naija/state
