"""Unit tests for the StateProvider class from the fakernaija package.

This module contains unit tests for the StateProvider class, which provides methods
for accessing and validating information about Nigerian states. The tests ensure
that the methods return the expected results and handle various inputs correctly.
"""

import unittest

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

    def test_get_lgas(self) -> None:
        """Test getting all LGAs for all states."""
        lgas = self.state_provider.get_lgas()
        self.assertIn("Apapa", lgas)

    def test_get_postal_codes(self) -> None:
        """Test getting all postal codes of states."""
        postal_codes = self.state_provider.get_postal_codes()
        self.assertIn("100001", postal_codes)

    def test_get_postal_code_by_state(self) -> None:
        """Test getting the postal code of a specific state."""
        postal_code = self.state_provider.get_postal_code_by_state("Lagos")
        self.assertEqual(postal_code, "100001")

    def test_get_state_lgas(self) -> None:
        """Test getting a list of Local Government Areas for a specific state."""
        lgas = self.state_provider.get_state_lgas("Lagos")
        self.assertIn("Agege", lgas)

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
            "State 'InvalidState' does not exist in Nigeria.",
            str(context.exception),
        )
