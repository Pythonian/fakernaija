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
        assert "states" in data
        assert isinstance(data, dict)

    @patch("pathlib.Path.open", new_callable=mock_open)
    def test_load_json_file_not_found(self, mock_file: Any) -> None:  # noqa: ANN401
        """Test handling of file not found error."""
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):  # noqa: PT027
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
        with self.assertRaises(ValueError) as context:  # noqa: PT027
            self.state_provider.load_json(self.state_provider.data_path)
        assert "Error decoding JSON" in str(context.exception)

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
        with self.assertRaises(ValueError) as context:  # noqa: PT027
            self.state_provider.load_json(self.state_provider.data_path)
        assert "Invalid data format" in str(context.exception)

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
        with self.assertRaises(ValueError) as context:  # noqa: PT027
            self.state_provider.load_json(self.state_provider.data_path)
        assert "Invalid data format" in str(context.exception)

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
        assert self.state_provider.validate_states_data(valid_data) is True
        assert self.state_provider.validate_states_data(invalid_data) is False

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
        assert self.state_provider.validate_state_data(valid_state) is True
        assert self.state_provider.validate_state_data(invalid_state) is False

    def test_get_states(self) -> None:
        """Test getting all state names."""
        states = self.state_provider.get_states()
        # Check that a state exists in the list of state names
        assert "Lagos" in states

    def test_get_shortcodes(self) -> None:
        """Test getting all state shortcodes."""
        shortcodes = self.state_provider.get_shortcodes()
        # Check that a shortcode exists in the list of shortcodes
        assert "LA" in shortcodes

    def test_get_capitals(self) -> None:
        """Test getting all state capitals."""
        capitals = self.state_provider.get_capitals()
        # Check that a capital exists in the list of capitals
        assert "Ikeja" in capitals

    def test_get_lgas(self) -> None:
        """Test getting all LGAs for all states."""
        lgas = self.state_provider.get_lgas()
        # Check that an LGA exists in the list of all LGAs
        assert "Apapa" in lgas

    def test_get_regions(self) -> None:
        """Test getting all unique region codes."""
        regions = self.state_provider.get_regions()
        # Check that a region exists in the list of regions
        assert "South West" in regions

    def test_get_postal_codes(self) -> None:
        """Test getting all postal codes of states."""
        postal_codes = self.state_provider.get_postal_codes()
        # Check the existence of Lagos postal code in the list returned
        assert "100001" in postal_codes

    def test_get_states_by_region(self) -> None:
        """Test getting states by a specific region code."""
        states = self.state_provider.get_states_by_region("SW")
        state_names = [state["name"] for state in states]
        assert "Lagos" in state_names

    def test_get_state_by_name(self) -> None:
        """Test getting state information by state name."""
        state_info = self.state_provider.get_state_by_name("Lagos")
        assert state_info["name"] == "Lagos"
        assert state_info["code"] == "LA"
        assert state_info["capital"] == "Ikeja"

    def test_get_state_by_name_not_found(self) -> None:
        """Test getting a state by name when the state does not exist."""
        state = self.state_provider.get_state_by_name("Pythonian")
        assert state is None

    def test_get_postal_code_by_state(self) -> None:
        """Test getting the postal code of a specific state."""
        postal_code = self.state_provider.get_postal_code_by_state("Lagos")
        assert postal_code == "100001"

    def test_get_state_capital(self) -> None:
        """Test getting the capital city of a specific state."""
        capital = self.state_provider.get_state_capital("Lagos")
        assert capital == "Ikeja"

    def test_get_state_lgas(self) -> None:
        """Test getting a list of Local Government Areas for a specific state."""
        lgas = self.state_provider.get_state_lgas("Lagos")
        # Check that an LGA in Lagos is in the list
        assert "Agege" in lgas


if __name__ == "__main__":
    unittest.main()
