# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.0.3] - 2024-05-15

### Added

- *postal_code* key to the states dictionary in `states.json` file
- Added more last names to the file `ethnicities/last_names.json`
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
