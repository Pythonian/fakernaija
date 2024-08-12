"""CLI commands for SchoolProvider to generate random Nigerian schools."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
@click.option(
    "--ownership",
    "-o",
    default=None,
    help="Filter school by ownership.",
    type=click.Choice(["federal", "state", "private"], case_sensitive=False),
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Filter by state.",
    type=str,
)
@click.option(
    "--school_type",
    "-t",
    default=None,
    help="Filter school by school type.",
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

    This command generates random Nigerian schools based on filters.

    Args:
        ownership (str): Filter by ownership ('federal', 'state', 'private').
        state (str): Filter by state.
        school_type (str): Filter by school type ('university', 'polytechnic', 'college').
        repeat (int): The number of random schools to return.

    Examples:
        $ naija school
        $ naija school --ownership federal --state lagos --school_type university --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        school = naija.school(ownership=ownership, state=state, school_type=school_type)
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
    help="Filter school by ownership.",
    type=click.Choice(["federal", "state", "private"], case_sensitive=False),
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Filter by state.",
    type=str,
)
@click.option(
    "--school_type",
    "-t",
    default=None,
    help="Filter school by school type.",
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

    This command generates random Nigerian school names based on filters.

    Args:
        acronym (bool): Return the school's acronym instead of the full name.
        ownership (str): Filter by ownership ('federal', 'state', 'private').
        state (str): Filter by state.
        school_type (str): Filter by school type ('university', 'polytechnic', 'college').
        repeat (int): The number of random school names to return.

    Examples:
        $ naija school_name
        $ naija school_name --acronym
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
