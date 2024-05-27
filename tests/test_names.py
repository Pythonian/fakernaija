"""Unit tests for the NameProvider class.

This module contains unit tests for the NameProvider class, which provides methods
for generating random Nigerian names. The tests ensure that the
methods return the expected names based on tribes and gender.
"""

import json
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import mock_open, patch

from fakernaija.providers.names import NameProvider


class TestNameProvider(unittest.TestCase):
    """Unit tests for the NameProvider class."""

    @classmethod
    def setUpClass(cls) -> None:  # noqa: ANN102
        """Load the JSON data once for all tests."""
        base_path = (
            Path(__file__).parent.parent / "fakernaija" / "providers" / "data" / "names"
        )

        # Load first names data
        first_names_path = base_path / "first_names.json"
        with first_names_path.open(encoding="utf-8") as file:
            cls.first_names_data = json.load(file)

        # Load last names data
        last_names_path = base_path / "last_names.json"
        with last_names_path.open(encoding="utf-8") as file:
            cls.last_names_data = json.load(file)

    def setUp(self) -> None:
        """Set up the NameProvider instance for testing."""
        self.name_provider = NameProvider()
        # self.name_provider.first_names = [
        #     {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        #     {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
        #     {"tribe": "yoruba", "gender": "female", "name": "Adeola"},
        #     {"tribe": "yoruba", "gender": "male", "name": "Tunde"},
        # ]
        # self.name_provider.last_names = [
        #     {"tribe": "yoruba", "name": "Obisesan"},
        #     {"tribe": "igbo", "name": "Maduike"},
        #     {"tribe": "igbo", "name": "Okafor"},
        #     {"tribe": "yoruba", "name": "Adebayo"},
        # ]
        self.valid_first_names = [
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
            {"tribe": "igbo", "gender": "male", "name": "Jidenna"},
        ]
        self.valid_last_names = [
            {"tribe": "yoruba", "name": "Obisesan"},
            {"tribe": "igbo", "name": "Maduike"},
        ]

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Tunde"}]),
    )
    def test_load_json_success(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test loading JSON data successfully."""
        data = self.name_provider.load_json(
            self.name_provider.data_path / "first_names.json",
        )
        expected_data = [{"tribe": "yoruba", "gender": "male", "name": "Tunde"}]
        assert data == expected_data
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch("fakernaija.providers.names.Path.open")
    def test_load_json_file_not_found(self, mock_open: Any) -> None:  # noqa: ANN401
        """Test handling of a missing JSON file."""
        mock_open.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as cm:  # noqa: PT027
            self.name_provider.load_json(self.name_provider.data_path / "none.json")
        assert (
            str(cm.exception)
            == f"File not found: {self.name_provider.data_path / 'none.json'}"
        )

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data="Invalid JSON",
    )
    def test_load_json_invalid_json(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test handling of invalid JSON data."""
        with self.assertRaises(ValueError) as cm:  # noqa: PT027
            self.name_provider.load_json(self.name_provider.data_path / "invalid.json")
        assert "Error decoding JSON from file" in str(cm.exception)
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([]),
    )
    def test_load_json_empty_file(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test loading an empty JSON file."""
        data = self.name_provider.load_json(self.name_provider.data_path / "empty.json")
        assert data == []
        mock_file.assert_called_once_with(encoding="utf-8")

    @patch(
        "fakernaija.providers.names.Path.open",
        new_callable=mock_open,
        read_data=json.dumps([{"tribe": "yoruba", "gender": "male", "name": "Tunde"}]),
    )
    def test_load_json_check_path(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test that the correct file path is used."""
        file_path = self.name_provider.data_path / "first_names.json"
        self.name_provider.load_json(file_path)
        mock_file.assert_called_once_with(encoding="utf-8")

    def test_get_first_names(self) -> None:
        """Test getting the first names."""
        first_names = self.valid_first_names
        assert first_names[0]["name"] == "Ugochi"
        assert first_names[1]["name"] == "Jidenna"

    def test_get_last_names(self) -> None:
        """Test getting the last names."""
        last_names = self.valid_last_names
        assert last_names[0]["name"] == "Obisesan"
        assert last_names[1]["name"] == "Maduike"

    def test_generate_first_name(self) -> None:
        """Test generating a first name."""
        first_name = self.name_provider.generate_first_name(
            tribe="igbo",
            gender="female",
        )
        assert first_name in [
            entry["name"]
            for entry in self.first_names_data
            if entry["tribe"] == "igbo" and entry["gender"] == "female"
        ]

    def test_generate_last_name(self) -> None:
        """Test generating a last name."""
        last_name = self.name_provider.generate_last_name(tribe="yoruba")
        assert last_name in [
            entry["name"]
            for entry in self.last_names_data
            if entry["tribe"] == "yoruba"
        ]

    def test_generate_full_name(self) -> None:
        """Test generating a full name."""
        full_name = self.name_provider.generate_full_name(tribe="igbo", gender="male")
        first_names = [
            entry["name"]
            for entry in self.first_names_data
            if entry["tribe"] == "igbo" and entry["gender"] == "male"
        ]
        last_names = [
            entry["name"] for entry in self.last_names_data if entry["tribe"] == "igbo"
        ]
        first_name, last_name = full_name.split()
        assert first_name in first_names
        assert last_name in last_names


if __name__ == "__main__":
    unittest.main()
