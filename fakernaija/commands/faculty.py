"""Faculty commands to return random Nigerian schools faculty and department data."""

import click

from fakernaija import Faker
from fakernaija.utils import generate_command_data, handle_command_output

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random faculty objects to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def faculty(repeat: int, output: str) -> None:
    """Returns random faculty objects.

    Args:
        repeat (int): The number of random faculty objects to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single random faculty:

        .. code-block:: console

            $ naija faculty
            {'faculty_name': 'Medicine and Dentistry', 'departments': ['Bachelor of Medicine and Bachelor of Surgery', 'Dentistry']}

        To return 3 random faculty objects:

        .. code-block:: console

            $ naija faculty --repeat 3
            {'faculty_name': 'Basic Medical Sciences', 'departments': ['Human Anatomy', 'Physiology']}
            {'faculty_name': 'Medicine and Dentistry', 'departments': ['Bachelor of Medicine and Bachelor of Surgery', 'Dentistry']}
            {'faculty_name': 'Computing', 'departments': ['Cybersecurity', 'Software Engineering', 'Data Science', 'Information and Communications Technology', 'Information Technology', 'Information System', 'Computer Science']}

        To return 30 random faculty objects and save them to a specified format:

        .. code-block:: bash

            $ naija faculty --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.faculty)
    if data:
        handle_command_output(data, output, "faculties", "faculties")


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
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def faculty_name(repeat: int, output: str) -> None:
    """Returns random faculty names.

    Args:
        repeat (int): The number of random faculty names to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single faculty name:

        .. code-block:: console

            $ naija faculty_name
            Allied Health Sciences

        To return 3 random faculty names:

        .. code-block:: console

            $ naija faculty_name --repeat 3
            Law
            Allied Health Sciences
            Medicine and Dentistry

        To return 30 random faculty names and save them to a specified format:

        .. code-block:: bash

            $ naija faculty_name --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.faculty_name)
    if data:
        handle_command_output(data, output, "faculty_name", "faculties")


@click.command()
@click.option(
    "--faculty",
    "-f",
    default=None,
    help="Name of the faculty to return departments from.",
)
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random department names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def department_name(repeat: int, faculty: str, output: str) -> None:
    """Returns random department names.

    Args:
        repeat (int): The number of random department names to return.
            Must be a positive integer. Defaults to 1.
        faculty (str): The specific faculty name to return departments from.
            Defaults to None.
        output (str): The format of the output file if provided.

    Raises:
        ValueError: If the given faculty name is invalid.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single department name:

        .. code-block:: console

            $ naija department_name
            Computer Science

        To return 3 random department names:

        .. code-block:: console

            $ naija department_name --repeat 3
            Physiology
            Logistics and Supply Chain Management
            Health Information Management

        To return a single department by faculty name:

        .. code-block:: console

            $ naija department_name --faculty 'Basic Medical Sciences'
            Human Anatomy

        To return 3 random departments by faculty name:

        .. code-block:: console

            $ naija department_name --faculty 'computing' --repeat 3
            Computer Science
            Information and Communications Technology
            Data Science

        To return 30 random department names and save them to a specified format:

        .. code-block:: bash

            $ naija department_name --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.department_name, faculty=faculty)
    if data:
        handle_command_output(data, output, "department_name", "departments")
