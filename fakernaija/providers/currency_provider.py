"""This module provides a CurrencyProvider class for generating Nigerian currency."""


class CurrencyProvider:
    """Provides functionality for generating currency related to Nigerian Naira."""

    def __init__(self) -> None:
        """Initialize the CurrencyProvider."""
        self.currency_code = "NGN"
        self.currency_name = "Nigerian naira"
        self.currency_symbol = "₦"

    def get_currency(self) -> tuple[str, str]:
        """Returns the currency code and name as a tuple.

        Returns:
            tuple[str, str]: The currency code and currency name.
        """
        return self.currency_code, self.currency_name

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

    def get_pricetag(self, amount: float) -> str:
        """Get a formatted pricetag with the currency symbol.

        Args:
            amount (float): The amount to format.

        Returns:
            str: The formatted pricetag.
        """
        return f"{self.currency_symbol}{amount:,.2f}"
