# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

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
