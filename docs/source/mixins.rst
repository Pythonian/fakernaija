Mixins
======

The ``Mixins`` module serves as a foundational component of the **Fakernaija** library, offering a collection of classes that encapsulate reusable methods for generating specific categories of data. Each ``Mixin`` class focuses on a distinct domain and interacts with corresponding :doc:`providers` to deliver realistic Nigerian data.

Overview
--------

``Mixins`` in **Fakernaija** are designed to be composable, allowing the ``Faker`` class to inherit from multiple ``Mixins`` and thus aggregate their functionalities. This modular approach ensures that each ``Mixin`` class is responsible for a single aspect of data generation.

How to Use
----------

When you create an instance of the :doc:`faker`, it automatically inherits methods from all the included ``Mixin`` classes. You can then call these methods to generate various types of data. The ``Mixins`` abstract away the complexities of data retrieval and processing, providing you with a simple and intuitive API.

Classes
-------

The following are the ``Mixin`` classes available in the **Fakernaija** library. Each ``Mixin`` class is documented with examples to illustrate its usage. These examples can be run directly in your Python environment to see the results.

.. toctree::
   :maxdepth: 1

   mixins/course
   mixins/currency
   mixins/degree
   mixins/email
   mixins/faculty
   mixins/name
   mixins/phonenumber
   mixins/school
   mixins/state
