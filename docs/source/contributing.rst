Contributing
============

Thank you for your interest in contributing to Fakernaija! This guide will walk you through the process of setting up your development environment, testing your changes, and submitting your contributions.


Prerequisites
-------------

This guide assumes the following:

- **Python 3.10 or higher** installed
- A **Linux/MacOS environment** or **WSL** (if using Windows)


Getting Started
---------------

To contribute to Fakernaija, you'll need to follow the steps below. A `Makefile <https://github.com/Pythonian/fakernaija/blob/main/Makefile>`_ has been provided for easy project setup.

1. Create a fork of `Fakernaija <https://github.com/Pythonian/fakernaija>`_ to your GitHub account.

2. Clone your fork to your local machine.

   .. code-block:: console

      git clone https://github.com/your-username/fakernaija.git

   Replace ``your-username`` with your GitHub username.

3. Move into the cloned project directory.

   .. code-block:: console

      cd fakernaija

4. Set up the upstream remote to keep your fork in sync with the original repository.

   .. code-block:: console

      git remote add upstream https://github.com/Pythonian/fakernaija.git

5. Create a virtual environment to isolate your project dependencies.

   .. code-block:: console

      make venv

   This will create a virtual environment in the ``.venv`` directory.

   Now **activate** the virtual environment with:

   .. code-block:: console

      source .venv/bin/activate

5. Install the necessary dependencies for development.

   .. code-block:: console

      make install

6. Ensure your development environment has been properly setup with the command:

   .. code-block:: console

      make check

If everything goes green, then you have successfully setup your development environment for contributions.

If you wish to reset your development environment to a clean slate, then run:

.. code-block:: console

   make clean


Contribution Process
--------------------

For any change you wish to make, we encourage you to follow the guideline we have set out.

1. **Open an Issue**: Create a `new issue <https://github.com/Pythonian/fakernaija/issues/new/choose>`_ and itemize your proposed changes.

2. **Create a New Branch**: Always create a new branch for your contributions.

   .. code-block:: console

      git checkout -b feature-or-bugfix-name

   Replace ``feature-or-bugfix-name`` with a descriptive name that reflect the work you are doing.

3. **Testing Your Changes**: Before committing your code, ensure your changes do not break existing functionality.

   .. code-block:: console

      make check

   **Note**: If you add new functionality, please include corresponding tests and update the documentation where necessary.

4. **Commit Your Changes**: Make sure your commit messages are clear and concise.

   .. code-block:: console

      git add .
      git commit -m "feat: Brief description of your changes"

   We encourage you to follow `conventional commit <https://www.conventionalcommits.org/>`_ guidelines for your commit messages.

5. **Push Your Changes**: Push your branch to your forked repository.

   .. code-block:: console

      git push origin feature-or-bugfix-name

6. **Submit a Pull Request**:

   - Go to the `Fakernaija repository <https://github.com/Pythonian/fakernaija>`_ on GitHub.
   - Click the ``Compare & pull request`` button.
   - Provide a title and description of your changes, including the issue number.
   - Submit the pull request for review.

   **Note**: Ensure that your pull request is up to date with the upstream `main` branch before submitting it.

7. **Review Process and Merging**: Your pull request will be reviewed by the maintainers. Be prepared to make adjustments based on their feedback. Once your pull request is approved, it will be merged into the main branch. **Only repository maintainers** have the authority to build and push releases to PyPI.


Documentation Changes
---------------------

If you make changes to the code that affect the documentation, or if you are improving the documentation, follow these steps:

1. **Build the Documentation**:

   .. code-block:: console

      make docs

   This will generate the HTML documentation in the ``docs/build`` directory.

2. **Update the Documentation**: Make your changes to the ``.rst`` files in the ``docs`` directory.

3. **Verify Your Changes**: Ensure that the documentation builds correctly by viewing the generated HTML files in a browser.

4. **Commit and Push Documentation Changes:**

   .. code-block:: console

      git add .
      git commit -m "docs: commit message for the doc update"
      git push origin doc-branch-name


Updating your Fork
------------------

To keep your fork up to date with the original repository and handle any potential merge conflicts, follow these steps:

1. **Check Out Your main Branch**: Start by making sure you are on your fork's ``main`` branch.

   .. code-block:: console

      git checkout main

2. **Fetch the Latest Changes from Upstream**: Fetch the latest changes from the original repository (upstream). This downloads the changes but does not apply them to your branch yet.

   .. code-block:: console

      git fetch upstream

