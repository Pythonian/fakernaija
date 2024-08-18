"""Unit tests for the FacultyProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers.faculty_provider import FacultyProvider


class TestFacultyProvider(unittest.TestCase):
    """Test suite for the FacultProvider class."""

    @patch("fakernaija.providers.faculty_provider.load_json")
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
