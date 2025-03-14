"""Unit tests for the SchoolProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers import SchoolProvider


class TestSchoolProvider(unittest.TestCase):
    """Test suite for the SchoolProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.sample_schools = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "state": "Lagos",
                "type": "university",
                "ownership": "Federal",
            },
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "state": "Lagos",
                "type": "university",
                "ownership": "State",
            },
            {
                "name": "Yaba College of Technology",
                "acronym": "YABATECH",
                "state": "Lagos",
                "type": "polytechnic",
                "ownership": "Federal",
            },
            {
                "name": "Ahmadu Bello University",
                "acronym": "ABU",
                "state": "Kaduna",
                "type": "university",
                "ownership": "Federal",
            },
        ]

    @patch("fakernaija.providers.school.load_json")
    def test_initialization(self, mock_load_json: MagicMock) -> None:
        """Test the initialization of SchoolProvider."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        self.assertEqual(provider.schools_data, self.sample_schools)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_no_filters(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with no filters."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools()
        self.assertEqual(result, self.sample_schools)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_ownership_filter(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with an ownership filter."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools(ownership="federal")
        expected = [
            self.sample_schools[0],  # UNILAG
            self.sample_schools[2],  # YABATECH
            self.sample_schools[3],  # ABU
        ]
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_state_filter(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with a state filter."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools(state="lagos")
        expected = [
            self.sample_schools[0],  # UNILAG
            self.sample_schools[1],  # LASU
            self.sample_schools[2],  # YABATECH
        ]
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_school_type_filter(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with a school type filter."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools(school_type="polytechnic")
        expected = [self.sample_schools[2]]  # YABATECH
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_combined_filters(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with combined filters."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools(
            ownership="federal",
            state="lagos",
            school_type="university",
        )
        expected = [self.sample_schools[0]]  # UNILAG
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_schools_no_matches(self, mock_load_json: MagicMock) -> None:
        """Test get_schools with filters that result in no matches."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_schools(ownership="private")
        self.assertEqual(result, [])

    @patch("fakernaija.providers.school.load_json")
    def test_get_school_names_no_filters(self, mock_load_json: MagicMock) -> None:
        """Test get_school_names with no filters."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_school_names()
        expected = [school["name"] for school in self.sample_schools]
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    @patch("fakernaija.providers.school.StateProvider")
    def test_invalid_state_with_suggestions(
        self, mock_state_provider_class: MagicMock, mock_load_json: MagicMock
    ) -> None:
        """Test raising suggestions for invalid state name."""
        mock_load_json.return_value = self.sample_schools

        # Patch the StateProvider to return a fixed list of states.
        mock_state_provider_instance = mock_state_provider_class.return_value
        mock_state_provider_instance.get_state_names.return_value = ["Lagos", "Kaduna"]

        provider = SchoolProvider()

        # Use a misspelled state name that should trigger suggestions.
        with self.assertRaises(ValueError) as context:
            provider.get_schools(state="lagoss")  # Note the extra "s"

        error_message = str(context.exception)
        self.assertIn("Did you mean:", error_message)
        self.assertIn("Lagos", error_message)

    @patch("fakernaija.providers.school.load_json")
    def test_get_school_names_with_acronym(self, mock_load_json: MagicMock) -> None:
        """Test get_school_names with acronym option."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_school_names(acronym=True)
        expected = [school["acronym"] for school in self.sample_schools]
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_school_names_with_filters(self, mock_load_json: MagicMock) -> None:
        """Test get_school_names with filters."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_school_names(state="lagos", school_type="university")
        expected = [
            self.sample_schools[0]["name"],  # UNILAG
            self.sample_schools[1]["name"],  # LASU
        ]
        self.assertEqual(result, expected)

    @patch("fakernaija.providers.school.load_json")
    def test_get_school_names_no_matches(self, mock_load_json: MagicMock) -> None:
        """Test get_school_names with filters that result in no matches."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        result = provider.get_school_names(state="benue")
        self.assertEqual(result, [])

    @patch("fakernaija.providers.school.load_json")
    def test_invalid_state_name(self, mock_load_json: MagicMock) -> None:
        """Test that a ValueError is raised for an invalid state name."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        with self.assertRaises(ValueError):
            provider.get_schools(state="invalid_state")

    @patch("fakernaija.providers.school.load_json")
    def test_invalid_ownership(self, mock_load_json: MagicMock) -> None:
        """Test that a ValueError is raised for an unsupported ownership."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        with self.assertRaises(ValueError):
            provider.get_schools(ownership="unsupported_ownership")

    @patch("fakernaija.providers.school.load_json")
    def test_invalid_school_type(self, mock_load_json: MagicMock) -> None:
        """Test that a ValueError is raised for an unsupported school type."""
        mock_load_json.return_value = self.sample_schools
        provider = SchoolProvider()
        with self.assertRaises(ValueError):
            provider.get_schools(school_type="unsupported_type")
