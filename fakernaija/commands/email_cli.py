"""CLI commands for EmailProvider to generate random email addresses."""

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
    help="Number of random emails to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe to generate email addresses from.",
    type=click.Choice(
        ["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"],
        case_sensitive=False,
    ),
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="Specify the gender from which emails will be generated.",
    type=click.Choice(["male", "female"], case_sensitive=False),
)
@click.option(
    "--domain",
    "-d",
    default=None,
    help="A custom domain to use for the email address.",
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv", "xml"], case_sensitive=False),
)
def email(
    repeat: int,
    tribe: str,
    gender: str,
    domain: str,
    output: str,
) -> None:
    """Return random Nigerian email addresses.

    This command generates random Nigerian email addresses.

    Args:
        repeat (int): The number of random email addresses to return.
        tribe (str): The tribe to generate names from.
        gender (str): The specific gender from which the email address will be generated.
        domain (str): A custom domain to use for the email address.
        output (str): The format of the output file.

    Examples:
        $ naija email
        $ naija email --repeat 3
        $ naija email --tribe igbo
        $ naija email --gender female
        $ naija email --domain gov.ng
        $ naija email --repeat 50 --tribe yoruba --gender male --domain gov.ng --output json
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    # Normalize tribe and gender to lowercase if they are provided
    tribe = tribe.lower() if tribe else None
    gender = gender.lower() if gender else None

    emails = []

    try:
        for _ in range(repeat):
            email = naija.email(tribe=tribe, gender=gender, domain=domain)
            if email:
                emails.append(email)
            else:
                click.echo("Error: Failed to generate email address.", err=True)

        if output:
            file_extensions = {
                "json": ".json",
                "text": ".txt",
                "csv": ".csv",
                "xml": ".xml",
            }

            base_filename = Path(f"emails{file_extensions[output]}")
            output_path = get_unique_filename(Path.cwd() / base_filename)
            write_data_to_file(emails, output_path, output, "email")

        else:
            for email in emails:
                click.echo(email)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
