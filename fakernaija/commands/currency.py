"""Currency commands to return Nigerian currency data."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
def currency() -> None:
    """Returns Nigerian currency object.

    Example:
        .. code-block:: bash

            $ naija currency
            {'code': 'NGN', 'name': 'Nigerian naira', 'symbol': '₦'}
    """
    currency = naija.currency()
    if currency:
        click.echo(currency)
    else:
        click.echo("Error: Failed to return currency object.", err=True)


@click.command()
def currency_code() -> None:
    """Returns Nigerian currency code.

    Example:
        .. code-block:: bash

            $ naija currency_code
            NGN
    """
    currency_code = naija.currency_code()
    if currency_code:
        click.echo(currency_code)
    else:
        click.echo("Error: Failed to return currency code.", err=True)


@click.command()
def currency_name() -> None:
    """Returns Nigerian currency name.

    Example:
        .. code-block:: bash

            $ naija currency_name
            Nigerian naira
    """
    currency_name = naija.currency_name()
    if currency_name:
        click.echo(currency_name)
    else:
        click.echo("Error: Failed to return currency name.", err=True)


@click.command()
def currency_symbol() -> None:
    """Returns Nigerian currency symbol.

    Example:
        .. code-block:: bash

            $ naija currency_symbol
            ₦
    """
    currency_symbol = naija.currency_symbol()
    if currency_symbol:
        click.echo(currency_symbol)
    else:
        click.echo("Error: Failed to return currency symbol.", err=True)
