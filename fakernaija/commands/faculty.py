"""CLI commands for FacultyProvider to generate random faculty and department."""

import click

from fakernaija import Faker

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
        if faculty:
            click.echo(faculty)
            click.echo()
        else:
            click.echo("Error: Failed to generate faculty.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random faculty names to return. Defaults to 1.",
    type=int,
)
def faculty_name(repeat: int) -> None:
    """Return random faculty names.

    This command generates random Nigerian school faculty names.

    Args:
        repeat (int): The number of random faculty names to return.

    Examples:
        $ naija faculty_name
        $ naija faculty_name --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        faculty_name = naija.faculty_name()
        if faculty_name:
            click.echo(faculty_name)
        else:
            click.echo("Error: Failed to generate faculty name.", err=True)


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
        department = naija.department_name()
        if department:
            click.echo(department)
        else:
            click.echo("Error: Failed to generate department.", err=True)


@click.command()
@click.argument("faculty")
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random departments to return from the specified faculty. Defaults to 1.",
    type=int,
)
def department_by_faculty(faculty: str, repeat: int) -> None:
    """Return random departments from a specified faculty.

    This command generates random Nigerian school departments from a specified faculty.

    Args:
        faculty (str): The name of the faculty.
        repeat (int): The number of random departments to return.

    Examples:
        $ naija department_by_faculty 'Basic Medical Sciences'
        $ naija department_by_faculty 'Basic Medical Sciences' --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        for _ in range(repeat):
            department = naija.department_by_faculty(faculty)
            if department:
                click.echo(department)
            else:
                click.echo("Error: Failed to generate department.", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
