"""CLI commands for CourseProvider to generate random Nigerian courses."""

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
    help="Number of random courses to return. Defaults to 1.",
    type=int,
)
def course(repeat: int) -> None:
    """Return random courses.

    This command generates random Nigerian courses.

    Args:
        repeat (int): The number of random courses to return.

    Examples:
        $ naija course
        $ naija course --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course = naija.course()
        if course:
            click.echo(course)
        else:
            click.echo("Error: Failed to generate course.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
)
def course_name(repeat: int, output: str) -> None:
    """Return random course names.

    This command generates random Nigerian course names.

    Args:
        repeat (int): The number of random course names to return.
        output (str): The format of the output file.

    Examples:
        $ naija course_name
        $ naija course_name --repeat 3
        $ naija course_name --repeat 30 --output csv
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    course_names = []

    for _ in range(repeat):
        course_name = naija.course_name()
        if course_name:
            course_names.append(course_name)
        else:
            click.echo("Error: Failed to generate course name.", err=True)

    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
        }

        base_filename = Path(f"course_names{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(course_names, output_path, output, "course_name")

    else:
        for course_name in course_names:
            click.echo(course_name)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course codes to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
)
def course_code(repeat: int, output: str) -> None:
    """Return random course codes.

    This command generates random Nigerian course codes.

    Args:
        repeat (int): The number of random course codes to return.
        output (str): The format of the output file.

    Examples:
        $ naija course_code
        $ naija course_code --repeat 3
        $ naija course_code -r 3 -o json
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    course_codes = []

    for _ in range(repeat):
        course_code = naija.course_code()
        if course_code:
            course_codes.append(course_code)
        else:
            click.echo("Error: Failed to generate course code.", err=True)

    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
        }

        base_filename = Path(f"course_codes{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(course_codes, output_path, output, "course_code")

    else:
        for course_code in course_codes:
            click.echo(course_code)
