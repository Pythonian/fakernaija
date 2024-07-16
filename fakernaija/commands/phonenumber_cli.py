"""CLI commands for PhoneNumberProvider to generate random Nigerian phone numbers."""

from pathlib import Path

import click

from fakernaija.faker import Faker
from fakernaija.utils import get_unique_filename, write_data_to_file

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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv", "xml"], case_sensitive=False),
)
def phonenumber(repeat: int, network: str, prefix: str, output: str) -> None:
    """Return random Nigerian phone numbers.

    This command generates random Nigerian phone numbers.

    Args:
        repeat (int): The number of random phone numbers to return.
        network (str): The network type (mtn, glo, airtel, etisalat).
        prefix (str): The specific prefix for the phone number.
        output (str): The format of the output file.

    Examples:
        $ naija phonenumber
        $ naija phonenumber --repeat 3
        $ naija phonenumber --network mtn
        $ naija phonenumber --prefix 0703
        $ naija phonenumber -r 3 --network glo --prefix 0805 --output json
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    phonenumbers = []

    try:
        for _ in range(repeat):
            phonenumber = naija.phone_number(network=network, prefix=prefix)
            if phonenumber:
                phonenumbers.append(phonenumber)
            else:
                click.echo("Error: Failed to generate phone number.", err=True)

        if output:
            file_extensions = {
                "json": ".json",
                "text": ".txt",
                "csv": ".csv",
                "xml": ".xml",
            }

            base_filename = Path(f"phonenumbers{file_extensions[output]}")
            output_path = get_unique_filename(Path.cwd() / base_filename)
            write_data_to_file(phonenumbers, output_path, output, "phonenumber")

        else:
            for phonenumber in phonenumbers:
                click.echo(phonenumber)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
