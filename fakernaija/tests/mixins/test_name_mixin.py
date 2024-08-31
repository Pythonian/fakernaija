"""Unit tests for the Name mixin methods.

This module contains unit tests for the Name mixin class, which provides methods
to interact with the NameProvider class for generating names.
"""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.mixins import Name
from fakernaija.providers import NameProvider


class TestNameMixin(unittest.TestCase):
    """Unit tests for the Name mixin."""

    def setUp(self) -> None:
        """Setup the Name mixin for testing."""
        self.name_mixin = Name()

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_default(self, mock_generate_first_name: MagicMock) -> None:
        """Test first_name method without parameters."""
        mock_generate_first_name.return_value = "Nasiru"
        result = self.name_mixin.first_name()
        self.assertEqual(result, "Nasiru")
        mock_generate_first_name.assert_called_once_with(tribe=None, gender=None)

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_with_tribe(self, mock_generate_first_name: MagicMock) -> None:
        """Test first_name method with tribe parameter."""
        mock_generate_first_name.return_value = "Opeyemi"
        result = self.name_mixin.first_name(tribe="yoruba")
        self.assertEqual(result, "Opeyemi")
        mock_generate_first_name.assert_called_once_with(tribe="yoruba", gender=None)

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_with_gender(self, mock_generate_first_name: MagicMock) -> None:
        """Test first_name method with gender parameter."""
        mock_generate_first_name.return_value = "Somtochi"
        result = self.name_mixin.first_name(gender="female")
        self.assertEqual(result, "Somtochi")
        mock_generate_first_name.assert_called_once_with(tribe=None, gender="female")

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_with_tribe_and_gender(
        self, mock_generate_first_name: MagicMock
    ) -> None:
        """Test first_name method with both tribe and gender parameters."""
        mock_generate_first_name.return_value = "Seyi"
        result = self.name_mixin.first_name(tribe="yoruba", gender="male")
        self.assertEqual(result, "Seyi")
        mock_generate_first_name.assert_called_once_with(tribe="yoruba", gender="male")

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_invalid_tribe(
        self, mock_generate_first_name: MagicMock
    ) -> None:
        """Test first_name method raises ValueError for invalid tribe."""
        mock_generate_first_name.side_effect = ValueError("Invalid tribe")
        with self.assertRaises(ValueError) as context:
            self.name_mixin.first_name(tribe="invalid_tribe")
        self.assertEqual(str(context.exception), "Invalid tribe")

    @patch.object(NameProvider, "generate_first_name")
    def test_first_name_invalid_gender(
        self, mock_generate_first_name: MagicMock
    ) -> None:
        """Test first_name method raises ValueError for invalid gender."""
        mock_generate_first_name.side_effect = ValueError("Invalid gender")
        with self.assertRaises(ValueError) as context:
            self.name_mixin.first_name(gender="invalid_gender")
        self.assertEqual(str(context.exception), "Invalid gender")

    @patch.object(NameProvider, "generate_last_name")
    def test_last_name_default(self, mock_generate_last_name: MagicMock) -> None:
        """Test last_name method without parameters."""
        mock_generate_last_name.return_value = "Okonkwo"
        result = self.name_mixin.last_name()
        self.assertEqual(result, "Okonkwo")
        mock_generate_last_name.assert_called_once_with(tribe=None)

    @patch.object(NameProvider, "generate_last_name")
    def test_last_name_with_tribe(self, mock_generate_last_name: MagicMock) -> None:
        """Test last_name method with tribe parameter."""
        mock_generate_last_name.return_value = "Abubakar"
        result = self.name_mixin.last_name(tribe="hausa")
        self.assertEqual(result, "Abubakar")
        mock_generate_last_name.assert_called_once_with(tribe="hausa")

    @patch.object(NameProvider, "generate_last_name")
    def test_last_name_invalid_tribe(self, mock_generate_last_name: MagicMock) -> None:
        """Test last_name method raises ValueError for invalid tribe."""
        mock_generate_last_name.side_effect = ValueError("Invalid tribe")
        with self.assertRaises(ValueError) as context:
            self.name_mixin.last_name(tribe="invalid_tribe")
        self.assertEqual(str(context.exception), "Invalid tribe")

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_default(self, mock_generate_full_name: MagicMock) -> None:
        """Test full_name method without parameters."""
        mock_generate_full_name.return_value = "Ugochi Maduike"
        result = self.name_mixin.full_name()
        self.assertEqual(result, "Ugochi Maduike")
        mock_generate_full_name.assert_called_once_with(
            middle_name=False, tribe=None, gender=None
        )

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_with_middle_name(
        self, mock_generate_full_name: MagicMock
    ) -> None:
        """Test full_name method with middle_name parameter."""
        mock_generate_full_name.return_value = "Kosisochukwu Somtochukwu Mbakwe"
        result = self.name_mixin.full_name(middle_name=True)
        self.assertEqual(result, "Kosisochukwu Somtochukwu Mbakwe")
        mock_generate_full_name.assert_called_once_with(
            middle_name=True, tribe=None, gender=None
        )

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_with_tribe(self, mock_generate_full_name: MagicMock) -> None:
        """Test full_name method with tribe parameter."""
        mock_generate_full_name.return_value = "Opeyemi Obisesan"
        result = self.name_mixin.full_name(tribe="yoruba")
        self.assertEqual(result, "Opeyemi Obisesan")
        mock_generate_full_name.assert_called_once_with(
            middle_name=False, tribe="yoruba", gender=None
        )

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_with_gender(self, mock_generate_full_name: MagicMock) -> None:
        """Test full_name method with gender parameter."""
        mock_generate_full_name.return_value = "Chisom Nnabude"
        result = self.name_mixin.full_name(gender="female")
        self.assertEqual(result, "Chisom Nnabude")
        mock_generate_full_name.assert_called_once_with(
            middle_name=False, tribe=None, gender="female"
        )

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_with_all_parameters(
        self, mock_generate_full_name: MagicMock
    ) -> None:
        """Test full_name method with all parameters."""
        mock_generate_full_name.return_value = "Osazee Osahon Ogiemwonyi"
        result = self.name_mixin.full_name(
            middle_name=True, tribe="edo", gender="female"
        )
        self.assertEqual(result, "Osazee Osahon Ogiemwonyi")
        mock_generate_full_name.assert_called_once_with(
            middle_name=True, tribe="edo", gender="female"
        )

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_invalid_tribe(self, mock_generate_full_name: MagicMock) -> None:
        """Test full_name method raises ValueError for invalid tribe."""
        mock_generate_full_name.side_effect = ValueError("Invalid tribe")
        with self.assertRaises(ValueError) as context:
            self.name_mixin.full_name(tribe="invalid_tribe")
        self.assertEqual(str(context.exception), "Invalid tribe")

    @patch.object(NameProvider, "generate_full_name")
    def test_full_name_invalid_gender(self, mock_generate_full_name: MagicMock) -> None:
        """Test full_name method raises ValueError for invalid gender."""
        mock_generate_full_name.side_effect = ValueError("Invalid gender")
        with self.assertRaises(ValueError) as context:
            self.name_mixin.full_name(gender="invalid_gender")
        self.assertEqual(str(context.exception), "Invalid gender")
