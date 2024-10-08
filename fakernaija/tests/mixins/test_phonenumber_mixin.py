"""Unit tests for the PhoneNumber mixin classes which exposes methods to the Naija class."""

import unittest

from fakernaija import Naija

PHONE_NUMBER_LENGTH = 11


class TestNaijaPhoneNumberProvider(unittest.TestCase):
    """Unit tests for the Naija method from the PhoneNumberProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.naija = Naija()

    def test_phone_number(self) -> None:
        """Test that phone_number returns a valid Nigerian phone number."""
        number = self.naija.phone_number()
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)

    def test_phone_number_with_network(self) -> None:
        """Test that phone_number returns a valid phone number for a given network."""
        number = self.naija.phone_number(network="mtn")
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)
        self.assertTrue(
            number.startswith(
                (
                    "0703",
                    "0706",
                    "0803",
                    "0806",
                    "0813",
                    "0816",
                    "0810",
                    "0814",
                    "0903",
                    "0906",
                    "0913",
                    "0916",
                ),
            ),
        )

    def test_phone_number_with_prefix(self) -> None:
        """Test that phone_number returns a valid phone number for a given prefix."""
        number = self.naija.phone_number(prefix="0803")
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)
        self.assertTrue(number.startswith("0803"))

    def test_phone_number_with_invalid_prefix(self) -> None:
        """Test that phone_number raises ValueError for an invalid prefix."""
        with self.assertRaises(ValueError):
            self.naija.phone_number(prefix="0999")

    def test_phone_number_with_invalid_network(self) -> None:
        """Test that phone_number raises ValueError for an invalid network."""
        with self.assertRaises(ValueError):
            self.naija.phone_number(network="invalid_network")
