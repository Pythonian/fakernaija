"""This module provides a CurrencyProvider class for generating Nigerian currency."""


class CurrencyProvider:
    """Provides functionality for generating currency related to Nigerian Naira."""

    def __init__(self) -> None:
        """Initialize the CurrencyProvider."""
        self.currency_code = "NGN"
        self.currency_name = "Nigerian naira"
        self.currency_symbol = "₦"

    def get_currency(self) -> dict[str, str]:
        """Returns the currency code and name as a dictionary.

        Returns:
            dict[str, str]: The currency code and currency name.
        """
        return {
            "code": self.currency_code,
            "name": self.currency_name,
        }

    def get_currency_code(self) -> str:
        """Returns the currency code.

        Returns:
            str: The currency code.
        """
        return self.currency_code

    def get_currency_name(self) -> str:
        """Returns the currency name.

        Returns:
            str: The currency name.
        """
        return self.currency_name

    def get_currency_symbol(self) -> str:
        """Returns the currency symbol.

        Returns:
            str: The currency symbol.
        """
        return self.currency_symbol
