"""CLI commands for PhoneNumberProvider to generate random Nigerian phone numbers."""

import click

from fakernaija.faker import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random phone numbers to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--network",
    "-n",
    default=None,
    help="Type of network to generate.",
    type=click.Choice(["mtn", "glo", "airtel", "etisalat"]),
)
@click.option(
    "--prefix",
    "-p",
    default=None,
    help="Specific prefix to generate the phone number from.",
)
def phonenumber(repeat: int, network: str, prefix: str) -> None:
    """Return random Nigerian phone numbers.

    This command generates random Nigerian phone numbers.

    Args:
        repeat (int): The number of random phone numbers to return.
        network (str): The network type (mtn, glo, airtel, etisalat).
        prefix (str): The specific prefix for the phone number.

    Examples:
        $ naija phonenumber
        $ naija phonenumber --repeat 3
        $ naija phonenumber --network mtn
        $ naija phonenumber --prefix 0703
        $ naija phonenumber --repeat 3 --network glo --prefix 0805
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        for _ in range(repeat):
            phonenumber = naija.phone_number(network=network, prefix=prefix)
            if phonenumber:
                click.echo(phonenumber)
            else:
                click.echo("Error: Failed to generate phonenumber.", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
