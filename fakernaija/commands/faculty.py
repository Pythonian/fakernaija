"""CLI commands for FacultyProvider to return random faculty and department."""

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
    """Return random Nigerian school faculties.

    Args:
        repeat (int): The number of random faculties to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random faculty:

        .. code-block:: bash

            $ naija faculty
            {'faculty_name': 'Medicine and Dentistry', 'departments': ['Bachelor of Medicine and Bachelor of Surgery', 'Dentistry']}

        To return 3 random faculties:

        .. code-block:: bash

            $ naija faculty --repeat 3
            {'faculty_name': 'Basic Medical Sciences', 'departments': ['Human Anatomy', 'Physiology']}

            {'faculty_name': 'Medicine and Dentistry', 'departments': ['Bachelor of Medicine and Bachelor of Surgery', 'Dentistry']}

            {'faculty_name': 'Computing', 'departments': ['Cybersecurity', 'Software Engineering', 'Data Science', 'Information and Communications Technology', 'Information Technology', 'Information System', 'Computer Science']}

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
            click.echo("Error: Failed to return faculty.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random faculty names to return. Defaults to 1.",
    type=int,
)
def faculty_name(repeat: int) -> None:
    """Return random Nigerian school faculty names.

    Args:
        repeat (int): The number of random faculty names to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single faculty name:

        .. code-block:: bash

            $ naija faculty_name
            Allied Health Sciences

        To return 3 random faculty names:

        .. code-block:: bash

            $ naija faculty_name --repeat 3
            Law
            Allied Health Sciences
            Medicine and Dentistry
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        faculty_name = naija.faculty_name()
        if faculty_name:
            click.echo(faculty_name)
        else:
            click.echo("Error: Failed to return faculty name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random department names to return. Defaults to 1.",
    type=int,
)
def department_name(repeat: int) -> None:
    """Return random school departments.

    Args:
        repeat (int): The number of random departments to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single department name:

        .. code-block:: bash

            $ naija department_name
            Technology Education

        To return 3 random department names:

        .. code-block:: bash

            $ naija department_name --repeat 3
            Physiology
            Logistics and Supply Chain Management
            Health Information Management
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        department_name = naija.department_name()
        if department_name:
            click.echo(department_name)
        else:
            click.echo("Error: Failed to return department name.", err=True)


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
    """Return random school departments from a specific faculty.

    Args:
        faculty (str): The specific faculty name to return departments from.
        repeat (int): The number of random departments to return.
            Must be an integer. Defaults to 1.

    Raises:
        ValueError: If the given faculty name is invalid.

    Examples:
        To return a single department by faculty name:

        .. code-block:: bash

            $ naija department_by_faculty 'Basic Medical Sciences'
            Human Anatomy

        To return 3 random departments by faculty name:

        .. code-block:: bash

            $ naija department_by_faculty 'computing' --repeat 3
            Computer Science
            Information and Communications Technology
            Data Science
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
                click.echo(
                    "Error: Failed to return department name.",
                    err=True,
                )
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
