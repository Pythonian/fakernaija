"""Unit tests for the StateProvider class from the fakernaija package.

This module contains unit tests for the StateProvider class, which provides methods
for accessing and validating information about Nigerian states. The tests ensure
that the methods return the expected results and handle various inputs correctly.
"""

import json
import unittest
from typing import Any
from unittest.mock import mock_open, patch

from fakernaija.providers.states import StateProvider


class TestStateProvider(unittest.TestCase):
    """Test suite for the StateProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment by initializing a StateProvider instance."""
        self.state_provider = StateProvider()

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"states": []}),
    )
    def test_load_json_success(self, mock_file: Any) -> None:  # noqa: ARG002, ANN401
        """Test loading JSON data successfully."""
        data = self.state_provider.load_json(self.state_provider.data_path)
        self.assertIn("states", data)
        self.assertIsInstance(data, dict)

    @patch("pathlib.Path.open", new_callable=mock_open)
    def test_load_json_file_not_found(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test handling of file not found error."""
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            self.state_provider.load_json("none.json")

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            self.state_provider.load_json(self.state_provider.data_path)
        self.assertIn("Error decoding JSON", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"invalid_key": []}),
    )
    def test_load_json_invalid_data_structure(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of invalid data structure."""
        with self.assertRaises(ValueError) as context:
            self.state_provider.load_json(self.state_provider.data_path)
        self.assertIn("Invalid data format", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data=json.dumps({"states": [{"name": "Lagos"}]}),
    )
    def test_load_json_missing_keys_in_state(
        self,
        mock_file: Any,  # noqa: ARG002, ANN401
    ) -> None:
        """Test handling of missing required keys in state data."""
        with self.assertRaises(ValueError) as context:
            self.state_provider.load_json(self.state_provider.data_path)
        self.assertIn("Invalid data format", str(context.exception))

    def test_validate_states_data(self) -> None:
        """Test validation of state data."""
        valid_data = {
            "states": [
                {
                    "code": "FC",
                    "name": "FCT",
                    "capital": "Abuja",
                    "region": "North Central",
                    "region_initial": "NC",
                    "postal_code": "900001",
                    "lgas": ["Abuja", "Kwali", "Kuje", "Gwagwalada", "Bwari", "Abaji"],
                },
            ],
        }
        invalid_data = {
            "states": [
                {
                    "code": "FC",
                    "name": "FCT",
                    "capital": "Abuja",
                    "region": "North Central",
                    "region_initial": "NC",
                },
            ],
        }
        self.assertTrue(self.state_provider.validate_states_data(valid_data))
        self.assertFalse(self.state_provider.validate_states_data(invalid_data))

    def test_validate_state_data(self) -> None:
        """Test validation of individual state data."""
        valid_state = {
            "name": "Lagos",
            "code": "LA",
            "capital": "Ikeja",
            "lgas": ["Agege", "Ajeromi-Ifelodun", "Alimosho", "Amuwo-Odofin"],
            "region": "South West",
            "region_initial": "SW",
            "postal_code": "100001",
        }
        invalid_state = {
            "name": "Lagos",
            "code": "LA",
            "capital": "Ikeja",
            "region": "South West",
            "region_initial": "SW",
            "postal_code": "100001",
        }
        self.assertTrue(self.state_provider.validate_state_data(valid_state))
        self.assertFalse(self.state_provider.validate_state_data(invalid_state))

    def test_get_states(self) -> None:
        """Test getting all state names."""
        states = self.state_provider.get_states()
        self.assertIn("Lagos", states)

    def test_get_shortcodes(self) -> None:
        """Test getting all state shortcodes."""
        shortcodes = self.state_provider.get_shortcodes()
        self.assertIn("LA", shortcodes)

    def test_get_capitals(self) -> None:
        """Test getting all state capitals."""
        capitals = self.state_provider.get_capitals()
        self.assertIn("Ikeja", capitals)

    def test_get_lgas(self) -> None:
        """Test getting all LGAs for all states."""
        lgas = self.state_provider.get_lgas()
        self.assertIn("Apapa", lgas)

    def test_get_regions(self) -> None:
        """Test getting all unique region codes."""
        regions = self.state_provider.get_regions()
        self.assertIn("South West", regions)

    def test_get_postal_codes(self) -> None:
        """Test getting all postal codes of states."""
        postal_codes = self.state_provider.get_postal_codes()
        self.assertIn("100001", postal_codes)

    def test_get_states_by_region(self) -> None:
        """Test getting states by a specific region code."""
        states = self.state_provider.get_states_by_region("SW")
        state_names = [state["name"] for state in states]
        self.assertIn("Lagos", state_names)

    def test_get_state_by_name(self) -> None:
        """Test getting state information by state name."""
        state_info = self.state_provider.get_state_by_name("Lagos")
        assert state_info is not None, "Expected state info to not be None"
        assert state_info["name"] == "Lagos"
        assert state_info["code"] == "LA"
        assert state_info["capital"] == "Ikeja"

    def test_get_state_by_name_not_found(self) -> None:
        """Test getting a state by name when the state does not exist."""
        state = self.state_provider.get_state_by_name("Pythonian")
        self.assertIsNone(state)

    def test_get_postal_code_by_state(self) -> None:
        """Test getting the postal code of a specific state."""
        postal_code = self.state_provider.get_postal_code_by_state("Lagos")
        self.assertEqual(postal_code, "100001")

    def test_get_state_capital(self) -> None:
        """Test getting the capital city of a specific state."""
        capital = self.state_provider.get_state_capital("Lagos")
        self.assertEqual(capital, "Ikeja")

    def test_get_state_lgas(self) -> None:
        """Test getting a list of Local Government Areas for a specific state."""
        lgas = self.state_provider.get_state_lgas("Lagos")
        self.assertIn("Agege", lgas)
