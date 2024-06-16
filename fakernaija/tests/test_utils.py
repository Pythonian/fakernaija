"""Unittests for functions in the utils module."""

import unittest
from unittest.mock import MagicMock, mock_open, patch

from fakernaija.providers.name_provider import NameProvider
from fakernaija.utils import load_json, validate_json_structure


class NameProviderLoadJSONFirstNames(unittest.TestCase):
    """Unit tests for loading the JSON data of the NameProvider."""

    @patch("fakernaija.providers.name_provider.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade", "extra": "value"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.required_keys: list[str] = ["tribe", "gender", "name"]
        self.name_provider = NameProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.name_provider.data_path / "first_names.json",
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.name_provider.data_path / 'first_names.json'}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class NameProviderLoadJSONLastNames(unittest.TestCase):
    """Unit tests for loading the JSON data of the NameProvider."""

    @patch("fakernaija.providers.name_provider.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"tribe": "yoruba", "name": "Tinubu"},
            {"tribe": "igbo", "name": "Maduike"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"tribe": "yoruba"},
            {"name": "Maduike"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Tinubu"},
            {"tribe": "igbo", "gender": "female", "name": "Maduike"},
        ]
        self.required_keys: list[str] = ["tribe", "name"]
        self.name_provider = NameProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.name_provider.data_path / "last_names.json",
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.name_provider.data_path / 'last_names.json'}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))
