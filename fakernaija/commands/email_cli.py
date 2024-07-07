"""CLI commands for EmailProvider to generate random email addresses."""

import csv
import json
from pathlib import Path

import click

from fakernaija.faker import Faker

naija = Faker()


def get_unique_filename(base_path: Path) -> Path:
    """Generate a unique file name by appending numbers if the file exists."""
    counter = 1
    unique_path = base_path
    while unique_path.exists():
        unique_path = base_path.with_stem(f"{base_path.stem}_{counter}")
        counter += 1
    return unique_path


def write_emails_to_file(emails: list[str], output_path: Path, output: str) -> None:
    """Write emails to file in specified format."""
    try:
        if output == "json":
            with output_path.open("w") as f:
                json.dump(emails, f, indent=4)
        elif output == "csv":
            with output_path.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Emails"])
                for email in emails:
                    writer.writerow([email])
        elif output == "text":
            with output_path.open("w") as f:
                for email in emails:
                    f.write(email + "\n")
        click.echo(f"Generated emails saved to {output_path}")
    except OSError as e:
        click.echo(f"Error: Could not write to file {output_path}. {e}", err=True)


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
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
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
            }

            base_filename = Path(f"emails{file_extensions[output]}")
            output_path = get_unique_filename(Path.cwd() / base_filename)
            write_emails_to_file(emails, output_path, output)

        else:
            for email in emails:
                click.echo(email)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
