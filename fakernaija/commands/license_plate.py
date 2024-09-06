"""License plate command to return random license plates data."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random license plates to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Generate plate numbers from any state LGA in Nigeria.",
    type=str,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def license_plate(repeat: int, state: str, output: str) -> None:
    """Generate and returns random license plates.

    Args:
        repeat (int): The number of random license plates to return.
            Must be a positive integer. Defaults to 1.
        state (str): Generate license plate number by state.
        output (str): The format of the output file if provided.

    Note:
        - Output options: csv, json, text
        - State options: 36 states in Nigeria + FCT

    Examples:
        To generate a single random license plate:

        .. code-block:: bash

            $ naija license_plate
            FST-452UB

        To generate 3 random license plates:

        .. code-block:: bash

            $ naija license_plate --repeat 3
            LND-718GQ
            BWR-486US
            AAA-182DD

        To generate a random license plate from a specific state in Nigeria:

        .. code-block:: console

            $ naija license_plate --state "akwa ibom"
            NGD-631CK

        To generate 30 random license plate numbers and save them to a specified format:

        .. code-block:: bash

            $ naija license_plate --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(repeat, naija.license_plate, state=state)
    if data:
        handle_command_output(data, output, "license_plate", "license plates")
