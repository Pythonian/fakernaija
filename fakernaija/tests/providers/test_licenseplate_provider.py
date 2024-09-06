"""LicensePlateProvider unittests."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers.license_plate import LicensePlateProvider
from fakernaija.providers.state import StateProvider


class TestLicensePlateProvider(unittest.TestCase):
    """Test cases for the LicensePlateProvider class."""

    def setUp(self) -> None:
        """Set up a LicensePlateProvider instance for testing."""
        self.license_plate_provider = LicensePlateProvider()
        self.state_provider = StateProvider()

    @patch.object(StateProvider, "get_state_names")
    @patch.object(StateProvider, "get_lga_codes")
    def test_generate_license_plate_valid_state(
        self,
        mock_get_lga_codes: MagicMock,
        mock_get_state_names: MagicMock,
    ) -> None:
        """Test license plate generation with a valid state."""
        # Mocking data for a valid state
        mock_get_state_names.return_value = ["FCT", "Lagos"]
        mock_get_lga_codes.return_value = {
            "FCT": ["ABJ", "KWA", "KUJ", "GWA", "BWR"],
            "Lagos": ["IKE", "EPE"],
        }

        state = "FCT"
        plate = self.license_plate_provider.generate_license_plate(state)

        self.assertTrue(
            any(
                plate.startswith(prefix)
                for prefix in ["ABJ-", "KWA-", "KUJ-", "GWA-", "BWR-"]
            )
        )
        self.assertRegex(plate, r"^[A-Z]{3}-\d{3}[A-Z]{2}$")

    @patch.object(StateProvider, "get_state_names")
    def test_generate_license_plate_invalid_state(
        self, mock_get_state_names: MagicMock
    ) -> None:
        """Test license plate generation with an invalid state."""
        mock_get_state_names.return_value = ["FCT", "Lagos"]

        state = "InvalidState"
        with self.assertRaises(ValueError) as context:
            self.license_plate_provider.generate_license_plate(state)

        self.assertIn("Invalid state name: invalidstate", str(context.exception))

    @patch.object(StateProvider, "get_lga_codes")
    def test_generate_license_plate_no_state(
        self, mock_get_lga_codes: MagicMock
    ) -> None:
        """Test license plate generation when no state is provided."""
        mock_get_lga_codes.return_value = {
            "FCT": ["ABJ", "KWA", "KUJ"],
            "Lagos": ["IKE", "EPE"],
        }

        plate = self.license_plate_provider.generate_license_plate()

        self.assertRegex(plate, r"^[A-Z]{3}-\d{3}[A-Z]{2}$")

    @patch(
        "fakernaija.providers.license_plate.normalize_input",
        side_effect=lambda x: x.strip().lower(),
    )
    @patch.object(StateProvider, "get_state_names")
    def test_generate_license_plate_case_insensitivity(
        self, mock_get_state_names: MagicMock, mock_normalize_input: MagicMock
    ) -> None:
        """Test license plate generation with case-insensitive state input."""
        mock_get_state_names.return_value = ["FCT", "Lagos"]

        state = "fct"  # lower case input
        plate = self.license_plate_provider.generate_license_plate(state)

        self.assertRegex(plate, r"^[A-Z]{3}-\d{3}[A-Z]{2}$")
        mock_normalize_input.assert_called_once_with("fct")

    @patch.object(StateProvider, "get_state_names")
    @patch.object(StateProvider, "get_lga_codes")
    def test_generate_license_plate_random_selection(
        self,
        mock_get_lga_codes: MagicMock,
        mock_get_state_names: MagicMock,
    ) -> None:
        """Test license plate generation with random LGA selection when no state is specified."""
        mock_get_state_names.return_value = ["FCT", "Lagos"]
        mock_get_lga_codes.return_value = {
            "FCT": ["ABJ", "KWA", "KUJ"],
            "Lagos": ["IKE", "EPE"],
        }

        plate = self.license_plate_provider.generate_license_plate()

        self.assertRegex(plate, r"^[A-Z]{3}-\d{3}[A-Z]{2}$")
