"""Course commands to return random Nigerian schools course data."""

import click

from fakernaija import Faker
from fakernaija.utils import generate_command_data, handle_command_output

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course objects to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def course(repeat: int, output: str) -> None:
    """Returns random course objects.

    Args:
        repeat (int): The number of random course objects to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Examples:
        To return a single random course object:

        .. code-block:: console

            $ naija course
            {'name': 'Advanced Physical Chemistry I', 'code': 'CHM411'}

        To return 3 random course objects:

        .. code-block:: console

            $ naija course --repeat 3
            {'name': 'Advanced Quantum Mechanics', 'code': 'PHY463'}
            {'name': 'Numerical Analysis II', 'code': 'MTH444'}
            {'name': 'Time Series Analysis I', 'code': 'STA415'}

        To return 30 random course objects and save them to a specified format:

        .. code-block:: console

            $ naija course --repeat 30 --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.course)
    if data:
        handle_command_output(data, output, "courses", "courses")


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
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def course_name(repeat: int, output: str) -> None:
    """Returns random course names.

    Args:
        repeat (int): The number of random course names to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single random course name:

        .. code-block:: console

            $ naija course_name
            Methods of Theoretical Physics I

        To return 3 random course names:

        .. code-block:: console

            $ naija course_name --repeat 3
            Multivariate Analysis
            Optimization to Operation Research
            Multivariate Analysis II

        To return 30 random course names and save them to a specified format:

        .. code-block:: console

            $ naija course_name --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.course_name)
    if data:
        handle_command_output(data, output, "course_names", "course names")


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
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def course_code(repeat: int, output: str) -> None:
    """Returns random course codes.

    Args:
        repeat (int): The number of random course codes to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single random course code:

        .. code-block:: console

            $ naija course_code
            CHM302

        To return 3 random course codes:

        .. code-block:: console

            $ naija course_code --repeat 3
            PHY434
            CHM484
            CHM324

        To return 30 random course codes and save them to a specified format:

        .. code-block:: console

            $ naija course_code --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.course_code)
    if data:
        handle_command_output(data, output, "course_codes", "course codes")
