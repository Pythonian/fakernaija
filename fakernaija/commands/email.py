"""Email commands to generate and return random email addresses."""

import click

from fakernaija import Faker
from fakernaija.utils import generate_command_data, handle_command_output

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random emails to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--tribe",
    "-t",
    default=None,
    help="The tribe to generate email addresses from.",
    type=click.Choice(
        ["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"],
        case_sensitive=False,
    ),
)
@click.option(
    "--gender",
    "-g",
    default=None,
    help="Specify the gender from which emails will be generated.",
    type=click.Choice(["male", "female"], case_sensitive=False),
)
@click.option(
    "--domain",
    "-d",
    default=None,
    help="A custom domain to use for the email address.",
)
@click.option(
    "--name",
    "-n",
    default=None,
    help="Generate an email address from a given name.",
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def email(  # noqa: PLR0913
    repeat: int,
    tribe: str,
    gender: str,
    domain: str,
    name: str,
    output: str,
) -> None:
    """Generate and return random email addresses.

    Args:
        repeat (int): The number of random email addresses to return.
            Must be a positive integer. Defaults to 1.
        tribe (str): The tribe to generate names from for the email address.
        gender (str): The specific gender to use when generating names
            for the email address.
        domain (str): A custom domain to use for the email address.
        name (str): A specific name to use for generating the email address.
        output (str): The format of the output file if provided.

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
        - Output options: csv, json, text

    Examples:
        To generate a single random email address:

        .. code-block:: console

            $ naija email
            osayandeiyamu@gov.ng

        To generate 3 random email addresses:

        .. code-block:: console

            $ naija email --repeat 3
            gidado.bello@hotmail.com
            oluwaseunjide@gmail.com
            tochukwu.nwankwo@gov.ng

        To generate a random email address from a specific tribe:

        .. code-block:: console

            $ naija email --tribe igbo
            chioma.onyekaozuru97@gmail.com

        To generate a random email address from a specific gender:

        .. code-block:: console

            $ naija email --gender female
            oluchi.obi@gov.ng

        To generate a random email address with a custom domain:

        .. code-block:: console

            $ naija email --domain unn.edu.ng
            hassan.sadio54@unn.edu.ng

        To generate an email address from a specific name:

        .. code-block:: console

            $ naija email --name "Ugochi Maduike"
            ugochi.maduike75@mail.com

        To generate 3 random emails for a specific tribe, gender and domain:

        .. code-block:: console

            $ naija email -r 3 --tribe yoruba --gender male --domain gov.ng
            ogunlana.kola@gov.ng
            olamideogunbiyi@gov.ng
            kunleadewale@gov.ng

        To generate 30 random emails and save them to a specified format:

        .. code-block:: bash

            $ naija email --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.email,
        tribe=tribe,
        gender=gender,
        domain=domain,
        name=name,
    )
    if data:
        handle_command_output(data, output, "emails", "email addresses")
