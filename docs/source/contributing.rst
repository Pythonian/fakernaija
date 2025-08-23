Contributing
============

Thank you for your interest in contributing to Fakernaija! This guide will walk you through the process of setting up your development environment, testing your changes, and submitting your contributions.

Quick Start
-----------

Ready to contribute? Here's the fastest way to get started:

1. Fork the `Fakernaija repository <https://github.com/Pythonian/fakernaija>`_ on GitHub
2. Clone your fork: ``git clone https://github.com/your-username/fakernaija.git``
3. Create a virtual environment: ``python -m venv .venv``
4. Activate it and install dependencies (see detailed setup below)
5. Make your changes and add tests
6. Run ``tox`` to test your changes
7. Submit a pull request

Detailed Setup
--------------

**1. Fork and Clone**

Create a fork of `Fakernaija <https://github.com/Pythonian/fakernaija>`_ to your GitHub account, then clone it:

.. code-block:: console

   git clone https://github.com/your-username/fakernaija.git
   cd fakernaija

Replace ``your-username`` with your GitHub username.

**2. Set Up Upstream Remote**

.. code-block:: console

   git remote add upstream https://github.com/Pythonian/fakernaija.git

**3. Create Virtual Environment**

.. code-block:: console

   python -m venv .venv

**4. Activate Virtual Environment**

**On Windows:**

.. code-block:: console

   .venv\Scripts\activate

**On Linux/macOS:**

.. code-block:: console

   source .venv/bin/activate

**Install Dependencies**

.. code-block:: console

   pip install -U pip setuptools
   pip install -e .
   pip install -r docs/requirements.txt
   pip install tox pre-commit

**5. Set Up Pre-commit Hooks (Optional)**

.. code-block:: console

   pre-commit install

**6. Verify Setup**

Run the checks to ensure everything is working:

.. code-block:: console

   tox

If tests pass, you're ready to contribute!

Making Contributions
--------------------

**1. Create an Issue**

Before making changes, create a `new issue <https://github.com/Pythonian/fakernaija/issues/new/choose>`_ describing your proposed changes.

**2. Create a New Branch**

.. code-block:: console

   git checkout -b feature-or-bugfix-name

Use a descriptive name that reflects the work you're doing.

**3. Make Your Changes**

- Write your code following the coding guidelines below
- Add tests for new functionality
- Update documentation if needed

**4. Test Your Changes**

Run the full test suite:

.. code-block:: console

   tox

**5. Commit Your Changes**

.. code-block:: console

   git add .
   git commit -m "feat: Brief description of your changes"

We encourage following `conventional commit <https://www.conventionalcommits.org/>`_ guidelines.

**6. Push and Create Pull Request**

.. code-block:: console

   git push origin feature-or-bugfix-name

Then go to GitHub and create a pull request with:
- A clear title and description
- Reference to the related issue number
- Summary of changes made

Testing
-------

- Write unit tests for all new features and bug fixes
- Tests should be in the ``tests/`` directory
- Aim for good test coverage
- Use descriptive test names

Documentation Changes
---------------------

If you're updating documentation:

1. **Build the docs locally:**

   .. code-block:: console

      sphinx-build -M html docs/source/ docs/build/

2. **View the generated HTML** in ``docs/build/html/index.html``

3. **Commit documentation changes** with a clear commit message:

   .. code-block:: console

      git commit -m "docs: update installation instructions"

Keeping Your Fork Updated
--------------------------

To sync your fork with the original repository:

.. code-block:: console

   git checkout main
   git fetch upstream
   git merge upstream/main
   git push origin main

If you encounter merge conflicts, resolve them manually in your editor, then:

.. code-block:: console

   git add .
   git commit

Getting Help
------------

If you need help or have questions:

- Check existing `issues <https://github.com/Pythonian/fakernaija/issues>`_ for similar problems
- Create a new issue with the "question" label
- Join discussions in existing pull requests

Thank you for contributing to Fakernaija!
