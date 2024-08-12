"""CLI commands for CurrencyProvider to return Nigerian Naira information."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
def currency() -> None:
    """Return currency code and name.

    This command returns Nigerian currency code and name.

    Examples:
        $ naija currency
    """
    currency = naija.currency()
    if currency:
        click.echo(currency)
    else:
        click.echo("Error: Failed to generate currency.", err=True)


@click.command()
def currency_code() -> None:
    """Return the currency code.

    This command returns Nigerian currency code.

    Examples:
        $ naija currency_code
    """
    currency_code = naija.currency_code()
    if currency_code:
        click.echo(currency_code)
    else:
        click.echo("Error: Failed to generate currency code.", err=True)


@click.command()
def currency_name() -> None:
    """Return the currency name.

    This command returns Nigerian currency name.

    Examples:
        $ naija currency_name
    """
    currency_name = naija.currency_name()
    if currency_name:
        click.echo(currency_name)
    else:
        click.echo("Error: Failed to generate currency name.", err=True)


@click.command()
def currency_symbol() -> None:
    """Return the currency symbol.

    This command returns Nigerian currency symbol.

    Examples:
        $ naija currency_symbol
    """
    currency_symbol = naija.currency_symbol()
    if currency_symbol:
        click.echo(currency_symbol)
    else:
        click.echo("Error: Failed to generate currency symbol.", err=True)
