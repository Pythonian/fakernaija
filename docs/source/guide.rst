Usage Guide
===========

Overview
--------

This guide explores the various features available in **Fakernaija**, providing you with the information needed to generate realistic Nigerian data efficiently.

Basic Usage
-----------

Once you have installed Fakernaija as described in the :doc:`installation` guide, using it is straightforward. Start by launching your Python interpreter and exploring the following examples:

.. code-block:: python

    from fakernaija import Faker

    naija = Faker()

    print(naija.full_name())
    # Output: 'Ugochi Maduike'

    print(naija.state_capital())
    # Output: 'Owerri'

    print(naija.course_name())
    # Output: 'Introduction to Computer Science'

    print(naija.degree_name())
    # Output: 'Bachelor of Pharmacy'

    print(naija.faculty_name())
    # Output: 'Pharmaceutical Sciences'

Customizing Data Generation
---------------------------

Fakernaija allows you to customize the generated data by passing parameters to methods, giving you greater control over the results:

.. code-block:: python

    from fakernaija import Faker

    naija = Faker()

    print(naija.email(tribe="igbo", gender="female", domain="unn.edu.ng"))
    # Output: 'maduike.ugochi@unn.edu.ng'

    print(naija.phone_number(network="airtel", prefix="0902"))
    # Output: '09021234567'

    print(naija.school_name(acronym=True, ownership="federal", school_type="university"))
    # Output: 'UNN'

Consistent Randomization
------------------------

Fakernaija tries to ensure that each method call returns a different result within the same session until all possible outcomes are exhausted:

.. code-block:: python

    from fakernaija import Faker

    naija = Faker()

    for _ in range(5):
        print("A random MTN Phone number:", naija.phone_number(network="mtn"))
        # A random MTN Phone number: 08160189846
        # A random MTN Phone number: 09130280890
        # A random MTN Phone number: 08065421583
        # A random MTN Phone number: 08142772705
        # A random MTN Phone number: 08066980070

Data Representation
-------------------

If you need to retrieve complete data objects rather than individual attributes, Fakernaija supports this functionality, enabling easy integration into more complex data structures:

.. code-block:: python

    from fakernaija import Faker

    naija = Faker()

    print(naija.course())
    # Output: "{'name': 'Introduction to Computer Science', 'code': 'COS101'}"

    print(naija.currency())
    # Output: "{'code': 'NGN', 'name': 'Nigerian naira', 'symbol': '₦'}"

    print(naija.degree())
    # Output: "{'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}"

    print(naija.school())
    # Output: "{'name': 'Lagos State University', 'acronym': 'LASU', 'state': 'Lagos', 'type': 'university', 'ownership': 'State'}"

Command-Line Interface (CLI)
----------------------------

Fakernaija also lets you easily generate data by executing commands directly from your terminal:

.. code-block:: bash

    $ naija full_name --repeat 5
    Ugochi Maduike
    Lolade Lawal
    Usman Danladi
    Nasir Bello
    Ihuoma Maduabuchi

    $ naija email --domain example.com --tribe yoruba
    alayode.mustapha23@example.com

    $ naija phonenumber --repeat 3 --network glo --prefix 0805
    08059845756
    08053408825
    08051024278

Exporting Data
--------------

If you need to export your generated data to various file formats, Fakernaija supports CSV, JSON, and plain text exports:

.. code-block:: bash

    $ naija data --repeat 30 --fields fullname,email,phonenumber --output csv
    Generated data saved to /home/projectdir/data.csv

    $ naija data --repeat 30 --fields fullname,email,phonenumber --output json
    Generated data saved to /home/projectdir/data.json

    $ naija data --repeat 30 --fields fullname,email,phonenumber --output text
    Generated data saved to /home/projectdir/data.txt

Error Handling
--------------

While using Fakernaija, you might encounter errors due to incorrect parameter usage. Always verify that the parameters passed are correct and supported. If in doubt, refer to the API documentation for the list of valid values for each method.
