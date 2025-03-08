"""Unittests for the State mixins."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.mixins import State


class TestFakerStateProvider(unittest.TestCase):
    """Unit tests for the Naija methods from the StateProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.state_mixin = State()

    @patch("fakernaija.providers.StateProvider.get_states")
    @patch("random.choice")
    def test_state_without_parameters(
        self,
        mock_choice: MagicMock,
        mock_get_states: MagicMock,
    ) -> None:
        """Test state method without parameters."""
        mock_get_states.return_value = [
            {"name": "Lagos", "code": "LA"},
            {"name": "Ogun", "code": "OG"},
        ]
        mock_choice.return_value = {"name": "Lagos", "code": "LA"}

        result = self.state_mixin.state()
        self.assertEqual(result["name"], "Lagos")

    @patch("fakernaija.providers.StateProvider.get_capitals")
    @patch("random.choice")
    def test_state_capital_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_capitals: MagicMock,
    ) -> None:
        """Test capital method without state parameter."""
        mock_get_capitals.return_value = ["Ikeja", "Abeokuta"]
        mock_choice.return_value = "Ikeja"

        result = self.state_mixin.state_capital()
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.StateProvider.get_state_lgas")
    @patch("random.choice")
    def test_lga_with_state(
        self,
        mock_choice: MagicMock,
        mock_get_state_lgas: MagicMock,
    ) -> None:
        """Test lga method with state parameter."""
        mock_get_state_lgas.return_value = ["Ikeja", "Epe"]
        mock_choice.return_value = "Ikeja"

        result = self.state_mixin.state_lga(state="Lagos")
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.StateProvider.get_lgas")
    @patch("random.choice")
    def test_lga_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_lgas: MagicMock,
    ) -> None:
        """Test lga method without state parameter."""
        mock_get_lgas.return_value = ["Ikeja", "Epe", "Abeokuta"]
        mock_choice.return_value = "Ikeja"

        result = self.state_mixin.state_lga()
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.StateProvider.get_postal_code_by_state")
    def test_postal_code_with_state(
        self,
        mock_get_postal_code_by_state: MagicMock,
    ) -> None:
        """Test postal code method with state parameter."""
        mock_get_postal_code_by_state.return_value = "100001"

        result = self.state_mixin.state_postal_code(state="Lagos")
        self.assertEqual(result, "100001")

    @patch("fakernaija.providers.StateProvider.get_postal_codes")
    @patch("random.choice")
    def test_postal_code_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_postal_codes: MagicMock,
    ) -> None:
        """Test postal code method without state parameter."""
        mock_get_postal_codes.return_value = ["100001", "110001"]
        mock_choice.return_value = "100001"

        result = self.state_mixin.state_postal_code()
        self.assertEqual(result, "100001")

    @patch("fakernaija.providers.StateProvider.get_states_by_region")
    @patch("fakernaija.providers.StateProvider.validate_region")
    @patch("random.choice")
    def test_state_with_valid_region(
        self,
        mock_choice: MagicMock,
        mock_validate_region: MagicMock,
        mock_get_states_by_region: MagicMock,
    ) -> None:
        """Test state method with valid region parameter."""
        mock_get_states_by_region.return_value = [
            {"name": "Lagos", "code": "LA"},
            {"name": "Ogun", "code": "OG"},
        ]
        mock_choice.return_value = {"name": "Lagos", "code": "LA"}

        result = self.state_mixin.state(region="SW")
        self.assertEqual(result["name"], "Lagos")
        mock_validate_region.assert_called_once_with("SW")

    def test_state_invalid_region(self) -> None:
        """Test state method with invalid region and invalid state parameters."""
        with self.assertRaises(ValueError) as context:
            self.state_mixin.state(region="InvalidRegion")
        self.assertIn(
            "Invalid region abbreviation: InvalidRegion. Available options are: NC, NE, NW, SE, SS, SW",
            str(context.exception),
        )
        with self.assertRaises(ValueError) as context:
            self.state_mixin.state_name(region="InvalidRegion")
        self.assertIn(
            "Invalid region abbreviation: InvalidRegion. Available options are: NC, NE, NW, SE, SS, SW",
            str(context.exception),
        )

    def test_state_lga_invalid_state(self) -> None:
        """Test state_lga method with invalid state parameter."""
        with self.assertRaises(ValueError) as context:
            self.state_mixin.state_lga(state="InvalidState")
        self.assertIn(
            "Invalid state: InvalidState. Available states are: FCT, Abia, Adamawa, Akwa Ibom, Anambra, Bauchi, Bayelsa, Benue, Borno, Cross River, Delta, Ebonyi, Edo, Ekiti, Enugu, Gombe, Imo, Jigawa, Kaduna, Kano, Katsina, Kebbi, Kogi, Kwara, Lagos, Nassarawa, Niger, Ogun, Ondo, Osun, Oyo, Plateau, Rivers, Sokoto, Taraba, Yobe, Zamfara",
            str(context.exception),
        )
        with self.assertRaises(ValueError) as context:
            self.state_mixin.state_postal_code(state="InvalidState")
        self.assertIn(
            "Invalid state: InvalidState. Available states are: FCT, Abia, Adamawa, Akwa Ibom, Anambra, Bauchi, Bayelsa, Benue, Borno, Cross River, Delta, Ebonyi, Edo, Ekiti, Enugu, Gombe, Imo, Jigawa, Kaduna, Kano, Katsina, Kebbi, Kogi, Kwara, Lagos, Nassarawa, Niger, Ogun, Ondo, Osun, Oyo, Plateau, Rivers, Sokoto, Taraba, Yobe, Zamfara",
            str(context.exception),
        )

    @patch("fakernaija.providers.StateProvider.get_states_by_region")
    @patch("fakernaija.providers.StateProvider.validate_region")
    @patch("fakernaija.utils.get_unique_value")
    def test_state_capital_with_valid_region(
        self,
        mock_get_unique_value: MagicMock,
        mock_validate_region: MagicMock,
        mock_get_states_by_region: MagicMock,
    ) -> None:
        """Test the state_capital method with a valid region parameter."""
        # Mock the return value of get_states_by_region
        mock_get_states_by_region.return_value = [
            {
                "name": "Ogun",
                "code": "OG",
                "capital": "Abeokuta",
                "region": "South West",
            }
        ]

        # Mock validate_region to do nothing (return None)
        mock_validate_region.return_value = None

        # Mock get_unique_value to return "Abeokuta" since this is expected
        mock_get_unique_value.return_value = "Abeokuta"

        # Call the method under test
        result = self.state_mixin.state_capital(region="SW")

        # Assert that the result is as expected
        self.assertEqual(result, "Abeokuta")

        # Ensure that validate_region was called with the correct parameter
        mock_validate_region.assert_called_once_with("SW")

        # Ensure that get_states_by_region was called with the correct parameter
        mock_get_states_by_region.assert_called_once_with("SW")

    def test_state_capital_invalid_region(self) -> None:
        """Test state_capital method with invalid region parameter."""
        with self.assertRaises(ValueError) as context:
            self.state_mixin.state_capital(region="InvalidRegion")
        self.assertIn(
            "Invalid region abbreviation: InvalidRegion. Available options are: NC, NE, NW, SE, SS, SW",
            str(context.exception),
        )
