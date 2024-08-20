"""CLI commands for SchoolProvider to return random Nigerian schools."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
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
    type=click.Choice(["university", "polytechnic", "college"], case_sensitive=False),
)
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random schools to return. Defaults to 1.",
    type=int,
)
def school(ownership: str, state: str, school_type: str, repeat: int) -> None:
    """Return random schools.

    Args:
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        repeat (int): The number of random schools to return. Must be
            a positive integer. Defaults to 1.

    Note:
        - Ownership options: federal, state, private
        - School type options: university, polytechnic, college
        - State options: 36 states in Nigeria + FCT

    Examples:
        To return a single random school:

        .. code-block:: bash

            $ naija school
            {'name': 'Fidei Polytechnic', 'acronym': 'FIDEIPOLY', 'state': 'Benue', 'type': 'Polytechnic', 'ownership': 'Private'}

        To return 3 random schools:

        .. code-block:: bash

            $ naija school --repeat 3
            {'name': 'Federal Polytechnic Bali', 'acronym': 'FEDPOLYBALI', 'state': 'Taraba', 'type': 'Polytechnic', 'ownership': 'Federal'}

            {'name': 'Federal University of Petroleum Resources, Effurun', 'acronym': 'FUPRE', 'state': 'Delta', 'type': 'University', 'ownership': 'Federal'}

            {'name': 'Nnamdi Azikiwe University', 'acronym': 'UNIZIK', 'state': 'Anambra', 'type': 'University', 'ownership': 'Federal'}

        To return a random school filtered by ownership:

        .. code-block:: bash

            $ naija school --ownership private
            {'name': 'Ajayi Crowther University', 'acronym': 'ACU', 'state': 'Oyo', 'type': 'University', 'ownership': 'Private'}

        To return a random school filtered by school type:

        .. code-block:: bash

            $ naija school --school_type college
            {'name': 'Federal College of Education, Zaria', 'acronym': 'FCEZARIA', 'state': 'Kaduna', 'type': 'College', 'ownership': 'Federal'}

        To return a random school from a specific state in Nigeria:

        .. code-block:: bash

            $ naija school --state abuja
            {'name': 'University of Abuja', 'acronym': 'UNIABUJA', 'state': 'Abuja', 'type': 'University', 'ownership': 'Federal'}

        To return 3 random private universities in Ogun:

        .. code-block:: bash

            $ naija school --ownership private --state ogun --school_type university -r 3
            {'name': 'Babcock University', 'acronym': 'BU', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}

            {'name': 'Covenant University', 'acronym': 'CU', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}

            {'name': 'Bells University of Technology', 'acronym': 'BELLSTECH', 'state': 'Ogun', 'type': 'University', 'ownership': 'Private'}
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        school = naija.school(
            ownership=ownership,
            state=state,
            school_type=school_type,
        )
        if school:
            click.echo(school)
            click.echo()
        else:
            click.echo("Error: Failed to return school.", err=True)


@click.command()
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
    type=click.Choice(["university", "polytechnic", "college"], case_sensitive=False),
)
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random school names to return. Defaults to 1.",
    type=int,
)
def school_name(
    acronym: bool,
    ownership: str,
    state: str,
    school_type: str,
    repeat: int,
) -> None:
    """Return random school names.

    Args:
        acronym (bool): Whether to return the school's acronym instead of the full name.
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        repeat (int): The number of random school names to return. Must be
            a positive integer. Defaults to 1.

    Note:
        - Ownership options: federal, state, private
        - School type options: university, polytechnic, college
        - State options: 36 states in Nigeria + FCT

    Examples:
        To return a single random school name:

        .. code-block:: bash

            $ naija school_name
            Federal College of Education, Abeokuta

        To return a school acronym instead of the full name:

        .. code-block:: bash

            $ naija school_name --acronym
            UNN

        To return 3 random school names:

        .. code-block:: bash

            $ naija school_name -r 3
            Federal College of Education (Technical), Gombe
            Federal University of Technology, Akure
            Best Legacy College of Education

        To return a random school name filtered by ownership:

        .. code-block:: bash

            $ naija school_name --ownership private
            Bells University of Technology

        To return a random school name filtered by school type:

        .. code-block:: bash

            $ naija school_name --school_type college
            Abia State College of Education (Technical), Arochukwu

        To return a random school name from a specific state in Nigeria:

        .. code-block:: bash

            $ naija school_name --state "akwa ibom"
            University of Uyo

        To return 3 random private universities in Ogun:

        .. code-block:: bash

            $ naija school_name --school_type university --ownership private --state ogun --repeat 3
            Babcock University
            Bells University of Technology
            Covenant University
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        school_name = naija.school_name(
            acronym=acronym,
            ownership=ownership,
            state=state,
            school_type=school_type,
        )
        if school_name:
            click.echo(school_name)
        else:
            click.echo("Error: Failed to return school name.", err=True)
