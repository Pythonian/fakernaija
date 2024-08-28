"""School commands to return random Nigerian schools data."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random schools to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--ownership",
    "-o",
    default=None,
    help="Filter schools by ownership.",
    type=click.Choice(["federal", "state", "private"], case_sensitive=False),
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Filter schools by any state in Nigeria.",
    type=str,
)
@click.option(
    "--school_type",
    "-t",
    default=None,
    help="Filter schools by type.",
    type=click.Choice(
        ["university", "polytechnic", "college"],
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
def school(
    repeat: int,
    ownership: str,
    state: str,
    school_type: str,
    output: str,
) -> None:
    """Return random school objects.

    Args:
        repeat (int): The number of random school objects to return. Must be
            a positive integer. Defaults to 1.
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        output (str): The format of the output file if provided.

    Note:
        - Ownership options: federal, state, private
        - School type options: university, polytechnic, college
        - State options: 36 states in Nigeria + FCT
        - Output options: csv, json, text

    Examples:
        To return a single random school object:

        .. code-block:: console

            $ naija school
            {'name': 'Fidei Polytechnic', 'acronym': 'FIDEIPOLY', 'state': 'Benue', 'type': 'Polytechnic', 'ownership': 'Private'}

        To return 3 random school objects:

        .. code-block:: console

            $ naija school --repeat 3
            {'name': 'Federal Polytechnic Bali', 'acronym': 'FEDPOLYBALI', 'state': 'Taraba', 'type': 'Polytechnic', 'ownership': 'Federal'}
            {'name': 'Federal University of Petroleum Resources, Effurun', 'acronym': 'FUPRE', 'state': 'Delta', 'type': 'University', 'ownership': 'Federal'}
            {'name': 'Nnamdi Azikiwe University', 'acronym': 'UNIZIK', 'state': 'Anambra', 'type': 'University', 'ownership': 'Federal'}

        To return a random school object filtered by ownership:

        .. code-block:: console

            $ naija school --ownership private
            {'name': 'Ajayi Crowther University', 'acronym': 'ACU', 'state': 'Oyo', 'type': 'University', 'ownership': 'Private'}

        To return a random school object filtered by school type:

        .. code-block:: console

            $ naija school --school_type college
            {'name': 'Federal College of Education, Zaria', 'acronym': 'FCEZARIA', 'state': 'Kaduna', 'type': 'College', 'ownership': 'Federal'}

        To return a random school object from a specific state in Nigeria:

        .. code-block:: console

            $ naija school --state abuja
            {'name': 'University of Abuja', 'acronym': 'UNIABUJA', 'state': 'Abuja', 'type': 'University', 'ownership': 'Federal'}

        To return 3 random school objects filtered by ownership, school type and state:

        .. code-block:: console

            $ naija school --ownership private --state ogun --school_type university -r 3
            {'name': 'Babcock University', 'acronym': 'BU', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}
            {'name': 'Covenant University', 'acronym': 'CU', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}
            {'name': 'Bells University of Technology', 'acronym': 'BELLSTECH', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}

        To return 30 random school objects and save them to a specified format:

        .. code-block:: bash

            $ naija school --repeat 30 --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.school,
        ownership=ownership,
        state=state,
        school_type=school_type,
    )
    if data:
        handle_command_output(data, output, "schools", "schools")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random school names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--acronym",
    "-a",
    is_flag=True,
    help="Return the school's acronym instead of the full name.",
)
@click.option(
    "--ownership",
    "-o",
    default=None,
    help="Filter schools by ownership.",
    type=click.Choice(["federal", "state", "private"], case_sensitive=False),
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Filter schools by any state in Nigeria.",
    type=str,
)
@click.option(
    "--school_type",
    "-t",
    default=None,
    help="Filter schools by type.",
    type=click.Choice(
        ["university", "polytechnic", "college"],
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
def school_name(  # noqa: PLR0913
    repeat: int,
    acronym: bool,
    ownership: str,
    state: str,
    school_type: str,
    output: str,
) -> None:
    """Return random school names.

    Args:
        repeat (int): The number of random school names to return. Must be
            a positive integer. Defaults to 1.
        acronym (bool): Whether to return the school's acronym instead of the full name.
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        output (str): The format of the output file if provided.

    Note:
        - Ownership options: federal, state, private
        - School type options: university, polytechnic, college
        - State options: 36 states in Nigeria + FCT
        - Output options: csv, json, text

    Examples:
        To return a single random school name:

        .. code-block:: console

            $ naija school_name
            Federal College of Education, Abeokuta

        To return a school acronym instead of the full name:

        .. code-block:: console

            $ naija school_name --acronym
            UNN

        To return 3 random school names:

        .. code-block:: console

            $ naija school_name -r 3
            Federal College of Education (Technical), Gombe
            Federal University of Technology, Akure
            Best Legacy College of Education

        To return a random school name filtered by ownership:

        .. code-block:: console

            $ naija school_name --ownership private
            Bells University of Technology

        To return a random school name filtered by school type:

        .. code-block:: console

            $ naija school_name --school_type college
            Abia State College of Education (Technical), Arochukwu

        To return a random school name from a specific state in Nigeria:

        .. code-block:: console

            $ naija school_name --state "akwa ibom"
            University of Uyo

        To return 3 random private universities in Ogun:

        .. code-block:: console

            $ naija school_name --school_type university --ownership private --state ogun --repeat 3
            Babcock University
            Bells University of Technology
            Covenant University

        To return 30 random school names and save them to a specified format:

        .. code-block:: bash

            $ naija school_name --repeat 30 --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.school_name,
        acronym=acronym,
        ownership=ownership,
        state=state,
        school_type=school_type,
    )
    if data:
        handle_command_output(data, output, "schools", "schools")
