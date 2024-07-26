"""CLI commands for NameProvider to generate random Nigerian names."""

import click

from fakernaija.faker import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="The gender for the name.",
    type=click.Choice(["male", "female"]),
)
@click.option(
    "--middlename",
    "-m",
    is_flag=True,
    help="Include middle name to the full name.",
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe choice for the name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def fullname(
    repeat: int,
    gender: str,
    middlename: bool,
    tribe: str,
) -> None:
    """Return random full names.

    This command generates random Nigerian full names.

    Args:
        repeat (int): The number of random names to return.
        gender (str): The gender from which the name should be generated.
        middlename (bool): If set, include a middle name to the full name.
        tribe (str): The tribe from which the name should be generated.

    Examples:
        $ naija fullname
        $ naija fullname --repeat 3
        $ naija fullname --middlename
        $ naija fullname --tribe igbo
        $ naija fullname --gender female
        $ naija fullname --tribe yoruba --repeat 2 --gender female --middlename
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        if tribe and gender:
            if gender == "male":
                fullname = naija.full_name_tribe(tribe, middle_name=middlename)
            else:
                fullname = naija.full_name_tribe(tribe, middle_name=middlename)
        elif tribe:
            fullname = naija.full_name_tribe(tribe, middle_name=middlename)
        elif gender:
            if gender == "male":
                fullname = naija.male_full_name(middle_name=middlename)
            else:
                fullname = naija.female_full_name(middle_name=middlename)
        else:
            fullname = naija.full_name(middle_name=middlename)

        if fullname:
            click.echo(fullname)
        else:
            click.echo("Error: Failed to generate fullname.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="The gender for the name.",
    type=click.Choice(["male", "female"]),
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe choice for the name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def firstname(repeat: int, tribe: str, gender: str) -> None:
    """Return random first names.

    This command generates random Nigerian first names.

    Args:
        repeat (int): The number of random names to return.
        tribe (str): The tribe from which the name should be generated.
        gender (str): The gender from which the name should be generated.

    Examples:
        $ naija firstname
        $ naija firstname --repeat 3
        $ naija firstname --tribe igbo
        $ naija firstname --gender female
        $ naija firstname --tribe yoruba --repeat 2 --gender female
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        if tribe and gender:
            if gender == "male":
                firstname = naija.male_first_name_tribe(tribe)
            else:
                firstname = naija.female_first_name_tribe(tribe)
        elif tribe:
            firstname = naija.first_name_tribe(tribe)
        elif gender:
            if gender == "male":
                firstname = naija.male_first_name()
            else:
                firstname = naija.female_first_name()
        else:
            firstname = naija.first_name()

        if firstname:
            click.echo(firstname)
        else:
            click.echo("Error: Failed to generate firstname.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe choice for the name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def lastname(repeat: int, tribe: str) -> None:
    """Return random last names.

    This command generates random Nigerian last names.

    Args:
        repeat (int): The number of random names to return.
        tribe (str): The tribe from which the name should be generated.

    Examples:
        $ naija lastname
        $ naija lastname --repeat 3
        $ naija lastname --tribe igbo
        $ naija lastname --tribe yoruba --repeat 2
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        lastname = naija.last_name_tribe(tribe) if tribe else naija.last_name()

        if lastname:
            click.echo(lastname)
        else:
            click.echo("Error: Failed to generate last name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random prefixes to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--gender",
    "-g",
    type=click.Choice(["male", "female"], case_sensitive=False),
    help="Specify the gender for the prefix.",
)
def prefix(repeat: int, gender: str | None) -> None:
    """Return random prefixes.

    This command generates random name prefixes and honorifics.

    Args:
        repeat (int): The number of random prefixes to return.
        gender (str, optional): The gender for the prefix.

    Examples:
        $ naija prefix
        $ naija prefix --repeat 3
        $ naija prefix --gender male
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        if gender == "male":
            prefix = naija.male_prefix()
        elif gender == "female":
            prefix = naija.female_prefix()
        else:
            prefix = naija.prefix()

        if prefix:
            click.echo(prefix)
        else:
            click.echo("Error: Failed to generate prefix.", err=True)
