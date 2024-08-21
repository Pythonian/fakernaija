Installation
============

Overview
--------

Installing Fakernaija is straightforward and can be done using Python's package manager, ``pip``. This section will guide you through different installation methods and cover compatibility requirements.

Installing via Pip
------------------

The easiest and recommended way to install Fakernaija is through the Python Package Index (PyPI). This method ensures that you get the latest stable release of the package.

1. **Open your terminal** (or command prompt on Windows).

2. **Run the following command** to install Fakernaija:

   .. code-block:: bash

      pip install -U fakernaija

3. **Verify the installation** by checking the version installed:

   .. code-block:: bash

      naija --version

   If the above command executes without errors, the installation was successful.

Installing via GitHub
---------------------

If you want access to the latest features or bug fixes that haven't been released on PyPI, you can install Fakernaija directly from the GitHub repository.

1. **Open your terminal** (or command prompt on Windows).

2. **Run the following command** to install Fakernaija from GitHub:

   .. code-block:: bash

      pip install git+https://github.com/Pythonian/fakernaija.git#egg=fakernaija

3. **Verify the installation** by checking the version installed:

   .. code-block:: bash

      naija --version

   If the above command executes without errors, the installation from GitHub was successful.

Python Compatibility
--------------------

Fakernaija requires **Python 3.10** or higher. To check your Python version, run:

.. code-block:: bash

   python3 --version

If your Python version is below 3.10, you may have issues while using Fakernaija.

OS Compatibility
----------------

Fakernaija is platform-independent and works on any operating system that supports Python, including:

- **Windows**
- **macOS**
- **Linux**

For OS-specific issues, refer to the respective platform's documentation or `open an issue <https://github.com/Pythonian/fakernaija/issues/new/choose>`_ on our GitHub repository.

Dependencies
------------

Fakernaija relies on the `Click <https://click.palletsprojects.com/>`_ library to power its ``naija`` command-line interface (CLI). This dependency is automatically installed when you install Fakernaija via ``pip``, so no extra steps are needed.

Post-Installation Check
-----------------------

After installing Fakernaija, it's important to verify that the package is functioning correctly. To confirm the installation, you can run:

.. code-block:: bash

   pip show --verbose fakernaija

If this command runs without errors, your installation is complete and Fakernaija is ready to use.
