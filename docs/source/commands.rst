Commands
========

Overview
--------

The Commands module provides a set of command-line tools that allow users to generate various types of data directly from the terminal. Each command corresponds to a specific category of data, with available options to also customize the generated data.

Syntax
------

To run any command, use the ``naija`` command followed by a category command and any optional arguments. The general structure of the command is as follows:

.. code-block:: bash

   naija [OPTIONS] COMMAND [ARGS]...

* ``naija``: The primary command used to access all other category commands.
* ``COMMAND``: The category command to execute, responsible for generating specific types of data.
* ``ARGS``: Optional parameters that can be passed to a category command to filter the generated output.

**Options**:

- ``--version``: Show the version of the ``naija`` library and exit.
- ``--help``: Show a help message and exit.

.. code-block:: bash

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

Reference
---------

Each category command is documented with usage instructions and practical examples. Refer to the specific sections below for detailed guidance on using each command.

.. toctree::
   :maxdepth: 2

   commands/course
   commands/currency
   commands/degree
   commands/email
   commands/faculty
   commands/name
   commands/phonenumber
   commands/school
   commands/state
