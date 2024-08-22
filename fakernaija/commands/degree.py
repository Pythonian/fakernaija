"""Degree commands to return random Nigerian schools degree data."""

import click

from fakernaija import Faker

naija = Faker()


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
def degree(repeat: int, degree_type: str | None) -> None:
    """Returns random degree objects.

    Args:
        repeat (int): The number of random degree objects to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.

    Examples:
        To return a single random degree object:

        .. code-block:: bash

            $ naija degree
            {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}

        To return a random degree object by degree type:

        .. code-block:: bash

            $ naija degree --degree-type undergraduate
            {'name': 'Bachelor of Medicine, Bachelor of Surgery', 'degree_type': 'undergraduate', 'abbr': 'MBBS'}

        To return 3 random degree objects:

        .. code-block:: bash

            $ naija degree --repeat 3
            {'name': 'Doctor of Education', 'degree_type': 'doctorate', 'abbr': 'Ed.D.'}

            {'name': 'Bachelor of Nursing Science', 'degree_type': 'undergraduate', 'abbr': 'B.N.Sc.'}

            {'name': 'Master of Education', 'degree_type': 'masters', 'abbr': 'M.Ed.'}
    """
    if repeat < 1:
        click.echo(
            "Error: Repeat count must be a positive integer.",
            err=True,
        )
        return

    for _ in range(repeat):
        degree = naija.degree(degree_type=degree_type)
        if degree:
            click.echo(degree)
            click.echo()
        else:
            click.echo("Error: Failed to return degree object.", err=True)


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
def degree_name(repeat: int, degree_type: str | None) -> None:
    """Returns random degree names.

    Args:
        repeat (int): The number of random degree names to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.

    Examples:
        To return a single random degree name:

        .. code-block:: bash

            $ naija degree_name
            Bachelor of Law

        To return 3 random random degree names:

        .. code-block:: bash

            $ naija degree_name --repeat 3
            Bachelor of Technology
            Bachelor of Education
            Master of Urban and Regional Planning

        To return a random degree name by degree type:

        .. code-block:: bash

            $ naija degree_name --degree-type undergraduate
            Bachelor of Medicine, Bachelor of Surgery
    """
    if repeat < 1:
        click.echo(
            "Error: Repeat count must be a positive integer.",
            err=True,
        )
        return

    for _ in range(repeat):
        degree_name = naija.degree_name(degree_type=degree_type)
        if degree_name:
            click.echo(degree_name)
        else:
            click.echo("Error: Failed to return degree name.", err=True)


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
def degree_abbr(repeat: int, degree_type: str | None) -> None:
    """Returns random degree abbreviations.

    Args:
        repeat (int): The number of random degree abbreviations to return.
            Must be a positive integer. Defaults to 1.
        degree_type (str | None): The type of degree to generate.
            Defaults to any type.

    Examples:
        To return a single random degree abbreviation:

        .. code-block:: bash

            $ naija degree_abbr
            B.Pharm.

        To return 3 random random degree abbreviations:

        .. code-block:: bash

            $ naija degree_abbr --repeat 3
            MBBS
            LL.M.
            B.Sc.

        To return a random degree abbreviation by degree type:

        .. code-block:: bash

            $ naija degree_abbr --degree-type masters
            M.Eng.
    """
    if repeat < 1:
        click.echo(
            "Error: Repeat count must be a positive integer.",
            err=True,
        )
        return

    for _ in range(repeat):
        degree_abbr = naija.degree_abbr(degree_type=degree_type)
        if degree_abbr:
            click.echo(degree_abbr)
        else:
            click.echo(
                "Error: Failed to return degree abbreviation.",
                err=True,
            )
