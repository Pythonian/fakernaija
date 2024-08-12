"""Currency mixin to group related methods for the CurrencyProvider."""

from fakernaija.providers.currency_provider import CurrencyProvider


class Currency:
    """Methods for the CurrencyProvider."""

    def __init__(self) -> None:
        """Initializes the Currency mixin and its provider."""
        self.currency_provider = CurrencyProvider()

    def currency(self) -> dict[str, str]:
        """Generates the currency code and name.

        Returns:
            dict[str, str]: The currency code and name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> currency = naija.currency()
                >>> print(f"Nigerian currency: {currency}")
                "Nigerian currency: {'code': 'NGN', 'name': 'Nigerian naira', 'symbol': '₦'}"
        """
        return self.currency_provider.get_currency()

    def currency_code(self) -> str:
        """Generates the currency code.

        Returns:
            str: The currency code.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> currency_code = naija.currency_code()
                >>> print(f"Nigerian currency code: {currency_code}")
                'Nigerian currency code: NGN'
        """
        return self.currency_provider.get_currency_code()

    def currency_name(self) -> str:
        """Generates the currency name.

        Returns:
            str: The currency name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> currency_name = naija.currency_name()
                >>> print(f"Nigerian currency name: {currency_name}")
                'Nigerian currency name: Nigerian naira'
        """
        return self.currency_provider.get_currency_name()

    def currency_symbol(self) -> str:
        """Generates the currency symbol.

        Returns:
            str: The currency symbol.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> currency_symbol = naija.currency_symbol()
                >>> print(f"Nigerian currency symbol: {currency_symbol}")
                'Nigerian currency symbol: ₦'
        """
        return self.currency_provider.get_currency_symbol()
