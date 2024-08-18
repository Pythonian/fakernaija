"""CLI commands for NameProvider to generate random Nigerian names."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random full names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="The gender for the full name.",
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
    help="The tribe choice for the full name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def fullname(
    repeat: int,
    gender: str,
    middlename: bool,
    tribe: str,
) -> None:
    """Generate and return random full names.

    Args:
        repeat (int): The number of random full names to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender from which the full name should be generated.
        middlename (bool): If set, include a middle name to the full name.
        tribe (str): The tribe from which the full name should be generated.

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

    Examples:
        To generate a single random full name:

        .. code-block:: bash

            $ naija fullname
            Chibunna Ulelu

        To generate 3 random full names:

        .. code-block:: bash

            $ naija fullname --repeat 3
            Kelechi Onyekwere
            Ololade Lawal
            Nasir El-Rufai

        To generate a random full name with middle name:

        .. code-block:: bash

            $ naija fullname --middlename
            Kosisochukwu Somtochukwu Mbakwe

        To generate a random full name from a specific tribe:

        .. code-block:: bash

            $ naija fullname --tribe igbo
            Chisom Nnabude

        To generate a random full name from a specific gender:

        .. code-block:: bash

            $ naija fullname --gender male
            Ebube Madu

        To generate 3 random full names with middle names from a specific tribe and gender

        .. code-block:: bash

            $ naija fullname --tribe yoruba -r 3 --gender female --middlename
            Yetunde Bukola Ogunleye
            Jumoke Tola Olabisi
            Toyin Temitope Lemboye
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        fullname = naija.full_name(
            tribe=tribe,
            gender=gender,
            middle_name=middlename,
        )
        if fullname:
            click.echo(fullname)
        else:
            click.echo("Error: Failed to generate fullname.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random first names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="The gender for the first name.",
    type=click.Choice(["male", "female"]),
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe choice for the first name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def firstname(repeat: int, tribe: str, gender: str) -> None:
    """Generate and return random first names.

    Args:
        repeat (int): The number of random first names to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender from which the first name should be generated.
        tribe (str): The tribe from which the first name should be generated.

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

    Examples:
        To generate a single random first name:

        .. code-block:: bash

            $ naija firstname
            Mmasichukwu

        To generate 3 random first names:

        .. code-block:: bash

            $ naija firstname --repeat 3
            Ebuka
            Ololade
            Bashir

        To generate a random first name from a specific tribe:

        .. code-block:: bash

            $ naija firstname --tribe edo
            Osamagbe

        To generate a random first name from a specific gender:

        .. code-block:: bash

            $ naija firstname --gender male
            Seyi

        To generate 3 random first names from a specific tribe and gender

        .. code-block:: bash

            $ naija firstname --tribe hausa --repeat 3 --gender female
            Amina
            Aisha
            Falmata
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        firstname = naija.first_name(tribe=tribe, gender=gender)
        if firstname:
            click.echo(firstname)
        else:
            click.echo("Error: Failed to generate firstname.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random last names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe choice for the last name.",
    type=click.Choice(["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]),
)
def lastname(repeat: int, tribe: str) -> None:
    """Generate and return random last names.

    Args:
        repeat (int): The number of random last names to return.
            Must be a positive integer. Defaults to 1.
        tribe (str): The tribe from which the last name should be generated.

    Note:
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

    Examples:
        To generate a single random last name:

        .. code-block:: bash

            $ naija lastname
            Nwodo

        To generate 3 random last names:

        .. code-block:: bash

            $ naija lastname --repeat 3
            Eze
            Bello
            Okonkwo

        To generate a random last name from a specific tribe:

        .. code-block:: bash

            $ naija lastname --tribe edo
            Osagie

        To generate 3 random last names from a specific tribe

        .. code-block:: bash

            $ naija lastname --tribe ijaw -r 3
            Ebiere
            Opobo
            Oweipade
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        lastname = naija.last_name(tribe=tribe)
        if lastname:
            click.echo(lastname)
        else:
            click.echo("Error: Failed to generate lastname.", err=True)


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
@click.option(
    "--title",
    "-t",
    type=click.Choice(["traditional", "professional"], case_sensitive=False),
    help="Specify the title for the prefix.",
)
def prefix(repeat: int, gender: str | None, title: str | None) -> None:
    """Generate and return random prefixes.

    Args:
        repeat (int): The number of random prefixes to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender for the prefix.
        title (str): The title for the prefix.

    Note:
        - Gender options: male, female
        - Title options: traditional, professional

    Examples:
        To generate a single random prefix:

        .. code-block:: bash

            $ naija prefix
            Mr.

        To generate 3 random prefixes:

        .. code-block:: bash

            $ naija prefix --repeat 3
            Otunba
            Waziri
            Dr.

        To generate a random prefix from a specific gender:

        .. code-block:: bash

            $ naija prefix --gender male
            Prince

        To generate a random prefix from a specific title:

        .. code-block:: bash

            $ naija prefix --title professional
            Engr.

        To generate 3 random prefixes from a specific title and gender

        .. code-block:: bash

            $ naija prefix -r 3 --title traditional --gender female
            Lady (Mrs.)
            Lolo
            Princess
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        prefix = naija.prefix(gender=gender, title=title)
        if prefix:
            click.echo(prefix)
        else:
            click.echo("Error: Failed to generate prefix.", err=True)
