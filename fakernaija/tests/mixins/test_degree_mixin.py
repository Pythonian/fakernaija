"""Unit tests for the Degree mixin methods from the DegreeProvider.

This module contains a set of unit tests to verify the behavior of the Degree mixin methods from the DegreeProvider.
The tests ensure that the methods return valid degree names and abbr as expected.
"""

import unittest
from unittest.mock import Mock, patch

from fakernaija.mixins import Degree


class TestDegree(unittest.TestCase):
    """Unit tests for the Degree methods from the Degree mixins."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.degree = Degree()

    @patch("fakernaija.providers.degree_provider.DegreeProvider.get_degrees")
    def test_degree(self, mock_get_degrees: Mock) -> None:
        """Mocks the get_degrees method and checks if the returned degree is in the mocked return value."""
        mock_get_degrees.return_value = [
            {
                "name": "Bachelor of Arts",
                "degree_type": "undergraduate",
                "abbr": "B.A.",
            },
            {
                "name": "Bachelor of Science",
                "degree_type": "undergraduate",
                "abbr": "B.Sc.",
            },
        ]
        result = self.degree.degree()
        self.assertIn(result, mock_get_degrees.return_value)

    @patch("fakernaija.providers.degree_provider.DegreeProvider.get_degree_names")
    def test_degree_name(self, mock_get_degree_names: Mock) -> None:
        """Test degree_name method returns a degree name."""
        mock_get_degree_names.return_value = ["Bachelor of Arts", "Bachelor of Science"]
        result = self.degree.degree_name()
        self.assertIn(result, mock_get_degree_names.return_value)

    @patch("fakernaija.providers.degree_provider.DegreeProvider.get_degree_abbrs")
    def test_degree_abbr(self, mock_get_degree_abbrs: Mock) -> None:
        """Test degree_abbr method returns a degree abbreviation."""
        mock_get_degree_abbrs.return_value = ["B.A.", "B.Sc."]
        result = self.degree.degree_abbr()
        self.assertIn(result, mock_get_degree_abbrs.return_value)

    @patch("fakernaija.providers.degree_provider.DegreeProvider.get_degree_names")
    def test_degree_name_by_type(self, mock_get_degree_names: Mock) -> None:
        """Test that degree_name_by_type returns valid degree names based on that degree type."""
        mock_get_degree_names.return_value = ["Bachelor of Arts", "Bachelor of Science"]
        result = self.degree.degree_name_by_type("undergraduate")
        self.assertIn(result, mock_get_degree_names.return_value)

    def test_degree_name_by_type_invalid(self) -> None:
        """Test that degree_name_by_type raises ValueError if passed an invalid degree type."""
        with self.assertRaises(ValueError):
            self.degree.degree_name_by_type("invalid_type")

    @patch("fakernaija.providers.degree_provider.DegreeProvider.get_degree_abbrs")
    def test_degree_abbr_by_type(self, mock_get_degree_abbrs: Mock) -> None:
        """Test that degree_abbr_by_type returns valid degree abbreviations based on that degree type."""
        mock_get_degree_abbrs.return_value = ["B.A.", "B.Sc."]
        result = self.degree.degree_abbr_by_type("undergraduate")
        self.assertIn(result, mock_get_degree_abbrs.return_value)

    def test_degree_abbr_by_type_invalid(self) -> None:
        """Test that degree_abbr_by_type raises ValueError if passed an invalid degree type."""
        with self.assertRaises(ValueError):
            self.degree.degree_abbr_by_type("invalid_type")
