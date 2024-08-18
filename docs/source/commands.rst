Commands
========

Overview
--------

The Commands module provides a set of command-line tools that allow users to generate various types of data directly from the terminal. Each command corresponds to a specific category of data, with available options to also customize the generated data.

Syntax
------

To run any command, invoke the main ``naija`` command followed by the desired subcommand and options.

.. code-block:: bash

   naija [--version] [--help]
         [-r / --repeat] COMMAND [ARGS]...

**Parameters**:
   * ``naija``: The primary command used to access all subcommands.
   * ``--version``: Displays the current version of the library.
   * ``--help``: Shows the help message with information on usage.
   * ``-r`` or ``--repeat``: Specifies how many times the command should generate the output.
   * ``COMMAND``: The subcommand to execute, responsible for generating specific types of data.
   * ``ARGS``: Optional parameters that can be passed to a subcommand to filter the generated output.

Reference
---------

Each command's documentation includes usage instructions and examples that you can run on your terminal. Refer to the respective sections below for information on how to use each command.

.. toctree::
   :maxdepth: 2

   commands/course
   commands/currency
   commands/data
   commands/degree
   commands/email
   commands/faculty
   commands/name
   commands/phonenumber
   commands/school
   commands/state
