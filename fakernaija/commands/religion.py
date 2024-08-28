"""Religion command to return random religion data."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random religions to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def religion(repeat: int, output: str) -> None:
    """Returns random religions.

    Args:
        repeat (int): The number of random religions to return.
            Must be a positive integer. Defaults to 1.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text

    Examples:
        To return a single random religion:

        .. code-block:: bash

            $ naija religion
            Muslim

        To return 3 random religions:

        .. code-block:: bash

            $ naija religion --repeat 3
            Traditionalist
            Judaist
            Christian

        To return 30 random religions and save them to a specified format:

        .. code-block:: bash

            $ naija religion --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.religion)
    if data:
        handle_command_output(data, output, "religion", "religions")
