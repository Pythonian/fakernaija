"""Phonenumber commands to generate and return random phone numbers."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random phone numbers to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--network",
    "-n",
    default=None,
    help="Specific network to generate phone numbers from.",
    type=click.Choice(
        ["mtn", "glo", "airtel", "etisalat"],
        case_sensitive=False,
    ),
)
@click.option(
    "--prefix",
    "-p",
    default=None,
    help="Specific prefix to generate the phone numbers from.",
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def phone_number(repeat: int, network: str, prefix: str, output: str) -> None:
    """Generate and return random phone numbers.

    Args:
        repeat (int): The number of random phone numbers to return.
            Must be a positive integer. Defaults to 1.
        network (str): The network type to generate the phone number from.
        prefix (str): A specific prefix to generate the phone number from.
        output (str): The format of the output file if provided.

    Raises:
        ValueError: If the given prefix is not valid or the network and prefix
            combination does not match.

    Note:
        - Output options: csv, json, text
        - Available networks and prefixes:
            - mtn: 0703, 0706, 0803, 0806, 0813, 0816, 0810, 0814, 0903, 0906, 0913, 0916
            - glo: 0705, 0805, 0807, 0811, 0815, 0905, 0915
            - airtel: 0802, 0808, 0812, 0708, 0701, 0901, 0902, 0907
            - etisalat: 0809, 0817, 0818, 0908, 0909

    Examples:
        To generate a single random phone number:

        .. code-block:: console

            $ naija phone_number
            07062299016

        To generate 3 random phone numbers:

        .. code-block:: console

            $ naija phone_number --repeat 3
            08027680763
            09093662189
            07062504974

        To generate a random phone number from a specific network:

        .. code-block:: console

            $ naija phone_number --network mtn
            08061821006

        To generate a random phone number with a specific prefix:

        .. code-block:: console

            $ naija phone_number --prefix 0703
            07039490580

        To generate 3 random phone numbers for a specific network and prefix:

        .. code-block:: console

            $ naija phone_number -r 3 --network glo --prefix 0805
            08055333680
            08050142530
            08050269007

        To return 30 random phonenumbers and save them to a specified format:

        .. code-block:: bash

            $ naija phone_number --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.phone_number,
        network=network,
        prefix=prefix,
    )
    if data:
        handle_command_output(data, output, "phone_number", "phone numbers")
