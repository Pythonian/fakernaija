naija - CLI
===========

Overview
--------

The ``naija`` CLI (Command Line Interface) is designed to provide users with a way to generate Nigerian-specific data directly from the terminal. Each command in the CLI corresponds to a different type of data, allowing for rapid generation of test data without writing any code.

Why Use the CLI?
----------------

- **Quick Access**: Generate data directly from your terminal without needing to write scripts.
- **Customization**: Use various options to tailor the generated data to your specific needs.
- **Export Capability**: Output your generated data to multiple formats, including JSON, CSV, and plain text.

Syntax
------

To execute any command, use the ``naija`` command followed by the category command and optional arguments. The general structure is as follows:

.. code-block:: console

   naija [OPTIONS] COMMAND [ARGS]...

* ``naija``: The main command used to access all other category commands.
* ``COMMAND``: The specific category command to execute.
* ``ARGS``: Optional arguments and flags to customize the output.

**Options**:

- ``--version``: Display the current version of Fakernaija and exit.
- ``--help``: Display help information for the CLI or specific commands.

Basic Usage
-----------

Running the ``naija`` command without any subcommands will display a help message listing all available options and commands:

.. code-block:: console

    $ naija
    Usage: naija [OPTIONS] COMMAND [ARGS]...

      A CLI for generating and returning random Nigerian data.

    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.

    Commands:
      course             Returns random course objects.
      course_code        Returns random course codes.
      course_name        Returns random course names.
      ...                ...

Below are some examples of how you can generate data with the command:

.. code-block:: console

    $ naija name --gender female --tribe yoruba
    Aduke Lawal

    $ naija email --domain technomaniac.com --tribe igbo --gender male
    muolokwu.ekene@technomaniac.com

    $ naija phonenumber --network mtn --prefix 0803
    08031234567

Exporting Data
--------------

The CLI supports exporting generated data to various formats. Use the `--output` or `-o` flag to specify the format:

.. code-block:: console

    $ naija full_name --repeat 1000 --output csv
    Generated data saved to /path/to/directory/full_name.csv

Reference
---------

Each category command is documented with practical examples. You can find a guide to any of the commands you want to work with below:

.. toctree::
   :maxdepth: 2

   commands/course
   commands/degree
   commands/email
   commands/faculty
   commands/license_plate
   commands/marital_status
   commands/name
   commands/phonenumber
   commands/religion
   commands/school
   commands/state
