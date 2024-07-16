"""CLI commands for FacultyProvider to generate random faculty and department."""

from pathlib import Path

import click

from fakernaija.faker import Faker
from fakernaija.utils import get_unique_filename, write_data_to_file

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
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv", "xml"], case_sensitive=False),
)
def faculty_name(repeat: int, output: str) -> None:
    """Return random faculty names.

    This command generates random Nigerian school faculty names.

    Args:
        repeat (int): The number of random faculty names to return.
        output (str): The format of the output file.

    Examples:
        $ naija faculty_name
        $ naija faculty_name --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    faculty_names = []

    for _ in range(repeat):
        faculty_name = naija.faculty_name()
        if faculty_name:
            faculty_names.append(faculty_name)
        else:
            click.echo("Error: Failed to generate faculty name.", err=True)

    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
            "xml": ".xml",
        }

        base_filename = Path(f"faculty_names{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(faculty_names, output_path, output, "faculty_name")

    else:
        for faculty_name in faculty_names:
            click.echo(faculty_name)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random departments to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv", "xml"], case_sensitive=False),
)
def department(repeat: int, output: str) -> None:
    """Return random departments.

    This command generates random Nigerian school departments.

    Args:
        repeat (int): The number of random departments to return.
        output (str): The format of the output file.

    Examples:
        $ naija department
        $ naija department --repeat 3
        $ naija department -r 30 -o text
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    departments = []

    for _ in range(repeat):
        department = naija.department()
        if department:
            departments.append(department)
        else:
            click.echo("Error: Failed to generate department.", err=True)

    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
            "xml": ".xml",
        }

        base_filename = Path(f"departments{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(departments, output_path, output, "department")

    else:
        for department in departments:
            click.echo(department)


@click.command()
@click.argument("faculty")
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random departments to return from the specified faculty. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv", "xml"], case_sensitive=False),
)
def department_by_faculty(faculty: str, repeat: int, output: str) -> None:
    """Return random departments from a specified faculty.

    This command generates random Nigerian school departments from a specified faculty.

    Args:
        faculty (str): The name of the faculty.
        repeat (int): The number of random departments to return.
        output (str): The format of the output file.

    Examples:
        $ naija department_by_faculty 'Basic Medical Sciences'
        $ naija department_by_faculty 'Basic Medical Sciences' --repeat 3
        $ naija department_by_faculty 'Basic Medical Sciences' -o json -r 10
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    departments = []

    try:
        for _ in range(repeat):
            department = naija.department_by_faculty(faculty)
            if department:
                departments.append(department)
            else:
                click.echo("Error: Failed to generate department.", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)

    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
            "xml": ".xml",
        }

        base_filename = Path(f"departments_by_faculty{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(departments, output_path, output, "department_by_faculty")

    else:
        for department in departments:
            click.echo(department)
