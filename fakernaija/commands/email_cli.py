"""CLI commands for EmailProvider to generate random email addresses."""

import click

from fakernaija.faker import Faker

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
def email(repeat: int, tribe: str, gender: str, domain: str) -> None:
    """Return random Nigerian email addresses.

    This command generates random Nigerian email addresses.

    Args:
        repeat (int): The number of random email addresses to return.
        tribe (str): The tribe to generate names from (yoruba, igbo, hausa, edo, fulani, ijaw).
        gender (str): The specific gender from which the email address will be generated.
        domain (str): A custom domain to use for the email address.

    Examples:
        $ naija email
        $ naija email --repeat 3
        $ naija email --tribe igbo
        $ naija email --gender female
        $ naija email --domain gov.ng
        $ naija email --repeat 5 --tribe yoruba --gender male --domain unilag.edu.ng
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    # Normalize tribe and gender to lowercase if they are provided
    tribe = tribe.lower() if tribe else None
    gender = gender.lower() if gender else None

    try:
        for _ in range(repeat):
            email = naija.email(tribe=tribe, gender=gender, domain=domain)
            if email:
                click.echo(email)
            else:
                click.echo("Error: Failed to generate email address.", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
