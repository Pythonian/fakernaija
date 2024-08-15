"""CLI commands for SchoolProvider to generate random Nigerian schools."""

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
    help="Filter schools by state.",
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
    """Generate and return random schools.

    Args:
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        repeat (int): The number of random schools to return. Must be a positive integer. Defaults to 1.

    Examples:
        To generate a single random school:

        .. code-block:: bash

            $ naija school

        To generate three random federal universities in Lagos:

        .. code-block:: bash

            $ naija school --ownership federal --state lagos --school_type university --repeat 3
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
        else:
            click.echo("Error: Failed to generate school.", err=True)


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
    help="Filter schools by state.",
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
    """Generate and return random school names.

    Args:
        acronym (bool): Whether to return the school's acronym instead of the full name.
        ownership (str): Filter schools by ownership type.
        state (str): Filter schools by state.
        school_type (str): Filter schools by type.
        repeat (int): The number of random school names to return. Must be a positive integer. Defaults to 1.

    Note:
        - Ownership options: federal, state, private
        - School type options: university, polytechnic, college

    Examples:
        To generate a single random school name:

        .. code-block:: bash

            $ naija school_name
            Federal College of Education, Abeokuta

        To generate a school acronym instead of the full name:

        .. code-block:: bash

            $ naija school_name --acronym
            UNN

        To generate three random federal universities in Lagos:

        .. code-block:: bash

            $ naija school_name --school_type university --ownership federal --state lagos --repeat 3
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
            click.echo("Error: Failed to generate school name.", err=True)
