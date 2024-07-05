"""Unittests for the NameProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers.name_provider import NameProvider


class TestNameProvider(unittest.TestCase):
    """Test case for the NameProvider class."""

    @patch("fakernaija.providers.name_provider.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:
        """Set up the test case with mock data."""
        self.mock_first_names = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "yoruba", "gender": "female", "name": "Bisi"},
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.mock_last_names = [
            {"tribe": "yoruba", "name": "Ojo"},
            {"tribe": "igbo", "name": "Maduike"},
        ]

        mock_load_json.side_effect = [self.mock_first_names, self.mock_last_names]
        self.name_provider = NameProvider()

    def test_normalize_input(self) -> None:
        """Test normalization of input values to lowercase."""
        self.assertEqual(self.name_provider.normalize_input("Yoruba"), "yoruba")
        self.assertEqual(self.name_provider.normalize_input("FEMALE"), "female")
        self.assertIsNone(self.name_provider.normalize_input(None))

    def test_get_first_names_no_filters(self) -> None:
        """Test retrieving first names without filters."""
        first_names = self.name_provider.get_first_names()
        self.assertEqual(first_names, self.mock_first_names)

    def test_get_first_names_by_tribe(self) -> None:
        """Test getting first names filtered by tribe."""
        first_names = self.name_provider.get_first_names(tribe="igbo")
        expected = [
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.assertEqual(first_names, expected)

    def test_get_first_names_by_gender(self) -> None:
        """Test getting first names filtered by gender."""
        first_names = self.name_provider.get_first_names(gender="male")
        expected = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
        ]
        self.assertEqual(first_names, expected)

    def test_get_first_names_by_tribe_and_gender(self) -> None:
        """Test retrieving first names with tribe and gender filters."""
        first_names = self.name_provider.get_first_names(tribe="yoruba", gender="male")
        expected = [{"tribe": "yoruba", "gender": "male", "name": "Ade"}]
        self.assertEqual(first_names, expected)

    def test_get_first_names_no_match(self) -> None:
        """Test getting first names with no match found."""
        with self.assertRaises(ValueError) as context:
            self.name_provider.get_first_names(tribe="hausa", gender="male")
        self.assertIn("Unsupported tribe: hausa", str(context.exception))

    def test_get_first_names_invalid_gender(self) -> None:
        """Test getting first names with unsupported gender."""
        with self.assertRaises(ValueError) as context:
            self.name_provider.get_first_names(tribe="igbo", gender="invalid")
        self.assertIn("Unsupported gender: invalid", str(context.exception))

    def test_get_last_names_no_filters(self) -> None:
        """Test retrieving last names without filters."""
        last_names = self.name_provider.get_last_names()
        self.assertEqual(last_names, self.mock_last_names)

    def test_get_last_names_by_tribe(self) -> None:
        """Test getting last names filtered by tribe."""
        last_names = self.name_provider.get_last_names(tribe="igbo")
        expected = [{"tribe": "igbo", "name": "Maduike"}]
        self.assertEqual(last_names, expected)

    def test_get_last_names_no_match(self) -> None:
        """Test getting last names with no match found."""
        with self.assertRaises(ValueError) as context:
            self.name_provider.get_last_names(tribe="hausa")
        self.assertIn("Unsupported tribe: hausa", str(context.exception))

    def test_generate_full_name_invalid_gender(self) -> None:
        """Test generating full names with unsupported gender."""
        with self.assertRaises(ValueError) as context:
            self.name_provider.generate_full_name(tribe="igbo", gender="invalid")
        self.assertIn("Unsupported gender: invalid", str(context.exception))

    @patch(
        "random.choice",
        return_value={"tribe": "igbo", "gender": "female", "name": "Ugochi"},
    )
    def test_generate_first_name(self, mock_choice: MagicMock) -> None:  # noqa: ARG002
        """Test generating a random first name with filters."""
        first_name = self.name_provider.generate_first_name(
            tribe="igbo",
            gender="female",
        )
        self.assertEqual(first_name, "Ugochi")

    @patch("random.choice", return_value={"tribe": "igbo", "name": "Maduike"})
    def test_generate_last_name(self, mock_choice: MagicMock) -> None:  # noqa: ARG002
        """Test generating a random last name with tribe filter."""
        last_name = self.name_provider.generate_last_name(tribe="igbo")
        self.assertEqual(last_name, "Maduike")

    @patch(
        "random.choice",
        side_effect=[
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
            {"tribe": "igbo", "name": "Maduike"},
        ],
    )
    def test_generate_full_name_no_middle(
        self,
        mock_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generating a full name without middle name."""
        full_name = self.name_provider.generate_full_name(
            tribe="igbo",
            gender="female",
        )
        self.assertEqual(full_name, "Ugochi Maduike")

    @patch(
        "random.choice",
        side_effect=[
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},  # First name
            {"tribe": "yoruba", "name": "Ojo"},  # Last name
            {"tribe": "yoruba", "gender": "male", "name": "Bisi"},  # Middle name
        ],
    )
    def test_generate_full_name_with_middle(
        self,
        mock_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generating a full name with middle name."""
        result = self.name_provider.generate_full_name(
            tribe="yoruba",
            gender="male",
            middle_name=True,
        )
        self.assertEqual(result, "Ade Bisi Ojo")
