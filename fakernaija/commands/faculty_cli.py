"""CLI commands for FacultyProvider to generate random faculty and department."""

import click

from fakernaija.faker import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random faculties to return. Defaults to 1.",
    type=int,
)
def faculty(repeat: int) -> None:
    """Return random faculties.

    This command generates random Nigerian school faculties.

    Args:
        repeat (int): The number of random faculties to return.

    Examples:
        $ naija faculty
        $ naija faculty --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        faculty = naija.faculty()
        click.echo(faculty)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random departments to return. Defaults to 1.",
    type=int,
)
def department(repeat: int) -> None:
    """Return random departments.

    This command generates random Nigerian school departments.

    Args:
        repeat (int): The number of random departments to return.

    Examples:
        $ naija department
        $ naija department --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        department = naija.department()
        if department:
            click.echo(department)
        else:
            click.echo("Error: Failed to generate department.", err=True)
