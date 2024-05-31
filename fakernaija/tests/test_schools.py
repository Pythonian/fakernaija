"""Unit tests for the SchoolProvider class.

This module contains unit tests for the SchoolProvider class, which provides methods
for generating random Nigerian educational institutions. The tests ensure that the
methods return the expected school type and ownership.
"""

import json
import unittest
from typing import Any
from unittest.mock import mock_open, patch

from fakernaija.providers.schools import SchoolProvider


class TestSchoolProvider(unittest.TestCase):
    """Unit tests for the SchoolProvider class."""

    def setUp(self) -> None:
        """Set up the SchoolProvider instance for testing."""
        self.school_provider = SchoolProvider()
        self.valid_data = {
            "schools": [
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "location": "Lagos",
                    "type": "University",
                    "ownership": "Federal",
                    "year_founded": 1962,
                },
            ],
        }
        self.invalid_data = {"schools": "invalid_data"}
        self.valid_school = {
            "name": "University of Lagos",
            "acronym": "UNILAG",
            "location": "Lagos",
            "type": "University",
            "ownership": "Federal",
            "year_founded": 1962,
        }
        self.invalid_school = {
            "name": "University of Lagos",
            "acronym": "UNILAG",
            "location": "Lagos",
            "type": "University",
        }

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"schools": []}),
    )
    def test_load_json_success(self, mock_file: Any) -> None:  # noqa: ARG002, ANN401
        """Test loading JSON data successfully."""
        data = self.school_provider.load_json(self.school_provider.data_path)
        self.assertIn("schools", data)
        self.assertIsInstance(data["schools"], list)

    @patch("pathlib.Path.open", new_callable=mock_open)
    def test_load_json_file_not_found(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test handling of file not found error."""
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            self.school_provider.load_json("none.json")

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            self.school_provider.load_json(self.school_provider.data_path)
        self.assertIn("Error decoding JSON", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"invalid_key": []}),
    )
    def test_load_json_invalid_data_structure(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of invalid data structure."""
        with self.assertRaises(ValueError) as context:
            self.school_provider.load_json(self.school_provider.data_path)
        self.assertIn("Invalid data format", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"schools": [{"name": "Test School"}]}),
    )
    def test_load_json_missing_keys_in_school(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of missing required keys in school data."""
        with self.assertRaises(ValueError) as context:
            self.school_provider.load_json(self.school_provider.data_path)
        self.assertIn("Invalid data format", str(context.exception))

    def test_validate_schools_data(self) -> None:
        """Test validating the schools data."""
        self.assertTrue(self.school_provider.validate_schools_data(self.valid_data))
        self.assertFalse(self.school_provider.validate_schools_data(self.invalid_data))

    def test_validate_school_data(self) -> None:
        """Test validating individual school data."""
        self.assertTrue(self.school_provider.validate_school_data(self.valid_school))
        self.assertFalse(self.school_provider.validate_school_data(self.invalid_school))

    def test_get_schools(self) -> None:
        """Test getting a list of all schools' names."""
        schools = self.school_provider.get_schools()
        self.assertIn("University of Lagos", schools)

    def test_get_school_by_name(self) -> None:
        """Test getting information about a school by its name."""
        school_info = self.school_provider.get_school_by_name("University of Lagos")
        self.assertIsNotNone(school_info, "Expected school info to not be None")
        if school_info:
            self.assertEqual(school_info["name"], "University of Lagos")
            self.assertEqual(school_info["acronym"], "UNILAG")
            self.assertEqual(school_info["location"], "Lagos")

    def test_nonexistent_school_by_name(self) -> None:
        """Test getting information about a nonexistent school by its name."""
        school_info = self.school_provider.get_school_by_name("University of Amala")
        self.assertIsNone(school_info)

    def test_get_school_acronym(self) -> None:
        """Test getting a school acronym."""
        acronyms = self.school_provider.get_school_acronyms()
        self.assertIn("UNILAG", acronyms)

    def test_get_school_by_location(self) -> None:
        """Test getting a school located at the specified location."""
        schools = self.school_provider.get_schools_by_location("Lagos")
        self.assertEqual(schools[0]["name"], "University of Lagos")

    def test_get_universities_by_location(self) -> None:
        """Test getting a university located at the specified location."""
        schools = self.school_provider.get_universities_by_location("Lagos")
        self.assertEqual(schools[0]["name"], "University of Lagos")

    def test_get_polytechnics_by_location(self) -> None:
        """Test getting a polytechnic located at the specified location."""
        schools = self.school_provider.get_polytechnics_by_location("Rivers")
        self.assertEqual(schools[0]["name"], "Port Harcourt Polytechnic")

    def test_get_colleges_of_education_by_location(self) -> None:
        """Test getting a college of education located at the specified location."""
        schools = self.school_provider.get_colleges_of_education_by_location("Ogun")
        self.assertEqual(schools[0]["name"], "Federal College of Education, Abeokuta")

    def test_get_federal_schools(self) -> None:
        """Test getting a list of all federal schools."""
        schools = self.school_provider.get_federal_schools()
        self.assertEqual(schools[0]["ownership"], "Federal")

    def test_get_state_schools(self) -> None:
        """Test getting a list of all state schools."""
        schools = self.school_provider.get_state_schools()
        self.assertEqual(schools[0]["ownership"], "State")

    def test_get_private_schools(self) -> None:
        """Test getting a list of all private schools."""
        schools = self.school_provider.get_private_schools()
        self.assertEqual(schools[0]["ownership"], "Private")

    def test_get_universities(self) -> None:
        """Test getting a list of all universities."""
        schools = self.school_provider.get_universities()
        self.assertEqual(schools[0]["type"], "University")

    def test_get_polytechnics(self) -> None:
        """Test getting a list of all polytechnics."""
        schools = self.school_provider.get_polytechnics()
        self.assertEqual(schools[0]["type"], "Polytechnic")

    def test_get_colleges_of_education(self) -> None:
        """Test getting a list of all colleges of education."""
        schools = self.school_provider.get_colleges_of_education()
        self.assertEqual(schools[0]["type"], "College of Education")

    def test_get_federal_universities(self) -> None:
        """Test getting a list of all federal universities."""
        schools = self.school_provider.get_federal_universities()
        self.assertEqual(schools[0]["ownership"], "Federal")

    def test_get_federal_polytechnics(self) -> None:
        """Test getting a list of all federal polytechnics."""
        schools = self.school_provider.get_federal_polytechnics()
        self.assertEqual(schools[0]["ownership"], "Federal")

    def test_get_federal_colleges_of_education(self) -> None:
        """Test getting a list of all federal colleges of education."""
        schools = self.school_provider.get_federal_colleges_of_education()
        self.assertEqual(schools[0]["ownership"], "Federal")
        self.assertEqual(schools[0]["type"], "College of Education")

    def test_get_state_universities(self) -> None:
        """Test getting a list of all state universities."""
        schools = self.school_provider.get_state_universities()
        self.assertEqual(schools[0]["ownership"], "State")

    def test_get_state_polytechnics(self) -> None:
        """Test getting a list of all state polytechnics."""
        schools = self.school_provider.get_state_polytechnics()
        self.assertEqual(schools[0]["ownership"], "State")

    def test_get_state_colleges_of_education(self) -> None:
        """Test getting a list of all state colleges of education."""
        schools = self.school_provider.get_state_colleges_of_education()
        self.assertEqual(schools[0]["ownership"], "State")

    def test_get_private_universities(self) -> None:
        """Test getting a list of all private universities."""
        schools = self.school_provider.get_private_universities()
        self.assertEqual(schools[0]["ownership"], "Private")

    def test_get_private_polytechnics(self) -> None:
        """Test getting a list of all private polytechnics."""
        schools = self.school_provider.get_private_polytechnics()
        self.assertEqual(schools[0]["ownership"], "Private")

    def test_get_private_colleges_of_education(self) -> None:
        """Test getting a list of all private colleges of education."""
        schools = self.school_provider.get_private_colleges_of_education()
        self.assertEqual(schools[0]["ownership"], "Private")
