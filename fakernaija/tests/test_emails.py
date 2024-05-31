"""Unit tests for the EmailProvider class.

This module contains unit tests for the EmailProvider class, which provides methods
for generating random email address with Nigerian names. The tests ensure that the
methods return the expected names based on tribes.
"""

import json
import unittest
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from fakernaija.providers.emails import EmailProvider


class TestLoadJson(unittest.TestCase):
    """Unit tests for the EmailProvider load_json method."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]),
    )
    def test_load_json_success(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test loading JSON data successfully."""
        data = self.email_provider.load_json(
            self.email_provider.data_path / "first_names.json",
        )
        expected_data = [{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]
        self.assertEqual(data, expected_data)
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch("fakernaija.providers.names.Path.open")
    def test_load_json_file_not_found(self, mock_open: Any) -> None:  # noqa: ANN401
        """Test handling of a missing JSON file."""
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as cm:
            self.email_provider.load_json(self.email_provider.data_path / "none.json")
        self.assertEqual(
            str(cm.exception),
            f"File not found: {self.email_provider.data_path / 'none.json'}",
        )

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data="Invalid JSON",
    )
    def test_load_json_invalid_json(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test handling of invalid JSON data."""
        with self.assertRaises(ValueError) as cm:
            self.email_provider.load_json(
                self.email_provider.data_path / "invalid.json",
            )
        self.assertIn("Error decoding JSON from file", str(cm.exception))
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([]),
    )
    def test_load_json_empty_file(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test loading an empty JSON file."""
        data = self.email_provider.load_json(
            self.email_provider.data_path / "empty.json",
        )
        self.assertEqual(data, [])
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]),
    )
    def test_load_json_check_path(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test that the correct file path is used."""
        file_path = self.email_provider.data_path / "first_names.json"
        self.email_provider.load_json(file_path)
        mock_file.assert_called_once_with(encoding="utf-8")


class TestGetFirstNames(unittest.TestCase):
    """Unit tests for the EmailProvider get_first_names method."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()

    @patch(
        "fakernaija.providers.emails.EmailProvider.load_json",
        return_value=[{"tribe": "yoruba", "gender": "male", "name": "Seyi"}],
    )
    def test_get_first_names_empty_list(
        self,
        mock_load_json: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test get_first_names with an empty first_names list."""
        email_provider = EmailProvider()
        names = email_provider.get_first_names()
        self.assertEqual(len(names), 1)
        self.assertEqual(names[0]["name"], "Seyi")
        self.assertEqual(names[0]["tribe"], "yoruba")
        self.assertEqual(names[0]["gender"], "male")

    def test_get_first_names_no_filter(self) -> None:
        """Test get_first_names with no filters applied."""
        with patch.object(
            self.email_provider,
            "first_names",
            [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
                {"tribe": "igbo", "gender": "female", "name": "Ada"},
            ],
        ):
            result = self.email_provider.get_first_names()
            expected = [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
                {"tribe": "igbo", "gender": "female", "name": "Ada"},
            ]
            self.assertEqual(result, expected)

    def test_get_first_names_with_tribe_filter(self) -> None:
        """Test get_first_names with only tribe filter applied."""
        with patch.object(
            self.email_provider,
            "first_names",
            [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
                {"tribe": "igbo", "gender": "female", "name": "Ada"},
            ],
        ):
            result = self.email_provider.get_first_names(tribe="yoruba")
            expected = [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
            ]
            self.assertEqual(result, expected)

    def test_get_first_names_with_gender_filter(self) -> None:
        """Test get_first_names with only gender filter applied."""
        with patch.object(
            self.email_provider,
            "first_names",
            [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
                {"tribe": "igbo", "gender": "female", "name": "Ada"},
            ],
        ):
            result = self.email_provider.get_first_names(gender="male")
            expected = [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
            ]
            self.assertEqual(result, expected)

    def test_get_first_names_with_tribe_and_gender_filter(self) -> None:
        """Test get_first_names with both tribe and gender filters applied."""
        with patch.object(
            self.email_provider,
            "first_names",
            [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
                {"tribe": "yoruba", "gender": "female", "name": "Funke"},
                {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
                {"tribe": "igbo", "gender": "female", "name": "Ada"},
            ],
        ):
            result = self.email_provider.get_first_names(tribe="yoruba", gender="male")
            expected = [
                {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
            ]
            self.assertEqual(result, expected)

    def test_get_last_names_no_filter(self) -> None:
        """Test get_last_names with no filters applied."""
        with patch.object(
            self.email_provider,
            "last_names",
            [
                {"tribe": "yoruba", "name": "Afolabi"},
                {"tribe": "igbo", "name": "Maduike"},
            ],
        ):
            result = self.email_provider.get_last_names()
            expected = [
                {"tribe": "yoruba", "name": "Afolabi"},
                {"tribe": "igbo", "name": "Maduike"},
            ]
            self.assertEqual(result, expected)

    def test_get_last_names_with_tribe_filter(self) -> None:
        """Test get_last_names with only tribe filter applied."""
        with patch.object(
            self.email_provider,
            "last_names",
            [
                {"tribe": "yoruba", "name": "Afolabi"},
                {"tribe": "igbo", "name": "Maduike"},
            ],
        ):
            result = self.email_provider.get_last_names(tribe="yoruba")
            expected = [
                {"tribe": "yoruba", "name": "Afolabi"},
            ]
            self.assertEqual(result, expected)


class TestGetNamesByTribe(unittest.TestCase):
    """Unit tests for the get_names_by_tribe method in EmailProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()
        self.email_provider.first_names = [
            {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
            {"tribe": "yoruba", "gender": "female", "name": "Funke"},
            {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
            {"tribe": "igbo", "gender": "female", "name": "Ada"},
        ]
        self.email_provider.last_names = [
            {"tribe": "yoruba", "name": "Ade"},
            {"tribe": "yoruba", "name": "Ola"},
            {"tribe": "igbo", "name": "Okoro"},
            {"tribe": "igbo", "name": "Nwosu"},
        ]

    def test_get_names_by_tribe_empty_lists(self) -> None:
        """Test get_names_by_tribe with empty first_names and last_names lists."""
        self.email_provider.first_names = []
        self.email_provider.last_names = []

        result = self.email_provider.get_names_by_tribe("yoruba")
        self.assertEqual(result, ([], []))

    def test_get_names_by_tribe_no_gender(self) -> None:
        """Test get_names_by_tribe with only tribe filter applied."""
        result = self.email_provider.get_names_by_tribe("yoruba")
        self.assertEqual(result, (["Seyi", "Funke"], ["Ade", "Ola"]))

    def test_get_names_by_tribe_no_match(self) -> None:
        """Test get_names_by_tribe with no matching tribe."""
        result = self.email_provider.get_names_by_tribe("nonexistent_tribe")
        self.assertEqual(result, ([], []))

    def test_get_names_by_tribe_with_gender(self) -> None:
        """Test get_names_by_tribe with both tribe and gender filters applied."""
        result = self.email_provider.get_names_by_tribe("yoruba", "male")
        self.assertEqual(result, (["Seyi"], ["Ade", "Ola"]))


class TestGenerateEmail(unittest.TestCase):
    """Unit tests for the generate_email method in EmailProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()
        self.email_provider.first_names = [
            {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
            {"tribe": "yoruba", "gender": "female", "name": "Funke"},
            {"tribe": "igbo", "gender": "male", "name": "Chinedu"},
            {"tribe": "igbo", "gender": "female", "name": "Ada"},
        ]
        self.email_provider.last_names = [
            {"tribe": "yoruba", "name": "Ade"},
            {"tribe": "yoruba", "name": "Ola"},
            {"tribe": "igbo", "name": "Okoro"},
            {"tribe": "igbo", "name": "Nwosu"},
        ]

    @patch("random.choice")
    def test_generate_email_no_matching_data(
        self,
        mock_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generate_email with no matching data."""
        result = self.email_provider.generate_email(tribe="nonexistent_tribe")
        self.assertIsNone(result)

    @patch("random.choice")
    @patch("random.random")
    def test_generate_email_with_random_suffix(
        self,
        mock_random: MagicMock,
        mock_choice: MagicMock,
    ) -> None:
        """Test generate_email with random number suffix for uniqueness."""
        mock_choice.side_effect = ["Seyi", "Ade", "seyi.ade", "gmail.com"]
        mock_random.side_effect = [0.3, 0.7]  # First call ensures suffix addition
        with patch("random.randint", return_value=123):
            result = self.email_provider.generate_email(tribe="yoruba")
            if result is not None:
                self.assertTrue(result.startswith("seyi.ade123@gmail.com"))
            else:
                self.fail("Generated email is None")

    def test_generate_email_empty_first_names(self) -> None:
        """Test generate_email with empty first_names list."""
        self.email_provider.first_names = []
        result = self.email_provider.generate_email(tribe="yoruba")
        self.assertIsNone(result)

    def test_generate_email_empty_last_names(self) -> None:
        """Test generate_email with empty last_names list."""
        self.email_provider.last_names = []
        result = self.email_provider.generate_email(tribe="yoruba")
        self.assertIsNone(result)

    @patch("random.choice")
    @patch.object(EmailProvider, "get_names_by_tribe")
    def test_generate_email_no_tribe(
        self,
        mock_get_names_by_tribe: MagicMock,
        mock_random_choice: MagicMock,
    ) -> None:
        """Test for when no tribe is specified, and a random tribe has to be chosen."""
        # Mock the randomness
        mock_random_choice.side_effect = [
            "Yoruba",  # Chosen tribe
            "Seyi",  # Chosen first name
            "Ade",  # Chosen last name
            "seyi.ade",  # Chosen format
            "test.com",  # Chosen domain
            0.6,  # Random number to not add a suffix
        ]

        # Mock get_names_by_tribe to return names for the chosen tribe
        mock_get_names_by_tribe.return_value = (
            ["Seyi", "Funke"],  # First names for Yoruba
            ["Ade"],  # Last names for Yoruba
        )

        # Ensure the random number is controlled to avoid adding a numeric suffix
        with patch("random.random", return_value=0.6):
            email = self.email_provider.generate_email()

        self.assertIsNotNone(email)
        if email is not None:  # This check ensures email is a str for type checkers
            self.assertTrue(email.endswith("@test.com"))
            self.assertTrue(email.startswith("seyi.ade"))
