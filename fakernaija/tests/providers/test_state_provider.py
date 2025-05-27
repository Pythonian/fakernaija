"""Unit tests for the StateProvider class from the fakernaija package.

This module contains unit tests for the StateProvider class, which provides methods
for accessing and validating information about Nigerian states. The tests ensure
that the methods return the expected results and handle various inputs correctly.
"""

import unittest
from unittest.mock import patch

from fakernaija.providers import StateProvider


class TestStateProvider(unittest.TestCase):
    """Test suite for the StateProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment by initializing a StateProvider instance."""
        self.state_provider = StateProvider()

    def test_get_states(self) -> None:
        """Test getting all states."""
        states = self.state_provider.get_states()
        self.assertTrue(any(state["name"] == "Lagos" for state in states))

    def test_get_state_names(self) -> None:
        """Test getting all state names."""
        state_names = self.state_provider.get_state_names()
        self.assertIn("Lagos", state_names)

    def test_get_capitals(self) -> None:
        """Test getting all state capitals."""
        capitals = self.state_provider.get_capitals()
        self.assertIn("Ikeja", capitals)

    def test_get_postal_codes(self) -> None:
        """Test getting all postal codes of states."""
        postal_codes = self.state_provider.get_postal_codes()
        self.assertIn("100001", postal_codes)

    def test_get_postal_code_by_state(self) -> None:
        """Test getting the postal code of a specific state."""
        postal_code = self.state_provider.get_postal_code_by_state("Lagos")
        self.assertEqual(postal_code, "100001")

    def test_validate_region(self) -> None:
        """Test validating a valid region abbreviation."""
        self.state_provider.validate_region("SW")

        with self.assertRaises(ValueError):
            self.state_provider.validate_region("INVALID")

    def test_get_regions(self) -> None:
        """Test getting all geopolitical regions."""
        regions = self.state_provider.get_regions()
        self.assertTrue(any(region["abbr"] == "SW" for region in regions))

    def test_get_states_by_region(self) -> None:
        """Test getting states by a specific region code."""
        states = self.state_provider.get_states_by_region("SW")
        self.assertTrue(any(state["name"] == "Lagos" for state in states))

    def test_get_state_error(self) -> None:
        """Test the _get_state method indirectly via public methods for non-existent states."""
        with self.assertRaises(ValueError) as context:
            self.state_provider.get_postal_code_by_state("InvalidState")
        self.assertIn(
            "Invalid state: InvalidState.",
            str(context.exception),
        )


class TestStateProviderExtended(unittest.TestCase):
    """Extended tests for the StateProvider class to cover additional code paths."""

    def setUp(self) -> None:
        """Sample states data for testing."""
        self.sample_states = [
            {
                "name": "Lagos",
                "code": "LA",
                "capital": "Ikeja",
                "slogan": "Power of the Sea",
                "lgas": [
                    {"name": "Ikeja", "code": "001"},
                    {"name": "Epe", "code": "002"},
                ],
                "region": "South West",
                "postal_code": "100001",
            },
            {
                "name": "Kaduna",
                "code": "KD",
                "capital": "Kaduna",
                "slogan": "Centre of Learning",
                "lgas": [
                    {"name": "Kaduna North", "code": "003"},
                    {"name": "Kaduna South", "code": "004"},
                ],
                "region": "North West",
                "postal_code": "200001",
            },
        ]
        # Patch load_json in the state provider module so that our sample data is used.
        patcher = patch(
            "fakernaija.providers.state.load_json", return_value=self.sample_states
        )
        self.mock_load_json = patcher.start()
        self.addCleanup(patcher.stop)
        self.state_provider = (
            StateProvider()
        )  # Uses patched data and runs _generate_region_abbrs()

    def test_get_lgas(self) -> None:
        """Test that get_lgas returns all LGAs from all states."""
        lgas = self.state_provider.get_lgas()
        expected = [
            {"name": "Ikeja", "code": "001"},
            {"name": "Epe", "code": "002"},
            {"name": "Kaduna North", "code": "003"},
            {"name": "Kaduna South", "code": "004"},
        ]
        self.assertEqual(lgas, expected)

    def test_get_state_lgas_valid(self) -> None:
        """Test that get_state_lgas returns LGAs for a valid state."""
        lgas = self.state_provider.get_state_lgas("Lagos")
        expected = [{"name": "Ikeja", "code": "001"}, {"name": "Epe", "code": "002"}]
        self.assertEqual(lgas, expected)

    def test_get_state_lgas_invalid(self) -> None:
        """Test that get_state_lgas raises a ValueError for an invalid state."""
        with self.assertRaises(ValueError) as context:
            self.state_provider.get_state_lgas("InvalidState")
        # Verify that the error message mentions the invalid state.
        self.assertIn("Invalid state: InvalidState.", str(context.exception))

    def test_get_lga_codes_all(self) -> None:
        """Test that get_lga_codes returns LGA codes for all states when no state is specified."""
        lga_codes = self.state_provider.get_lga_codes()
        expected = {
            "Lagos": ["001", "002"],
            "Kaduna": ["003", "004"],
        }
        self.assertEqual(lga_codes, expected)

    def test_get_lga_codes_specific(self) -> None:
        """Test that get_lga_codes returns LGA codes for a specific state."""
        lga_codes = self.state_provider.get_lga_codes("Kaduna")
        expected = {"Kaduna": ["003", "004"]}
        self.assertEqual(lga_codes, expected)

    def test_get_state_suggestions(self) -> None:
        """Test that _get_state returns suggestions when a near-match is provided."""
        # Patch difflib.get_close_matches to simulate suggestions.
        with patch(
            "fakernaija.providers.state.difflib.get_close_matches",
            return_value=["Lagos"],
        ) as mock_get_close_matches:
            with self.assertRaises(ValueError) as context:
                self.state_provider.get_postal_code_by_state("Lago")
            error_message = str(context.exception)
            # Verify that the error message contains a suggestion.
            self.assertIn("Did you mean: Lagos?", error_message)
            # Check that get_close_matches was called with expected arguments.
            available_states = ", ".join(self.state_provider.get_state_names())
            mock_get_close_matches.assert_called_with(
                "Lago", available_states, n=3, cutoff=0.6
            )