3. **Merge the Upstream Changes into Your main Branch**: Merge the fetched changes from the upstream ``main`` branch into your local ``main`` branch.

   .. code-block:: console

      git merge upstream/main

   If there are no conflicts, proceed to step 4. However, if there are merge conflicts, follow the steps below to resolve them before continuing:

   a. **Identify Conflicted Files**: Git will list the files with conflicts after the merge attempt. You can also see the list by running:

      .. code-block:: console

         git status

   b. **Open Conflicted Files**: Open each conflicted file in your text editor or IDE. Git marks the conflicts with ``<<<<<<<``, ``=======``, and ``>>>>>>>`` markers. The content between ``<<<<<<<`` and ``=======`` is your version, and the content between ``=======`` and ``>>>>>>>`` is the upstream version.

   c. **Resolve Conflicts**: Edit the conflicted sections to choose the correct code, or manually combine the changes as needed. Remove the conflict markers (``<<<<<<<``, ``=======``, ``>>>>>>>``) after resolving the conflicts.

   d. **Mark Files as Resolved**: After resolving all conflicts in a file, mark it as resolved using:

      .. code-block:: console

         git add <file>

      Do this for each conflicted file.

   e. **Continue the Merge**: After resolving all conflicts and staging the resolved files, complete the merge by running:

      .. code-block:: console

         git commit

      Git may prompt you to enter a commit message describing the merge. You can use the default message or write your own.

4. **Push the Updated `main` Branch to Your Fork**: Finally, push the updated ``main`` branch back to your GitHub fork.

   .. code-block:: console

      git push origin main

By following these steps, you will keep your fork up to date with the original repository and properly handle any merge conflicts that arise during the process.


Coding Guidelines
-----------------

Adhering to coding standards is crucial for maintaining the quality, consistency, and security of the project. Follow these guidelines to ensure that your contributions meet the project's standards.

**Code Style**

- **Follow PEP 8**: Adhere to PEP 8 for Python code style, including indentation, spacing, and line length. The project is configured to use ``ruff`` with custom settings for code formatting and linting.
- **Meaningful Names**: Use clear, descriptive names for variables, functions, and classes.
- **Docstrings**: Write comprehensive docstrings for all functions and classes. Use the Google style for docstrings, as configured in ``pyproject.toml``.
- **Quotes and Indentation**: Use double quotes for strings and follow the specified indentation style (4 spaces). The ``ruff`` configuration ensures consistency across the project.

**Type Annotations**

- **Enforce Type Annotations**: All functions should have explicit type annotations. The ``mypy`` tool is configured to enforce type correctness, and you should address any type errors before submitting code.

**Linting and Formatting**

- **Linting**: Use ``ruff`` for linting. The project's ``tox`` configuration includes a linting environment that checks for common issues. Run ``tox -e lint`` before committing code to ensure linting passes without issues.
- **Formatting**: The code should be formatted using the ``ruff`` formatter. Run ``tox -e format`` to automatically format your code before committing. The project enforces consistent formatting, including quote style and line endings.

**Testing**

- **Unit Tests**: All new features and bug fixes should include unit tests. Tests are located in the ``fakernaija/tests`` directory and should follow the structure of the existing tests.
- **Coverage**: The project uses ``coverage`` to ensure that tests cover a substantial portion of the codebase. Aim for at least 80% test coverage, and check this by running ``tox -e test``.

**Security**

- **Security Checks**: The project uses ``bandit`` to identify potential security issues. Run ``tox -e security`` to check your code for common security flaws, and fix any issues before submitting your code.

**Documentation**

- **Documentation**: Update the documentation to reflect any changes or new features you introduce. The project uses Sphinx for documentation, and you can build the HTML documentation using ``make docs``.
- **Docstring Format**: Ensure that your docstrings are formatted according to the project's standards, as enforced by ``pydocstyle``.

**Pre-Commit Hooks**

- **Pre-Commit Checks**: The project uses pre-commit hooks to automatically check for common issues before committing code. These checks include verifying the format, linting, and ensuring that no large files or private keys are committed.
- **Setup**: Install the pre-commit hooks by running ``make install-dev``. This step is required before your first commit.

**Dependency Management**

- **Dependencies**: The project manages dependencies through ``pyproject.toml`` and ``tox``. Ensure that all necessary dependencies are listed in these files and avoid adding unnecessary packages.
- **Environment Isolation**: Use the provided Makefile to create a virtual environment and install dependencies. This ensures that your development environment is consistent with the project's requirements.

**Contribution Process**

- **Commit Messages**: Write clear, concise commit messages that explain the purpose of the changes. Follow the project's guidelines for commit message format.
- **Pull Requests**: Before submitting a pull request, ensure that all tests pass, code is linted and formatted correctly, and documentation is updated. Use the ``make check`` command to verify this.


Help and Support
----------------

If you encounter any issues during the contribution process or you have any questions to ask or need additional help, feel free to `open an issue <https://github.com/Pythonian/fakernaija/issues/new/choose>`_ on the GitHub repository or reach out to `Seyi Pythonian <https://github.com/Ajibel>`_.

Thank you for your contribution!
