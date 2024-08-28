"""Unittests for the State mixins."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija import Naija


class TestFakerStateProvider(unittest.TestCase):
    """Unit tests for the Naija method from the StateProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.naija = Naija()

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

        result = self.naija.state()
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

        result = self.naija.state_capital()
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

        result = self.naija.state_lga(state="Lagos")
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

        result = self.naija.state_lga()
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.StateProvider.get_postal_code_by_state")
    def test_postal_code_with_state(
        self,
        mock_get_postal_code_by_state: MagicMock,
    ) -> None:
        """Test postal code method with state parameter."""
        mock_get_postal_code_by_state.return_value = "100001"

        result = self.naija.state_postal_code(state="Lagos")
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

        result = self.naija.state_postal_code()
        self.assertEqual(result, "100001")
