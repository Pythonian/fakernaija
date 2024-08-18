"""CLI commands for StateProvider to generate random Nigerian state information."""

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

    This command generates random Nigerian states information.

    Args:
        repeat (int): The number of random states to return.

    Examples:
        $ naija state
        $ naija state --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        states = [naija.state() for _ in range(repeat)]
        for state in states:
            click.echo(state)
            # Add a blank line
            click.echo("")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


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

    This command generates random Nigerian state names.

    Args:
        repeat (int): The number of random state names to return.

    Examples:
        $ naija state_name
        $ naija state_name --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_name = naija.state_name()
        if state_name:
            click.echo(state_name)
        else:
            click.echo("Error: Failed to generate state name.", err=True)


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

    This command generates random Nigerian state capitals.

    Args:
        repeat (int): The number of random state capitals to return.

    Examples:
        $ naija state_capital
        $ naija state_capital --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_capital = naija.state_capital()
        if state_capital:
            click.echo(state_capital)
        else:
            click.echo("Error: Failed to generate capital.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random LGAs to return. Defaults to 1.",
    type=int,
)
@click.argument("state")
def state_lga(repeat: int, state: str) -> None:
    """Return a random LGA or LGA in a specified state.

    Args:
        repeat (int): The number of random LGAs to return.
        state (str): The name of the state.

    Examples:
        $ naija state_lga
        $ naija state_lga --repeat 3
        $ naija state_lga Lagos
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_lga = naija.state_lga(state=state)
        if state_lga:
            click.echo(state_lga)
        else:
            click.echo("Error: Failed to generate State LGA.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random postal codes to return. Defaults to 1.",
    type=int,
)
@click.argument("state")
def state_postal_code(repeat: int, state: str) -> None:
    """Return random postal codes.

    Args:
        repeat (int): The number of random postal codes to return.
        state (str): The name of the state.

    Examples:
        $ naija state_postal_code
        $ naija state_postal_code --repeat 3
        $ naija state_postal_code Lagos
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_postal_code = naija.state_postal_code(state=state)
        if state_postal_code:
            click.echo(state_postal_code)
        else:
            click.echo("Error: Failed to generate postal code.", err=True)
