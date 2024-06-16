"""Unit tests for the Currency mixin methods.

This module contains unit tests for the Currency class, which provides methods
to interact with the CurrencyProvider class for generating Nigerian currency
related information.
"""

import unittest

from fakernaija.mixins.currency_mixin import Currency


class TestCurrency(unittest.TestCase):
    """Test suite for the Currency class."""

    def setUp(self) -> None:
        """Set up the Currency instance for testing."""
        self.currency = Currency()

    def test_currency(self) -> None:
        """Test the currency method for returning the currency code and name."""
        self.assertEqual(self.currency.currency(), ("NGN", "Nigerian naira"))

    def test_currency_code(self) -> None:
        """Test the currency_code method for returning the currency code."""
        self.assertEqual(self.currency.currency_code(), "NGN")

    def test_currency_name(self) -> None:
        """Test the currency_name method for returning the currency name."""
        self.assertEqual(self.currency.currency_name(), "Nigerian naira")

    def test_currency_symbol(self) -> None:
        """Test the currency_symbol method for returning the currency symbol."""
        self.assertEqual(self.currency.currency_symbol(), "₦")

    def test_pricetag(self) -> None:
        """Test the pricetag method for generating a formatted price tag."""
        pricetag = self.currency.pricetag()
        self.assertTrue(pricetag.startswith("₦"))
        self.assertTrue(pricetag.endswith(".00") or pricetag[-3] == ".")
