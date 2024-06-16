"""Currency mixin to group related methods for the CurrencyProvider."""

import random

from fakernaija.providers.currency_provider import CurrencyProvider


class Currency:
    """Methods for the CurrencyProvider."""

    def __init__(self) -> None:
        """Initializes the Currency mixin and its provider."""
        self.currency_provider = CurrencyProvider()

    def currency(self) -> tuple[str, str]:
        """Generates the currency code and name.

        Returns:
            tuple[str, str]: The currency code and name.

        Examples:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> currency = naija.currency()
                >>> print(f"Nigerian currency: {currency}")
                'Nigerian currency: ("NGN", "Nigerian naira")'
        """
        return self.currency_provider.get_currency()

    def currency_code(self) -> str:
        """Generates the currency code.

        Returns:
            str: The currency code.

        Examples:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
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

                >>> from fakernaija.faker import Faker
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

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> currency_symbol = naija.currency_symbol()
                >>> print(f"Nigerian currency symbol: {currency_symbol}")
                'Nigerian currency symbol: ₦'
        """
        return self.currency_provider.get_currency_symbol()

    def pricetag(self) -> str:
        """Generates a random price tag with the Nigerian currency.

        Returns:
            str: The formatted price tag.

        Examples:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> pricetag = naija.pricetag()
                >>> print(f"Pricetag: {pricetag}")
                'Pricetag: ₦2,235.00'
        """
        amount = random.uniform(1, 100000)

        # Decide if the amount should be rounded to the nearest hundred with 30% probability
        if random.random() < 0.3:  # noqa: PLR2004
            amount = round(amount / 100) * 100

        # Decide if there should be a kobo value or .00
        include_kobo = random.choice([True, False])

        if include_kobo:
            return self.currency_provider.get_pricetag(amount)
        return self.currency_provider.get_pricetag(amount).split(".")[0] + ".00"
