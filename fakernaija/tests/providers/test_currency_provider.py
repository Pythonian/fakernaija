"""Unit tests for the CurrencyProvider class.

This module contains unit tests for the CurrencyProvider class, which provides
methods to generate and return Nigerian currency information.
"""

import unittest

from fakernaija.providers.currency_provider import CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    """Test suite for the CurrencyProvider class."""

    def setUp(self) -> None:
        """Set up the CurrencyProvider instance for testing."""
        self.currency_provider = CurrencyProvider()

    def test_get_currency(self) -> None:
        """Test the get_currency method for returning the currency code and name."""
        self.assertEqual(
            self.currency_provider.get_currency(),
            ("NGN", "Nigerian naira"),
        )

    def test_get_currency_code(self) -> None:
        """Test the get_currency_code method for returning the currency code."""
        self.assertEqual(self.currency_provider.get_currency_code(), "NGN")

    def test_get_currency_name(self) -> None:
        """Test the get_currency_name method for returning the currency name."""
        self.assertEqual(self.currency_provider.get_currency_name(), "Nigerian naira")

    def test_get_currency_symbol(self) -> None:
        """Test the get_currency_symbol method for returning the currency symbol."""
        self.assertEqual(self.currency_provider.get_currency_symbol(), "₦")

    def test_get_pricetag(self) -> None:
        """Test the get_pricetag method for generating a formatted price tag."""
        amount = 1234.56
        self.assertEqual(self.currency_provider.get_pricetag(amount), "₦1,234.56")
