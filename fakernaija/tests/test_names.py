"""Unit tests for the NameProvider class.

This module contains unit tests for the NameProvider class, which provides methods
for generating random Nigerian names. The tests ensure that the
methods return the expected names based on tribes and gender.
"""

import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

from fakernaija.providers.names import NameProvider


class TestLoadJson(unittest.TestCase):
    """Unit tests for the NameProvider load_json method."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.name_provider = NameProvider()

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]),
    )
    def test_load_json_success(self, mock_file: MagicMock) -> None:
        """Test loading JSON data successfully."""
        data = self.name_provider.load_json(
            self.name_provider.data_path / "first_names.json",
            ["tribe", "gender", "name"],
        )
        expected_data = [{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]
        self.assertEqual(data, expected_data)
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch("fakernaija.providers.names.Path.open")
    def test_load_json_file_not_found(self, mock_open: MagicMock) -> None:
        """Test handling of a missing JSON file."""
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as cm:
            self.name_provider.load_json(
                self.name_provider.data_path / "none.json",
                ["tribe", "gender", "name"],
            )
        self.assertEqual(
            str(cm.exception),
            f"File not found: {self.name_provider.data_path / 'none.json'}",
        )

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data="Invalid JSON",
    )
    def test_load_json_invalid_json(self, mock_file: MagicMock) -> None:
        """Test handling of invalid JSON data."""
        with self.assertRaises(ValueError) as cm:
            self.name_provider.load_json(
                self.name_provider.data_path / "invalid.json",
                ["tribe", "gender", "name"],
            )
        self.assertIn("Error decoding JSON from file", str(cm.exception))
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([]),
    )
    def test_load_json_empty_file(self, mock_file: MagicMock) -> None:
        """Test loading an empty JSON file."""
        data = self.name_provider.load_json(
            self.name_provider.data_path / "empty.json",
            ["tribe", "gender", "name"],
        )
        self.assertEqual(data, [])
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]),
    )
    def test_load_json_check_path(self, mock_file: MagicMock) -> None:
        """Test that the correct file path is used."""
        file_path = self.name_provider.data_path / "first_names.json"
        self.name_provider.load_json(file_path, ["tribe", "gender", "name"])
        mock_file.assert_called_once_with(encoding="utf-8")


class TestValidateJsonStructure(unittest.TestCase):
    """Unit tests for the NameProvider validate_json_structure method."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.name_provider = NameProvider()

    def test_validate_json_structure_success(self) -> None:
        """Test successful validation of JSON structure."""
        data = [{"tribe": "yoruba", "gender": "male", "name": "Seyi"}]
        try:
            self.name_provider.validate_json_structure(
                data,
                ["tribe", "gender", "name"],
            )
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validation of JSON structure with missing keys."""
        data = [{"tribe": "yoruba", "name": "Seyi"}]
        with self.assertRaises(ValueError) as cm:
            self.name_provider.validate_json_structure(
                data,
                ["tribe", "gender", "name"],
            )
        self.assertIn("Missing keys {'gender'} in entry", str(cm.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validation of JSON structure with extra keys."""
        data = [{"tribe": "yoruba", "gender": "male", "name": "Seyi", "extra": "value"}]
        with self.assertRaises(ValueError) as cm:
            self.name_provider.validate_json_structure(
                data,
                ["tribe", "gender", "name"],
            )
        self.assertIn("Invalid keys {'extra'} in entry", str(cm.exception))


class TestNameProvider(unittest.TestCase):
    """Unit tests for the NameProvider class."""

    def setUp(self) -> None:
        """Set up the NameProvider instance for testing."""
        self.mock_first_names = [
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
            {"tribe": "yoruba", "gender": "female", "name": "Adeola"},
            {"tribe": "yoruba", "gender": "male", "name": "Seyi"},
        ]
        self.mock_last_names = [
            {"tribe": "yoruba", "name": "Obisesan"},
            {"tribe": "igbo", "name": "Maduike"},
            {"tribe": "igbo", "name": "Okafor"},
            {"tribe": "yoruba", "name": "Adebayo"},
        ]
        self.patcher = patch.object(
            NameProvider,
            "load_json",
            side_effect=[self.mock_first_names, self.mock_last_names],
        )
        self.mock_load_json = self.patcher.start()
        self.name_provider = NameProvider()

    def tearDown(self) -> None:
        """Stop the patcher."""
        self.patcher.stop()

    def test_get_first_names_no_filters(self) -> None:
        """Test getting all first names without any filters."""
        first_names = self.name_provider.get_first_names()
        expected_names = self.mock_first_names
        self.assertEqual(first_names, expected_names)

    def test_get_first_names_by_tribe(self) -> None:
        """Test getting first names filtered by tribe."""
        first_names = self.name_provider.get_first_names(tribe="igbo")
        expected_names = [
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
        ]
        self.assertEqual(first_names, expected_names)

    def test_get_first_names_by_gender(self) -> None:
        """Test getting first names filtered by gender."""
        first_names = self.name_provider.get_first_names(gender="female")
        expected_names = [
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
            {"tribe": "yoruba", "gender": "female", "name": "Adeola"},
        ]
        self.assertEqual(first_names, expected_names)

    def test_get_first_names_by_tribe_and_gender(self) -> None:
        """Test getting first names filtered by tribe and gender."""
        first_names = self.name_provider.get_first_names(tribe="igbo", gender="female")
        expected_names = [{"tribe": "igbo", "gender": "female", "name": "Ugochi"}]
        self.assertEqual(first_names, expected_names)

    def test_get_first_names_no_match(self) -> None:
        """Test getting first names with no match found."""
        first_names = self.name_provider.get_first_names(tribe="hausa", gender="male")
        self.assertEqual(first_names, [])

    def test_get_last_names_no_filters(self) -> None:
        """Test getting all last names without any filters."""
        last_names = self.name_provider.get_last_names()
        expected_names = self.mock_last_names
        self.assertEqual(last_names, expected_names)

    def test_get_last_names_by_tribe(self) -> None:
        """Test getting last names filtered by tribe."""
        last_names = self.name_provider.get_last_names(tribe="igbo")
        expected_names = [
            {"tribe": "igbo", "name": "Maduike"},
            {"tribe": "igbo", "name": "Okafor"},
        ]
        self.assertEqual(last_names, expected_names)

    def test_get_last_names_no_match(self) -> None:
        """Test getting last names with no match found."""
        last_names = self.name_provider.get_last_names(tribe="hausa")
        self.assertEqual(last_names, [])

    @patch("random.choice", side_effect=lambda x: x[0])
    def test_generate_first_name(
        self,
        mock_random_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generating a random first name."""
        first_name = self.name_provider.generate_first_name(
            tribe="igbo",
            gender="female",
        )
        self.assertEqual(first_name, "Ugochi")

    @patch("random.choice", side_effect=lambda x: x[0])
    def test_generate_last_name(
        self,
        mock_random_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generating a random last name."""
        last_name = self.name_provider.generate_last_name(tribe="igbo")
        self.assertEqual(last_name, "Maduike")

    @patch("random.choice", side_effect=lambda x: x[0])
    def test_generate_full_name(
        self,
        mock_random_choice: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test generating a random full name."""
        full_name = self.name_provider.generate_full_name(
            tribe="igbo",
            gender="female",
        )
        self.assertEqual(full_name, "Ugochi Maduike")
