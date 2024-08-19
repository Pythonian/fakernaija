"""Unit tests for the CurrencyProvider class."""

import unittest

from fakernaija.providers import CurrencyProvider


class TestCurrencyProvider(unittest.TestCase):
    """Test suite for the CurrencyProvider class."""

    def setUp(self) -> None:
        """Set up the CurrencyProvider instance for testing."""
        self.currency_provider = CurrencyProvider()

    def test_get_currency(self) -> None:
        """Test the get_currency method for returning the currency code, name and symbol."""
        self.assertEqual(
            self.currency_provider.get_currency(),
            {"code": "NGN", "name": "Nigerian naira", "symbol": "₦"},
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
