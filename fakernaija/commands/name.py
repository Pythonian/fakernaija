"""Name commands to generate and return random Nigerian names."""

import click

from fakernaija import Faker
from fakernaija.utils import generate_command_data, handle_command_output

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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def full_name(
    repeat: int,
    gender: str,
    middlename: bool,
    tribe: str,
    output: str,
) -> None:
    """Generate and return random full names.

    Args:
        repeat (int): The number of random full names to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender from which the full name should be generated.
        middlename (bool): If set, include a middle name to the full name.
        tribe (str): The tribe from which the full name should be generated.
        output (str): The format of the output file if provided.

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
        - Output options: csv, json, text

    Examples:
        To generate a single random full name:

        .. code-block:: console

            $ naija full_name
            Chibunna Ulelu

        To generate 3 random full names:

        .. code-block:: console

            $ naija full_name --repeat 3
            Kelechi Onyekwere
            Ololade Lawal
            Nasir El-Rufai

        To generate a random full name with middle name:

        .. code-block:: console

            $ naija full_name --middlename
            Kosisochukwu Somtochukwu Mbakwe

        To generate a random full name from a specific tribe:

        .. code-block:: console

            $ naija full_name --tribe igbo
            Chisom Nnabude

        To generate a random full name from a specific gender:

        .. code-block:: console

            $ naija full_name --gender male
            Ebube Madu

        To generate 3 random full names with middle names from a specific tribe and gender

        .. code-block:: console

            $ naija full_name --tribe yoruba -r 3 --gender female --middlename
            Yetunde Bukola Ogunleye
            Jumoke Tola Olabisi
            Toyin Temitope Lemboye

        To generate 30 random full names and save them to a specified format:

        .. code-block:: bash

            $ naija full_name --repeat 30 --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.full_name,
        tribe=tribe,
        gender=gender,
        middle_name=middlename,
    )
    if data:
        handle_command_output(data, output, "full_name", "full names")


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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def first_name(
    repeat: int,
    tribe: str,
    gender: str,
    output: str,
) -> None:
    """Generate and return random first names.

    Args:
        repeat (int): The number of random first names to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender from which the first name should be generated.
        tribe (str): The tribe from which the first name should be generated.
        output (str): The format of the output file if provided.

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
        - Output options: csv, json, text

    Examples:
        To generate a single random first name:

        .. code-block:: console

            $ naija first_name
            Mmasichukwu

        To generate 3 random first names:

        .. code-block:: console

            $ naija first_name --repeat 3
            Ebuka
            Ololade
            Muhammed

        To generate a random first name from a specific tribe:

        .. code-block:: console

            $ naija first_name --tribe edo
            Osamagbe

        To generate a random first name from a specific gender:

        .. code-block:: console

            $ naija first_name --gender male
            Seyi

        To generate 3 random first names from a specific tribe and gender

        .. code-block:: console

            $ naija first_name --tribe hausa --repeat 3 --gender female
            Amina
            Aisha
            Falmata

        To generate 30 random first names and save them to a specified format:

        .. code-block:: bash

            $ naija first_name --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.first_name,
        tribe=tribe,
        gender=gender,
    )
    if data:
        handle_command_output(data, output, "first_name", "first names")


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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def last_name(repeat: int, tribe: str, output: str) -> None:
    """Generate and return random last names.

    Args:
        repeat (int): The number of random last names to return.
            Must be a positive integer. Defaults to 1.
        tribe (str): The tribe from which the last name should be generated.
        output (str): The format of the output file if provided.

    Note:
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
        - Output options: csv, json, text

    Examples:
        To generate a single random last name:

        .. code-block:: console

            $ naija last_name
            Nwodo

        To generate 3 random last names:

        .. code-block:: console

            $ naija last_name --repeat 3
            Eze
            Bello
            Okonkwo

        To generate a random last name from a specific tribe:

        .. code-block:: console

            $ naija last_name --tribe edo
            Osagie

        To generate 3 random last names from a specific tribe

        .. code-block:: console

            $ naija last_name --tribe ijaw -r 3
            Ebiere
            Opobo
            Oweipade

        To generate 30 random last names and save them to a specified format:

        .. code-block:: bash

            $ naija last_name --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.last_name,
        tribe=tribe,
    )
    if data:
        handle_command_output(data, output, "last_name", "last names")


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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def prefix(repeat: int, gender: str, title: str, output: str) -> None:
    """Returns random name prefixes.

    Args:
        repeat (int): The number of random name prefixes to return.
            Must be a positive integer. Defaults to 1.
        gender (str): The gender for the prefix.
        title (str): The title for the prefix.
        output (str): The format of the output file if provided.

    Note:
        - Gender options: male, female
        - Title options: traditional, professional
        - Output options: csv, json, text

    Examples:
        To return a single random prefix:

        .. code-block:: console

            $ naija prefix
            Mr.

        To return 3 random prefixes:

        .. code-block:: console

            $ naija prefix --repeat 3
            Otunba
            Waziri
            Dr.

        To return a random prefix from a specific gender:

        .. code-block:: console

            $ naija prefix --gender male
            Prince

        To return a random prefix from a specific title:

        .. code-block:: console

            $ naija prefix --title professional
            Engr.

        To return 3 random prefixes from a specific title and gender

        .. code-block:: console

            $ naija prefix -r 3 --title traditional --gender female
            Lady (Mrs.)
            Lolo
            Princess

        To generate 30 random prefixes and save them to a specified format:

        .. code-block:: bash

            $ naija prefix --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.prefix,
        gender=gender,
        title=title,
    )
    if data:
        handle_command_output(data, output, "prefix", "prefixes")
