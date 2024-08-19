"""Unit tests for the DegreeProvider class."""

import unittest
from unittest.mock import Mock, patch

from fakernaija.providers import DegreeProvider


class TestDegreeProvider(unittest.TestCase):
    """Test suite for the DegreeProvider class."""

    @patch("fakernaija.utils.load_json")
    def setUp(self, mock_load_json: Mock) -> None:
        """Sets up the test environment for DegreeProvider tests."""
        mock_load_json.return_value = [
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
            {"name": "Master of Arts", "degree_type": "masters", "abbr": "M.A."},
            {
                "name": "Doctor of Philosophy",
                "degree_type": "doctorate",
                "abbr": "Ph.D.",
            },
        ]
        self.degree_provider = DegreeProvider()

    def test_get_degrees(self) -> None:
        """Tests get_degrees method without any degree_type filter."""
        degrees = self.degree_provider.get_degrees()
        degree = {"name": "Master of Arts", "degree_type": "masters", "abbr": "M.A."}
        self.assertIn(degree, degrees)

    def test_get_degrees_with_type(self) -> None:
        """Tests get_degrees method with a specific degree_type filter."""
        undergraduate_degrees = self.degree_provider.get_degrees("undergraduate")
        for degree in undergraduate_degrees:
            self.assertEqual(degree["degree_type"], "undergraduate")

    def test_get_degree_names(self) -> None:
        """Tests get_degree_names method without any degree_type filter."""
        degree_names = self.degree_provider.get_degree_names()
        expected_names = [
            "Bachelor of Arts",
            "Bachelor of Science",
            "Master of Arts",
            "Doctor of Philosophy",
        ]
        for name in expected_names:
            self.assertIn(name, degree_names)

    def test_get_degree_names_with_type(self) -> None:
        """Tests get_degree_names method with a specific degree_type filter."""
        degree_names = self.degree_provider.get_degree_names("undergraduate")
        expected_names = ["Bachelor of Arts", "Bachelor of Science"]
        for name in expected_names:
            self.assertIn(name, degree_names)

    def test_get_degree_abbrs(self) -> None:
        """Tests get_degree_abbrs method without any degree_type filter."""
        degree_abbrs = self.degree_provider.get_degree_abbrs()
        expected_abbrs = ["B.A.", "B.Sc.", "M.A.", "Ph.D."]
        for abbr in expected_abbrs:
            self.assertIn(abbr, degree_abbrs)

    def test_get_degree_abbrs_with_type(self) -> None:
        """Tests get_degree_abbrs method with a specific degree_type filter."""
        degree_abbrs = self.degree_provider.get_degree_abbrs("undergraduate")
        expected_abbrs = ["B.A.", "B.Sc."]
        for abbr in expected_abbrs:
            self.assertIn(abbr, degree_abbrs)


if __name__ == "__main__":
    unittest.main()
