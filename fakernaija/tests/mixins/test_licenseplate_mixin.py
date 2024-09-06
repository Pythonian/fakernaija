"""Unit tests for the LicensePlate mixin methods."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.mixins.license_plate import LicensePlate
from fakernaija.providers import LicensePlateProvider


class TestLicensePlateMixin(unittest.TestCase):
    """Test cases for the LicensePlate mixin class."""

    def setUp(self) -> None:
        """Set up the LicensePlate mixin instance for testing."""
        self.mixin = LicensePlate()

    @patch.object(LicensePlateProvider, "generate_license_plate")
    def test_license_plate_no_state(
        self, mock_generate_license_plate: MagicMock
    ) -> None:
        """Test license plate generation with no state."""
        # Arrange: Mock the provider to return a specific value
        mock_generate_license_plate.return_value = "ABJ-123XY"

        # Act: Call the license_plate method without a state
        plate = self.mixin.license_plate()

        # Assert: Ensure the mock was called and the correct value was returned
        mock_generate_license_plate.assert_called_once_with(state=None)
        self.assertEqual(plate, "ABJ-123XY")

    @patch.object(LicensePlateProvider, "generate_license_plate")
    def test_license_plate_with_valid_state(
        self, mock_generate_license_plate: MagicMock
    ) -> None:
        """Test license plate generation with a valid state."""
        # Arrange: Mock the provider to return a specific value
        mock_generate_license_plate.return_value = "LAG-456ZZ"

        # Act: Call the license_plate method with a valid state
        plate = self.mixin.license_plate(state="Lagos")

        # Assert: Ensure the mock was called with the correct state and the correct value was returned
        mock_generate_license_plate.assert_called_once_with(state="Lagos")
        self.assertEqual(plate, "LAG-456ZZ")

    @patch.object(LicensePlateProvider, "generate_license_plate")
    def test_license_plate_with_invalid_state(
        self, mock_generate_license_plate: MagicMock
    ) -> None:
        """Test license plate generation with an invalid state (raising ValueError)."""
        # Arrange: Mock the provider to raise a ValueError
        mock_generate_license_plate.side_effect = ValueError("Invalid state name")

        # Act & Assert: Call the license_plate method with an invalid state and check for ValueError
        with self.assertRaises(ValueError) as context:
            self.mixin.license_plate(state="InvalidState")

        self.assertIn("Invalid state name", str(context.exception))
        mock_generate_license_plate.assert_called_once_with(state="InvalidState")
