"""Marital status command to return random marital status data."""

import click

from fakernaija import Faker
from fakernaija.utils import generate_command_data, handle_command_output

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random marital statuses to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def marital_status(repeat: int, output: str) -> None:
    """Returns random marital statuses.

    Args:
        repeat (int): The number of random marital statuses to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single random marital status:

        .. code-block:: bash

            $ naija marital_status
            Widowed

        To return 3 random marital statuses:

        .. code-block:: bash

            $ naija marital_status --repeat 3
            Married
            Annulled
            Engaged

        To return 30 random marital statuses and save them to a specified format:

        .. code-block:: bash

            $ naija marital_status --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.marital_status)
    if data:
        handle_command_output(data, output, "marital_status", "marital statuses")
