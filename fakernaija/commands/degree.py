"""Degree commands to return random Nigerian schools degree data."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degree objects to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(
        ["undergraduate", "masters", "doctorate"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def degree(repeat: int, degree_type: str | None, output: str) -> None:
    """Returns random degree objects.

    Args:
        repeat (int): The number of random degree objects to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.
        output (str): The format of the output file if provided.

    Note:
        - Degree type options: undergraduate, masters, doctorate
        - Output options: csv, json, text

    Examples:
        To return a single random degree object:

        .. code-block:: console

            $ naija degree
            {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}

        To return a random degree object by degree type:

        .. code-block:: console

            $ naija degree --degree-type undergraduate
            {'name': 'Bachelor of Medicine, Bachelor of Surgery', 'degree_type': 'undergraduate', 'abbr': 'MBBS'}

        To return 3 random degree objects:

        .. code-block:: console

            $ naija degree --repeat 3
            {'name': 'Doctor of Education', 'degree_type': 'doctorate', 'abbr': 'Ed.D.'}
            {'name': 'Bachelor of Nursing Science', 'degree_type': 'undergraduate', 'abbr': 'B.N.Sc.'}
            {'name': 'Master of Education', 'degree_type': 'masters', 'abbr': 'M.Ed.'}

        To return 30 random degree objects and save them to a specified format:

        .. code-block:: bash

            $ naija degree --repeat 30 --degree-type undergraduate --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.degree, degree_type=degree_type)
    if data:
        handle_command_output(data, output, "degrees", "degrees")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degree names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(
        ["undergraduate", "masters", "doctorate"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def degree_name(repeat: int, degree_type: str | None, output: str) -> None:
    """Returns random degree names.

    Args:
        repeat (int): The number of random degree names to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.
        output (str): The format of the output file if provided.

    Note:
        - Degree type options: undergraduate, masters, doctorate
        - Output options: csv, json, text

    Examples:
        To return a single random degree name:

        .. code-block:: console

            $ naija degree_name
            Bachelor of Law

        To return 3 random random degree names:

        .. code-block:: console

            $ naija degree_name --repeat 3
            Bachelor of Technology
            Bachelor of Education
            Master of Urban and Regional Planning

        To return a random degree name by degree type:

        .. code-block:: console

            $ naija degree_name --degree-type undergraduate
            Bachelor of Medicine, Bachelor of Surgery

        To return 30 random degree names and save them to a specified format:

        .. code-block:: bash

            $ naija degree_name --repeat 30 --degree-type undergraduate --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.degree_name, degree_type=degree_type)
    if data:
        handle_command_output(data, output, "degree_names", "degree names")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degree abbreviations to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(
        ["undergraduate", "masters", "doctorate"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def degree_abbr(repeat: int, degree_type: str | None, output: str) -> None:
    """Returns random degree abbreviations.

    Args:
        repeat (int): The number of random degree abbreviations to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.
        output (str): The format of the output file if provided.

    Note:
        - Degree type options: undergraduate, masters, doctorate
        - Output options: csv, json, text

    Examples:
        To return a single random degree abbreviation:

        .. code-block:: console

            $ naija degree_abbr
            B.Pharm.

        To return 3 random random degree abbreviations:

        .. code-block:: console

            $ naija degree_abbr --repeat 3
            MBBS
            LL.M.
            B.Sc.

        To return a random degree abbreviation by degree type:

        .. code-block:: console

            $ naija degree_abbr --degree-type masters
            M.Eng.

        To return 30 random degree abbrs and save them to a specified format:

        .. code-block:: bash

            $ naija degree_abbr --repeat 30 --degree-type undergraduate --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.degree_abbr, degree_type=degree_type)
    if data:
        handle_command_output(data, output, "degree_abbrs", "degree abbreviations")
