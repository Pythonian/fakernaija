"""Unit tests for the PhoneNumberProvider class.

This module contains unit tests for the PhoneNumberProvider class, which provides methods
for generating random Nigerian phone number. The tests ensure that the
methods return the expected phone number based on network type and prefix specified.
"""

import unittest

from fakernaija.providers.phonenumbers import PhoneNumberProvider

PHONE_NUMBER_LENGTH = 11


class TestPhoneNumberProvider(unittest.TestCase):
    """Test suite for the PhoneNumberProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.provider = PhoneNumberProvider()

    def test_generate_phone_number(self) -> None:
        """Test that generate_phone_number returns a valid phone number."""
        prefix = "0703"
        phone_number = self.provider.generate_phone_number(prefix)
        assert phone_number.startswith(prefix)
        assert len(phone_number) == PHONE_NUMBER_LENGTH

    def test_phone_number_random(self) -> None:
        """Test that phone_number generates a valid random phone number."""
        phone_number = self.provider.phone_number()
        assert phone_number.startswith(tuple(self.provider.all_prefixes))
        assert len(phone_number) == PHONE_NUMBER_LENGTH

    def test_phone_number_with_valid_network(self) -> None:
        """Test that phone_number generates a valid phone number for a specific network."""
        phone_number = self.provider.phone_number(network="mtn")
        assert phone_number.startswith(tuple(self.provider.network_prefixes["mtn"]))
        assert len(phone_number) == PHONE_NUMBER_LENGTH

    def test_phone_number_with_valid_prefix(self) -> None:
        """Test that phone_number generates a valid phone number for a specific prefix."""
        prefix = "0805"
        phone_number = self.provider.phone_number(prefix=prefix)
        assert phone_number.startswith(prefix)
        assert len(phone_number) == PHONE_NUMBER_LENGTH

    def test_phone_number_with_invalid_prefix(self) -> None:
        """Test that phone_number raises ValueError for an invalid prefix."""
        with self.assertRaises(ValueError):
            self.provider.phone_number(prefix="1234")

    def test_phone_number_with_invalid_network(self) -> None:
        """Test that phone_number raises ValueError for an invalid network."""
        with self.assertRaises(ValueError):
            self.provider.phone_number(network="invalid_network")

    def test_phone_number_with_network_and_prefix(self) -> None:
        """Test that phone_number generates a valid phone number for a specific network and prefix."""
        phone_number = self.provider.phone_number(network="glo", prefix="0705")
        assert phone_number.startswith("0705")
        assert len(phone_number) == PHONE_NUMBER_LENGTH

    def test_phone_number_with_invalid_network_and_prefix(self) -> None:
        """Test that phone_number raises ValueError for a valid network and invalid prefix combination."""
        with self.assertRaises(ValueError):
            self.provider.phone_number(network="glo", prefix="0703")


if __name__ == "__main__":
    unittest.main()
