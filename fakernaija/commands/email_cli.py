"""CLI commands for EmailProvider to generate random email addresses."""

import json
import re
from pathlib import Path

import click

from fakernaija.faker import Faker

naija = Faker()

# Regex pattern to match invalid characters for output file names
INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*]')


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
    help="The path to the output JSON file. If not provided, prints to stdout.",
    type=click.Path(dir_okay=False, writable=True, path_type=Path),
)
def email(repeat: int, tribe: str, gender: str, domain: str, output: Path) -> None:
    """Return random Nigerian email addresses.

    This command generates random Nigerian email addresses.

    Args:
        repeat (int): The number of random email addresses to return.
        tribe (str): The tribe to generate names from (yoruba, igbo, hausa, edo, fulani, ijaw).
        gender (str): The specific gender from which the email address will be generated.
        domain (str): A custom domain to use for the email address.
        output (Path): The path to the output JSON file.

    Examples:
        $ naija email
        $ naija email --repeat 3
        $ naija email --tribe igbo
        $ naija email --gender female
        $ naija email --domain gov.ng
        $ naija email --repeat 50 --tribe yoruba --gender male --domain gov.ng --output emails.json
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    # Normalize tribe and gender to lowercase if they are provided
    tribe = tribe.lower() if tribe else None
    gender = gender.lower() if gender else None

    if output and INVALID_FILENAME_CHARS.search(output.name):
        click.echo("Error: Output file name contains invalid characters.", err=True)
        return

    emails = []

    try:
        for _ in range(repeat):
            email = naija.email(tribe=tribe, gender=gender, domain=domain)
            if email:
                emails.append(email)
            else:
                click.echo("Error: Failed to generate email address.", err=True)

        if output:
            output_path = Path.cwd() / output
            try:
                with output_path.open("w") as f:
                    json.dump(emails, f, indent=4)
                click.echo(f"Generated emails saved to {output_path}")
            except OSError as e:
                click.echo(
                    f"Error: Could not write to file {output_path}. {e}",
                    err=True,
                )
        else:
            for email in emails:
                click.echo(email)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
