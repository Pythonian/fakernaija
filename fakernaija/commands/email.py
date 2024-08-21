"""Email commands to generate and return random email addresses."""

import click

from fakernaija import Faker

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
def email(
    repeat: int,
    tribe: str,
    gender: str,
    domain: str,
    name: str,
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

    Note:
        - Gender options: male, female
        - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

    Examples:
        To generate a single random email address:

        .. code-block:: bash

            $ naija email
            osayandeiyamu@gov.ng

        To generate 3 random email addresses:

        .. code-block:: bash

            $ naija email --repeat 3
            gidado.bello@hotmail.com
            oluwaseunjide@gmail.com
            tochukwu.nwankwo@gov.ng

        To generate a random email address from a specific tribe:

        .. code-block:: bash

            $ naija email --tribe igbo
            chioma.onyekaozuru97@gmail.com

        To generate a random email address from a specific gender:

        .. code-block:: bash

            $ naija email --gender female
            oluchi.obi@gov.ng

        To generate a random email address with a custom domain:

        .. code-block:: bash

            $ naija email --domain unn.edu.ng
            hassan.sadio54@unn.edu.ng

        To generate an email address from a specific name:

        .. code-block:: bash

            $ naija email --name "Ugochi Maduike"
            ugochi.maduike75@mail.com

        To generate 3 random emails for a specific tribe, gender and domain:

        .. code-block:: bash

            $ naija email -r 3 --tribe yoruba --gender male --domain gov.ng
            ogunlana.kola@gov.ng
            olamideogunbiyi@gov.ng
            kunleadewale@gov.ng
    """
    if repeat < 1:
        click.echo(
            "Error: Repeat count must be a positive integer.",
            err=True,
        )
        return

    for _ in range(repeat):
        email = naija.email(
            tribe=tribe,
            gender=gender,
            domain=domain,
            name=name,
        )
        if email:
            click.echo(email)
        else:
            click.echo("Error: Failed to generate email address.", err=True)
