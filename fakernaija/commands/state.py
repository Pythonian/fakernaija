"""State commands to return random Nigerian state data."""

import click

from fakernaija import Naija
from fakernaija.utils import generate_command_data, handle_command_output

naija = Naija()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random state objects to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--region",
    default=None,
    help="Return state objects by region filter.",
    type=click.Choice(
        ["NW", "NE", "NC", "SE", "SW", "SS"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def state(repeat: int, region: str, output: str) -> None:
    """Return random state objects.

    Args:
        repeat (int): The number of random state objects to return.
            Must be a positive integer. Defaults to 1.
        region (str): The region to filter state objects by.
        output (str): The format of the output file if provided.

    Note:
        - Region options: NW, NE, NC, SE, SW, SS
        - Output options: csv, json, text

    Examples:
        To return a single random state object:

        .. code-block:: console

            $ naija state
            {'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa']}

        To return 3 random state objects:

        .. code-block:: console

            $ naija state --repeat 3
            {'code': 'EB', 'name': 'Ebonyi', 'capital': 'Abakaliki', 'slogan': 'Salt of the Nation', 'region': 'South East', 'postal_code': '840001', 'lgas': ['Abakaliki', 'Afikpo-North', 'Afikpo South (Edda)', 'Ebonyi', 'Ezza-North', 'Ezza-South', 'Ikwo', 'Ishielu', 'Ivo', 'Izzi', 'Ohaukwu', 'Onicha']}
            {'code': 'AD', 'name': 'Adamawa', 'capital': 'Yola', 'slogan': 'Land of Beauty', 'region': 'North East', 'postal_code': '640001', 'lgas': ['Demsa', 'Fufore', 'Ganye', 'Girei', 'Gombi', 'Guyuk', 'Hong', 'Jada', 'Lamurde', 'Madagali', 'Maiha', 'Mayo-Belwa', 'Michika', 'Mubi-North', 'Mubi-South', 'Numan', 'Shelleng', 'Song', 'Toungo', 'Yola North', 'Yola South']}
            {'code': 'KW', 'name': 'Kwara', 'capital': 'Ilorin', 'slogan': 'State of Harmony', 'region': 'North Central', 'postal_code': '240001', 'lgas': ['Asa', 'Baruten', 'Edu', 'Ekiti (Araromi/Opin)', 'Ilorin-East', 'Ilorin-South', 'Ilorin-West', 'Isin', 'Kaiama', 'Moro', 'Offa', 'Oke-Ero', 'Oyun', 'Pategi']}

        To return a random state object filtered by region:

        .. code-block:: bash

            $ naija state --region NW
            {'code': 'ZA', 'name': 'Zamfara', 'capital': 'Gusau', 'slogan': 'Farming is Our Pride', 'region': 'North West', 'postal_code': '860001', 'lgas': ['Anka', 'Bakura', 'Birnin Magaji/Kiyaw', 'Bukkuyum', 'Bungudu', 'Gummi', 'Gusau', 'Isa', 'Kaura-Namoda', 'Kiyawa', 'Maradun', 'Maru', 'Shinkafi', 'Talata-Mafara', 'Tsafe', 'Zurmi'], 'region_abbr': 'NW'}

        To return 30 random state objects and save them to a specified format:

        .. code-block:: bash

            $ naija state --repeat 30 --output csv
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.state,
        region=region,
    )
    if data:
        handle_command_output(data, output, "state", "states")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random state names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--region",
    default=None,
    help="Return state objects by region filter.",
    type=click.Choice(
        ["NW", "NE", "NC", "SE", "SW", "SS"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def state_name(repeat: int, region: str, output: str) -> None:
    """Return random state names.

    Args:
        repeat (int): The number of random state names to return.
            Must be a positive integer. Defaults to 1.
        region (str): The region to filter state objects by.
        output (str): The format of the output file if provided.

    Note:
        - Region options: NW, NE, NC, SE, SW, SS
        - Output options: csv, json, text

    Examples:
        To return a single random state name:

        .. code-block:: console

            $ naija state_name
            Lagos

        To return 3 random state names:

        .. code-block:: console

            $ naija state_name --repeat 3
            Gombe
            Edo
            Anambra

        To return a random state name by region:

        .. code-block:: bash

            $ naija state_name --region SE
            Imo

        To return 30 random state names and save them to a specified format:

        .. code-block:: bash

            $ naija state_name --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.state_name,
        region=region,
    )
    if data:
        handle_command_output(data, output, "state", "states")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random capitals to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--region",
    default=None,
    help="Return state objects by region filter.",
    type=click.Choice(
        ["NW", "NE", "NC", "SE", "SW", "SS"],
        case_sensitive=False,
    ),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def state_capital(repeat: int, region: str, output: str) -> None:
    """Return random state capitals.

    Args:
        repeat (int): The number of random state capitals to return.
            Must be a positive integer. Defaults to 1.
        region (str): The region to filter state objects by.
        output (str): The format of the output file if provided.

    Note:
        - Region options: NW, NE, NC, SE, SW, SS
        - Output options: csv, json, text

    Examples:
        To return a random state capital:

        .. code-block:: console

            $ naija state_capital
            Port Harcourt

        To return 3 random state capitals:

        .. code-block:: console

            $ naija state_capital --repeat 3
            Kano
            Gusau
            Ado-Ekiti

        To return a random state capital from a specific region:

        .. code-block:: bash

            $ naija state_capital --region NC
            Makurdi

        To return 30 random state capitals and save them to a specified format:

        .. code-block:: bash

            $ naija state_capital --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.state_capital,
        region=region,
    )
    if data:
        handle_command_output(data, output, "state_capital", "state capitals")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random LGAs to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Return LGA by any state in Nigeria.",
    type=str,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def state_lga(repeat: int, state: str, output: str) -> None:
    """Return a random LGA or LGA in a specified state.

    Args:
        repeat (int): The number of random LGAs to return.
            Must be a positive integer. Defaults to 1.
        state (str): The state's name to return a random LGA from.
        output (str): The format of the output file if provided.

    Note:
        - State options: 36 states in Nigeria + FCT
        - Output options: csv, json, text

    Examples:
        To return a single random LGA:

        .. code-block:: console

            $ naija state_lga
            Saki-West

        To return 3 random LGAs:

        .. code-block:: console

            $ naija state_lga --repeat 3
            Riyom
            Argungu
            Jaba

        To return a random LGA from a specific state:

        .. code-block:: console

            $ naija state_lga --state "cross river"
            Obudu

        To return 30 random LGAs and save them to a specified format:

        .. code-block:: bash

            $ naija state_lga --repeat 30 --output json
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.state_lga,
        state=state,
    )
    if data:
        handle_command_output(data, output, "lga", "local government areas")


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random postal codes to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--state",
    "-s",
    default=None,
    help="Return the Postal code of any state in Nigeria.",
    type=str,
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "csv", "text"], case_sensitive=False),
)
def state_postal_code(repeat: int, state: str, output: str) -> None:
    """Return random postal codes.

    Args:
        repeat (int): The number of random postal codes to return.
            Must be a positive integer. Defaults to 1.
        state (str): The state's name to return its postal code.
        output (str): The format of the output file if provided.

    Note:
        - State options: 36 states in Nigeria + FCT
        - Output options: csv, json, text

    Examples:
        To return a single random state postal code:

        .. code-block:: console

            $ naija state_postal_code
            700001

        To return 3 random state postal codes:

        .. code-block:: console

            $ naija state_postal_code --repeat 3
            740001
            720001
            440001

        To return the postal code of a specific state:

        .. code-block:: console

            $ naija state_postal_code --state "akwa ibom"
            520001

        To return 30 random postal codes and save them to a specified format:

        .. code-block:: bash

            $ naija state_postal_code --repeat 30 --output text
            Generated data saved to /path/to/directory/filename.ext
    """
    data = generate_command_data(
        repeat,
        naija.state_postal_code,
        state=state,
    )
    if data:
        handle_command_output(data, output, "postal_code", "postal codes")
