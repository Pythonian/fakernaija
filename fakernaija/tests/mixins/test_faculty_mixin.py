"""Unit tests for the Faculty mixin methods.

This module contains unit tests for the Faculty class, which provides methods
to interact with the FacultyProvider class for generating faculty information.
"""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.mixins.faculty_mixin import Faculty


class TestFaculty(unittest.TestCase):
    """Test suite for the Faculty class."""

    @patch("fakernaija.providers.faculty_provider.FacultyProvider")
    def setUp(self, mock_faculty_provider: MagicMock) -> None:
        """Setup to mock the FacultyProvider."""
        self.mock_faculty_provider = mock_faculty_provider.return_value
        self.mock_faculty_provider.faculties_data = [
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
        self.mock_faculty_provider.get_faculties.return_value = [
            "Basic Medical Sciences",
            "Communications and Media Studies",
        ]
        self.mock_faculty_provider.get_departments.return_value = [
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
        self.faculty_mixin = Faculty()

    @patch("random.choice")
    def test_faculty(self, mock_choice: MagicMock) -> None:
        """Test the faculty method."""
        mock_choice.side_effect = [
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
        faculty = self.faculty_mixin.faculty()
        self.assertIn("faculty_name", faculty)
        self.assertIn("departments", faculty)
        self.assertIn(
            faculty["faculty_name"],
            ["Basic Medical Sciences", "Communications and Media Studies"],
        )
        self.assertIsInstance(faculty["departments"], list)

    @patch("random.choice")
    def test_faculty_name(self, mock_choice: MagicMock) -> None:
        """Test the faculty_name method."""
        mock_choice.return_value = "Basic Medical Sciences"
        faculty_name = self.faculty_mixin.faculty_name()
        self.assertIn(
            faculty_name,
            ["Basic Medical Sciences", "Communications and Media Studies"],
        )

    @patch("random.choice")
    def test_department(self, mock_choice: MagicMock) -> None:
        """Test the department method."""
        mock_choice.return_value = "Human Anatomy"
        department = self.faculty_mixin.department()
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
        self.assertIn(department, expected_departments)

    @patch("random.choice")
    def test_department_by_faculty(self, mock_choice: MagicMock) -> None:
        """Test the department_by_faculty method."""
        mock_choice.side_effect = ["Human Anatomy", "Strategic Communications"]

        department = self.faculty_mixin.department_by_faculty("Basic Medical Sciences")
        self.assertIn(department, ["Human Anatomy", "Physiology"])

        department = self.faculty_mixin.department_by_faculty(
            "Communications and Media Studies",
        )
        self.assertIn(
            department,
            [
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
        )

        with self.assertRaises(ValueError):
            self.faculty_mixin.department_by_faculty("Nonexistent Faculty")
