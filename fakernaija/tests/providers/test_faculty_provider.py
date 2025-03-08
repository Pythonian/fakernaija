"""Unit tests for the FacultyProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers import FacultyProvider


class TestFacultyProvider(unittest.TestCase):
    """Test suite for the FacultProvider class."""

    @patch("fakernaija.providers.faculty.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:
        """Setup mock data for faculties."""
        self.mock_faculties_data = [
            {
                "name": "Basic Medical Sciences",
                "departments": ["Human Anatomy", "Physiology"],
            },
            {
                "name": "Communications and Media Studies",
                "departments": [
                    "Strategic Communications",
                    "Advertising",
                    "Broadcasting",
                    "Development Communications Studies",
                    "Film and Multimedia",
                    "Information and Media Studies",
                    "Journalism and Media Studies",
                    "Mass Communications",
                    "Public Relations",
                ],
            },
        ]
        mock_load_json.return_value = self.mock_faculties_data
        self.faculty_provider = FacultyProvider()

    def test_get_faculties(self) -> None:
        """Test the get_faculties method returns a list of Faculties."""
        faculties = self.faculty_provider.get_faculty_names()
        expected_faculties = [
            "Basic Medical Sciences",
            "Communications and Media Studies",
        ]
        self.assertEqual(faculties, expected_faculties)

    def test_get_departments(self) -> None:
        """Test the get_departments method returns a list of departments."""
        departments = self.faculty_provider.get_department_names()
        expected_departments = [
            "Human Anatomy",
            "Physiology",
            "Strategic Communications",
            "Advertising",
            "Broadcasting",
            "Development Communications Studies",
            "Film and Multimedia",
            "Information and Media Studies",
            "Journalism and Media Studies",
            "Mass Communications",
            "Public Relations",
        ]
        self.assertEqual(departments, expected_departments)

    def test_get_department_names_with_filter(self) -> None:
        """Test the get_department_names method with a faculty filter."""
        expected_departments = ["Human Anatomy", "Physiology"]
        self.assertEqual(
            self.faculty_provider.get_department_names("Basic Medical Sciences"),
            expected_departments,
        )

    def test_get_department_names_with_filter_case_insensitive(self) -> None:
        """Test the get_department_names method with a case-insensitive faculty filter."""
        expected_departments = ["Human Anatomy", "Physiology"]
        self.assertEqual(
            self.faculty_provider.get_department_names("basic medical sciences"),
            expected_departments,
        )

    def test_get_department_names_with_invalid_faculty(self) -> None:
        """Test the get_department_names method with an invalid faculty."""
        with self.assertRaises(ValueError) as context:
            self.faculty_provider.get_department_names("Invalid Faculty")
        self.assertIn("Invalid faculty name", str(context.exception))
        self.assertIn("Valid faculties are:", str(context.exception))
