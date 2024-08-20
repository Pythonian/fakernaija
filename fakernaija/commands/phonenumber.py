"""CLI commands for PhoneNumberProvider to generate random phone numbers."""

import click

from fakernaija import Faker

naija = Faker()


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
def phonenumber(repeat: int, network: str, prefix: str) -> None:
    """Generate and return random phone numbers.

    Args:
        repeat (int): The number of random phone numbers to return.
            Must be a positive integer. Defaults to 1.
        network (str): The network type to generate the phone number from.
        prefix (str): A specific prefix to generate the phone number from.

    Note:
        Available networks and prefixes:
            - mtn: 0703, 0706, 0803, 0806, 0813, 0816, 0810, 0814, 0903, 0906, 0913, 0916
            - glo: 0705, 0805, 0807, 0811, 0815, 0905, 0915
            - airtel: 0802, 0808, 0812, 0708, 0701, 0901, 0902, 0907
            - etisalat: 0809, 0817, 0818, 0908, 0909

    Raises:
        ValueError: If the given prefix is not valid or the network and prefix
            combination does not match.

    Examples:
        To generate a single random phone number:

        .. code-block:: bash

            $ naija phonenumber
            07062299016

        To generate 3 random phone numbers:

        .. code-block:: bash

            $ naija phonenumber --repeat 3
            08027680763
            09093662189
            07062504974

        To generate a random phone number from a specific network:

        .. code-block:: bash

            $ naija phonenumber --network mtn
            08061821006

        To generate a random phone number with a specific prefix:

        .. code-block:: bash

            $ naija phonenumber --prefix 0703
            07039490580

        To generate 3 random phone numbers for a specific network and prefix:

        .. code-block:: bash

            $ naija phonenumber -r 3 --network glo --prefix 0805
            08055333680
            08050142530
            08050269007
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        for _ in range(repeat):
            phonenumber = naija.phone_number(network=network, prefix=prefix)
            if phonenumber:
                click.echo(phonenumber)
            else:
                click.echo("Error: Failed to generate phone number.", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
