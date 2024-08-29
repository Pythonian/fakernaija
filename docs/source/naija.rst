Naija Class
===========

Overview
--------

The ``Naija`` class serves as the main interface for generating Nigerian-specific data with the Fakernaija library. You can see it as your ultimate data plug for generating all sorts of Nigerian data like Nigerian names, email addresses, phone numbers, state information, school data, bank information and more.

Initialization
--------------

Setting up the ``Naija`` class is as easy as `ABC`. Just import the class and create an instance of ``Naija``, and you're good to go:

.. code-block:: python

    >>> from fakernaija import Naija
    >>> naija = Naija()

In the above example, an instance of the ``Naija`` class named ``naija`` is created, giving you access to all the data generation methods available within the class.

Quick Examples
--------------

Once initialized, you can generate various types of Nigerian data with just a method call. Below are some examples:

.. code-block:: python

    >>> # Generate a Nigerian email address
    >>> email = naija.email()
    >>> print(f"Email: {email}")
    Email: somtochi.mbakwe@gmail.com

    >>> # Generate a Nigerian full name
    >>> name = naija.full_name()
    >>> print(f"Nigerian name: {name}")
    Nigerian name: Ugochi Maduike

    >>> # Generate a Nigerian phone number
    >>> phone = naija.phone_number()
    >>> print(f"Phone Number: {phone}")
    Phone Number: 08031234567

    >>> # Generate a Nigerian license plate
    >>> license_plate = naija.license_plate()
    >>> print(f"License Plate: {license_plate}")
    License Plate: KJA-234AB

Reference
---------

Each method of the ``Naija`` class has its own documentation, complete with usage examples, parameters, and expected outputs. For more understanding of each method, click on the links below:

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
