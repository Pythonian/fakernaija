# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.0.13] - 2024-06-01

### Added

- Added ascii art to `README.md`
- Added a `utils.py` file to encapsulate common functionalities
- Added ability to add domains optionally to email generation
- Added email validation logic
- Added ability to specify an optional middle name for full name generation
- Unittest updates for the new functionalities added

### Refactor

- Now loading the json data for `emails.py` and `names.py` via the utility `load_json` function
- Normalized tribe and gender inputs to lowercase
- Added new test case to `test_emails.py`

### Removed

- Removed formatting with black command in `tox.ini`

## [0.0.12] - 2024-05-31

### Added

- Added flake8 line length ignore rule to `tox.ini`
- Added issue templates
- Added some information to Readme file
- Added more tests to ensure test_emails coverage reached 100
- Added code to validate the name json data structure, and updated test cases

### Refactor

- Changed assert style statement to using unittest-style assert statements
- Updated `__init__.py` and `faker.py` module docstrings
- Made changes to the `make build` command

### Removed

- Removed assert_used skipping code from bandit configuration
- Removed ruff linting in github workflow

## [0.0.11] - 2024-05-30

### Added

- Added Issue Templates for Github
- Added Pull Request Template for Github
- Added bandit and black to `tox.ini` setup
- Added Makefile

### Refactor

- Moved coverage configurations from `setup.cfg` to `tox.ini` file
- Moved mypy configurations from `mypy.ini` to `pyproject.toml`

### Removed

- Deleted `setup.cfg` file
- Deleted `mypy.ini` file

## [0.0.10] - 2024-05-29

### Added

- Added EmailProvider module and tests for the prvider methods
- Added more tests for Faker class to cover all existing methods

### Refactor

- Pinned coverage version in `tox.ini`
- Made adjustments to Faker class to handle None or empty return values
- Modified an existing school data in `schools.json`
- Split the Faker class tests based on the providers
- Removed assert and replaced with unittest-style assert calls

## [0.0.9] - 2024-05-28

### Added

- Added tox to manage test and linting
- Added github workflow for linting and testing
- Added PT027 and PT029 to list of ignored ruff rules
- Added tests on the Faker class

### Refactor

- Moved the tests folder into the fakernaija folder
- Fixed mypy errors
- Updated requirements file
- Updated pyproject.toml file with ruff configurations
- Update pre-commit hook configurations
- Updated `mypy.ini` file to remove the strict requirement

### Removed

- Removed black from pre-commit file

## [0.0.8] - 2024-05-27

### Added

- Added Requirements file
- Added docstrings to module `__init__` files
- Added more schools data
- Added `first_names.json` and `last_names.json` files for names data
- Added Unittests and coverage for the Provider classes
- Added coverage configurations to `setup.cfg`
- Added coverage version to `requirements.txt`
- Added more rules for Ruff to ignore

### Refactor

- Fix mypy indetified static type warnings in `faker.py` and `names.py` files
- Modified few names in the json names file
- Changed the structure of json name directory and files

## Removed

- Deleted the tribe folder containing names
- Delete unnecessary `__init__` files

## [0.0.7] - 2024-05-26

### Added

- Added ruff linter; linting config files and git hook with pre-commit and mypy
- Added data validation for the JSON files

### Refactor

- JSON files formatted by ruff
- Updated python files to use Type checking and made code improvements
- Changed Faker9ja package name to fakernaija

## [0.0.6] - 2024-05-19

### Refactor

- Renamed `geo.py` to `states.py`
- Removed `data/geo` folder, and moved `states.json` file into the `data` folder
- Removed `data/schools` folder, and moved `schools.json` file into the `data` folder
- Renamed `GeoProvider` to `StateProvider` and updated relevant imports

## [0.0.5] - 2024-05-17

### Added

- PhoneNumber Provider
- Added more examples to the `examples.py` file for testing

## [0.0.4] - 2024-05-16

### Added

- Schools Provider
- Added more examples to the `examples.py` file for testing

### Refactor

- Renamed `data/states` folder to `data/geo`
- Updated the path to the JSON file containing states data in `geo.py`
- Changed the option of conditionally adding a `data_path` to the files
- Modified paths to the directory containing name data files

## [0.0.3] - 2024-05-15

### Added

- *postal_code* key to the states dictionary in `states.json` file
- Added more last names to the file `tribes/last_names.json`
- Added new set of methods to generate names to the `Faker` class
- Added the `example.py` file to test class methods easily
- Added the `region` and `postal_code` methods to `Faker` class

### Refactor

- Changed *region_code* to *region_initial* in `faker.py`, `states.py` and `states.json` files
- Changed "surname" key to "name" in `ijaw/last_names.json`
- Changed `edo/last_name.json` file to `edo/last_names.json`
- Fixed "gender" keyerror issue in the method `generate_first_name`
- Changed `NameGenerator` class to `Faker`
- Changed `providers/states.py` to `providers/geo.py`
- Merged the methods in the `StateGenerator` class into the `Faker` class
- Renamed `ethnic_group` to `tribe` in all occurences
- Renamed folder `names/ethnicities` to `names/tribes`
- Correction of Postcode of Kano and Kaduna

### Removed

- Docstring example of getting all geopolitical zones in `faker.py` file
- Deleted methods description from the `NameProvider` class docstring
- Deleted the `StateGenerator` class

## [0.0.2] - 2024-05-14

### Added

- State Provider

### Removed

- example.py file

## [0.0.1] - 2024-05-13

### Added

- Name Providers for: Yoruba, Igbo, Hausa, Fulani, Edo, Ijaw
- Everything else
