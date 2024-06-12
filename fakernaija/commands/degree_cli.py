"""CLI commands for DegreeProvider to generate random Nigerian degrees."""

import click

from fakernaija.faker import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degrees to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--initial",
    "-i",
    is_flag=True,
    help="Return degree initials instead of names.",
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(["undergraduate", "masters", "doctorate"]),
)
def degree(repeat: int, initial: bool, degree_type: str) -> None:
    """Return random degrees.

    This command generates random Nigerian degrees.

    Args:
        repeat (int): The number of random degrees to return.
        initial (bool): If set, return degree initials instead of full names.
        degree_type (str): Type of degree to generate.

    Examples:
        $ naija degree
        $ naija degree --repeat 3
        $ naija degree --initial
        $ naija degree --degree-type masters
        $ naija degree --repeat 3 --initial --degree-type undergraduate
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    if degree_type:
        if degree_type == "undergraduate":
            degrees = [
                naija.undergraduate_degree(initial=initial) for _ in range(repeat)
            ]
        elif degree_type == "masters":
            degrees = [naija.masters_degree(initial=initial) for _ in range(repeat)]
        elif degree_type == "doctorate":
            degrees = [naija.doctorate_degree(initial=initial) for _ in range(repeat)]
        else:
            click.echo(
                "Error: Invalid type. Must be one of 'undergraduate', 'masters', or 'doctorate'.",
            )
    else:
        # Get a random degree type if not specified
        degrees = [naija.degree(initial=initial) for _ in range(repeat)]

    for degree in degrees:
        click.echo(degree)
