Installation
============

Overview
--------

Installing Fakernaija is straightforward and can be done using Python's package manager, ``pip``. This section will guide you through different installation processes and cover compatibility requirements.

Installing via Pip
------------------

The easiest way to install Fakernaija is through the Python Package Index (PyPI). This method ensures that you get the latest stable release of the package.

1. **Open your terminal** (or command prompt on Windows).

2. **Run the following command** to install Fakernaija:

.. code-block:: bash

    pip install -U fakernaija

3. **Verify the installation** by running a quick check in the terminal:

.. code-block:: bash

    naija --version

If the above code executes without any errors, the installation was successful.

Installing via GitHub
---------------------

If you need the latest features or bug fixes that haven't yet been released on PyPI, you can install Fakernaija directly from the GitHub repository.

1. **Open your terminal** (or command prompt on Windows).

2. **Run the following command** to install Fakernaija directly from GitHub:

.. code-block:: bash

    pip install git+https://github.com/Pythonian/fakernaija.git#egg=fakernaija

3. **Verify the installation** by running a quick check in the terminal:

.. code-block:: bash

    naija --version

If the above command executes without any errors, the installation from GitHub was successful.

Python Compatibility
--------------------

Fakernaija requires **Python 3.10** or higher. Ensure that you have the correct Python version installed by running:

.. code-block:: bash

    python3 --version

OS Compatibility
----------------

Fakernaija is platform-independent and can run on any operating system that supports Python. This includes:

- **Windows**
- **macOS**
- **Linux**

For specific OS-related issues, refer to the respective platform's documentation or `raise an issue <https://github.com/Pythonian/fakernaija/issues/new/choose>`_ on our GitHub repository.

Dependencies
------------

Fakernaija relies on the `Click <https://click.palletsprojects.com/>`_ library to expose its ``naija`` command-line interface (CLI). Without ``Click``, the ``naija`` CLI command will not function. The Click library is automatically installed when you install Fakernaija via ``pip``, so no additional steps are required.

Post-Installation Check
-----------------------

After installing Fakernaija, it's important to verify that the package is functioning correctly. If you haven't already done so, you can run:

.. code-block:: bash

    pip show --verbose fakernaija

If this command runs without errors, your installation is complete and successful.
