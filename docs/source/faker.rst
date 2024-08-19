Faker Class
===========

Overview
--------

The ``Faker`` class serves as the primary interface for generating various types of Nigerian data, providing a user-friendly, cohesive way to access different data generation features. It aggregates multiple Mixins, each responsible for specific data generation functionalities, allowing users to generate diverse types of data through a single class instance. This design abstracts the complexity of interacting with underlying Providers or Mixins, making it easier to work with the full range of available data generation methods.

Initialization
--------------

When an instance of the ``Faker`` class is created, it automatically initializes all the Mixins included in its definition. This means that all methods provided by the Mixins are immediately available through the ``Faker`` instance.

.. code-block:: python

    >>> from fakernaija import Faker

    >>> naija = Faker()

In this example, ``naija`` is an instance of the ``Faker`` class. Upon initialization, ``naija`` has access to all the data generation methods provided by the available Mixins.

``naija`` Variable
------------------

In the documentation and examples, we use the variable name ``naija`` to refer to an instance of the ``Faker`` class. This naming convention is intentional to avoid potential clashes with the popular ``Faker`` library, which is often used as follows:

.. code-block:: python

    >>> from faker import Faker

    >>> fake = Faker()

If users were to name their ``Faker`` instance ``fake``, it could lead to confusion or conflicts, especially in projects that use both ``Faker`` and ``Fakernaija``. By using ``naija``, we maintain clarity and prevent any accidental overlaps.

Usage Example
-------------

.. code-block:: python

    >>> from fakernaija import Faker

    >>> naija = Faker()

    >>> # Generate a Nigerian currency
    >>> currency = naija.currency()
    >>> print(f"Nigerian currency: {currency}")

    >>> # Generate a Nigerian fullname
    >>> name = naija.full_name()
    >>> print(f"Nigerian name: {name}")

In this example, the ``naija`` instance is used to generate a Nigerian currency and fullname, demonstrating the ease of accessing different data generation methods through the ``Faker`` class.
