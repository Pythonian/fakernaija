Commands
========

The Commands module provides a set of command-line tools that allow users to generate fake data directly from the terminal. Each command corresponds to a specific category of data, such as courses, currencies, or names. These commands are designed to be flexible, allowing users to specify options and customize the generated data.

.. code-block:: bash

   naija [--version] [--help]
         [-r / --repeat] COMMAND [ARGS]...

Where:
   * ``naija`` is the main command to invoke to run any of the sub commands.
   * ``--version`` shows the version of the library.
   * ``--help`` shows the help message.
   * ``-r`` or ``--repeat`` will generate a specified number of output
   * ``COMMAND`` is the command to be run to generate an output.
   * ``ARGS`` are the optional parameters that can be passed to a command.

Below, you'll find the documentation for each command, including usage examples and available options.

.. toctree::
   :maxdepth: 2

   cli/course
   cli/currency
   cli/data
   cli/degree
   cli/email
   cli/faculty
   cli/name
   cli/phonenumber
   cli/school
   cli/state
