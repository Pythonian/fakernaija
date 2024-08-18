"""CLI commands for StateProvider to return random Nigerian state information."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random states to return. Defaults to 1.",
    type=int,
)
def state(repeat: int) -> None:
    """Return random states.

    Args:
        repeat (int): The number of random states to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random state:

        .. code-block:: bash

            $ naija state
            {'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa']}

        To return 3 random states:

        .. code-block:: bash

            $ naija state --repeat 3
            {'code': 'EB', 'name': 'Ebonyi', 'capital': 'Abakaliki', 'slogan': 'Salt of the Nation', 'region': 'South East', 'postal_code': '840001', 'lgas': ['Abakaliki', 'Afikpo-North', 'Afikpo South (Edda)', 'Ebonyi', 'Ezza-North', 'Ezza-South', 'Ikwo', 'Ishielu', 'Ivo', 'Izzi', 'Ohaukwu', 'Onicha']}

            {'code': 'AD', 'name': 'Adamawa', 'capital': 'Yola', 'slogan': 'Land of Beauty', 'region': 'North East', 'postal_code': '640001', 'lgas': ['Demsa', 'Fufore', 'Ganye', 'Girei', 'Gombi', 'Guyuk', 'Hong', 'Jada', 'Lamurde', 'Madagali', 'Maiha', 'Mayo-Belwa', 'Michika', 'Mubi-North', 'Mubi-South', 'Numan', 'Shelleng', 'Song', 'Toungo', 'Yola North', 'Yola South']}

            {'code': 'KW', 'name': 'Kwara', 'capital': 'Ilorin', 'slogan': 'State of Harmony', 'region': 'North Central', 'postal_code': '240001', 'lgas': ['Asa', 'Baruten', 'Edu', 'Ekiti (Araromi/Opin)', 'Ilorin-East', 'Ilorin-South', 'Ilorin-West', 'Isin', 'Kaiama', 'Moro', 'Offa', 'Oke-Ero', 'Oyun', 'Pategi']}
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state = naija.state()
        if state:
            click.echo(state)
            click.echo("")
        else:
            click.echo("Error: Failed to return state.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random state names to return. Defaults to 1.",
    type=int,
)
def state_name(repeat: int) -> None:
    """Return random state names.

    Args:
        repeat (int): The number of random state names to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random state name:

        .. code-block:: bash

            $ naija state_name
            Lagos

        To return 3 random state names:

        .. code-block:: bash

            $ naija state_name --repeat 3
            Gombe
            Edo
            Anambra
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_name = naija.state_name()
        if state_name:
            click.echo(state_name)
        else:
            click.echo("Error: Failed to return state name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random capitals to return. Defaults to 1.",
    type=int,
)
def state_capital(repeat: int) -> None:
    """Return random state capitals.

    Args:
        repeat (int): The number of random state capitals to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a random state capital:

        .. code-block:: bash

            $ naija state_capital
            Port Harcourt

        To return 3 random state capitals:

        .. code-block:: bash

            $ naija state_capital --repeat 3
            Kano
            Gusau
            Ado-Ekiti
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_capital = naija.state_capital()
        if state_capital:
            click.echo(state_capital)
        else:
            click.echo("Error: Failed to return state capital.", err=True)


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
def state_lga(repeat: int, state: str) -> None:
    """Return a random LGA or LGA in a specified state.

    Args:
        repeat (int): The number of random LGAs to return.
            Must be a positive integer. Defaults to 1.
        state (str): The state's name to return a random LGA from.

    Examples:
        To return a single random LGA:

        .. code-block:: bash

            $ naija state_lga
            Saki-West

        To return 3 random LGAs:

        .. code-block:: bash

            $ naija state_lga --repeat 3
            Riyom
            Argungu
            Jaba

        To return a random LGA from a specific state:

        .. code-block:: bash

            $ naija state_lga --state "cross river"
            Obudu
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_lga = naija.state_lga(state=state)
        if state_lga:
            click.echo(state_lga)
        else:
            click.echo("Error: Failed to return State LGA.", err=True)


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
def state_postal_code(repeat: int, state: str) -> None:
    """Return random postal codes.

    Args:
        repeat (int): The number of random postal codes to return.
            Must be a positive integer. Defaults to 1.
        state (str): The state's name to return its postal code.

    Examples:
        To return a single random state postal code:

        .. code-block:: bash

            $ naija state_postal_code
            700001

        To return 3 random state postal codes:

        .. code-block:: bash

            $ naija state_postal_code --repeat 3
            740001
            720001
            440001

        To return the postal code of a specific state:

        .. code-block:: bash

            $ naija state_postal_code --state "akwa ibom"
            520001
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_postal_code = naija.state_postal_code(state=state)
        if state_postal_code:
            click.echo(state_postal_code)
        else:
            click.echo("Error: Failed to return postal code.", err=True)
