"""Unit tests for the NameProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers import NameProvider


class TestNameProvider(unittest.TestCase):
    """Test suite for the NameProvider class."""

    @patch("fakernaija.providers.name.load_json")
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
            self.name_provider.get_first_names(tribe="pythonian", gender="male")
        self.assertIn("Unsupported tribe: pythonian", str(context.exception))

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
            self.name_provider.get_last_names(tribe="pythonian")
        self.assertIn("Unsupported tribe: pythonian", str(context.exception))

    def test_generate_full_name_invalid_gender(self) -> None:
        """Test generating full names with unsupported gender."""
        with self.assertRaises(ValueError) as context:
            self.name_provider.generate_full_name(tribe="igbo", gender="invalid")
        self.assertIn("Unsupported gender: invalid", str(context.exception))

    @patch(
        "random.choice",
        return_value={"tribe": "igbo", "gender": "female", "name": "Ugochi"},
    )
    def test_generate_first_name_with_filters(self, mock_choice: MagicMock) -> None:  # noqa: ARG002
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

    @patch("fakernaija.providers.name.load_json")
    def test_generate_first_name_unsupported_tribe(
        self,
        mock_load_json: MagicMock,
    ) -> None:
        """Test that a ValueError is raised for an unsupported tribe."""
        mock_load_json.return_value = self.mock_first_names
        provider = NameProvider()
        with self.assertRaises(ValueError):
            provider.generate_first_name(tribe="unsupported_tribe")

    @patch("fakernaija.providers.name.load_json")
    def test_generate_first_name_unsupported_gender(
        self,
        mock_load_json: MagicMock,
    ) -> None:
        """Test that a ValueError is raised for an unsupported gender."""
        mock_load_json.return_value = self.mock_first_names
        provider = NameProvider()
        with self.assertRaises(ValueError):
            provider.generate_first_name(gender="unsupported_gender")

    @patch("fakernaija.providers.name.load_json")
    def test_generate_last_name_unsupported_tribe(
        self,
        mock_load_json: MagicMock,
    ) -> None:
        """Test that a ValueError is raised for an unsupported tribe."""
        mock_load_json.return_value = self.mock_last_names
        provider = NameProvider()
        with self.assertRaises(ValueError):
            provider.generate_last_name(tribe="unsupported_tribe")

    def test_generate_full_name_with_filters(self) -> None:
        """Test generating a random full name with filters."""
        full_name = self.name_provider.generate_full_name(tribe="igbo", gender="female")
        self.assertTrue("Ugochi" in full_name)

    def test_generate_prefixes_professional(self) -> None:
        """Test generating professional prefixes."""
        prefixes = self.name_provider.generate_prefixes("professional", None)
        self.assertIn("Dr.", prefixes)

    def test_generate_prefixes_traditional(self) -> None:
        """Test generating traditional prefixes."""
        prefixes = self.name_provider.generate_prefixes("traditional", "male")
        self.assertIn("Oba", prefixes)

    def test_generate_prefixes_general(self) -> None:
        """Test generating general prefixes."""
        prefixes = self.name_provider.generate_prefixes(None, "female")
        self.assertIn("Mrs.", prefixes)

    def test_generate_prefixes_general_no_gender(self) -> None:
        """Test generating general prefixes without gender."""
        prefixes = self.name_provider.generate_prefixes(None, None)
        self.assertIn("Mr.", prefixes)
        self.assertIn("Mrs.", prefixes)

    def test_get_traditional_prefixes_male(self) -> None:
        """Test getting traditional prefixes for male."""
        prefixes = self.name_provider.get_traditional_prefixes("male")
        self.assertIn("Oba", prefixes)
        self.assertNotIn("Erelu", prefixes)

    def test_get_traditional_prefixes_female(self) -> None:
        """Test getting traditional prefixes for female."""
        prefixes = self.name_provider.get_traditional_prefixes("female")
        self.assertIn("Erelu", prefixes)
        self.assertNotIn("Oba", prefixes)

    def test_get_traditional_prefixes_no_gender(self) -> None:
        """Test getting traditional prefixes without specifying gender."""
        prefixes = self.name_provider.get_traditional_prefixes(None)
        self.assertIn("Oba", prefixes)
        self.assertIn("Erelu", prefixes)

    def test_get_general_prefixes_male(self) -> None:
        """Test getting general prefixes for male."""
        prefixes = self.name_provider.get_general_prefixes("male")
        self.assertIn("Mr.", prefixes)
        self.assertNotIn("Mrs.", prefixes)

    def test_get_general_prefixes_female(self) -> None:
        """Test getting general prefixes for female."""
        prefixes = self.name_provider.get_general_prefixes("female")
        self.assertIn("Mrs.", prefixes)
        self.assertNotIn("Mr.", prefixes)

    def test_get_general_prefixes_no_gender(self) -> None:
        """Test getting general prefixes without specifying gender."""
        prefixes = self.name_provider.get_general_prefixes(None)
        self.assertIn("Mr.", prefixes)
        self.assertIn("Mrs.", prefixes)
