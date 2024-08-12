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
    help="Number of random state codes to return. Defaults to 1.",
    type=int,
)
def state_code(repeat: int) -> None:
    """Return random state codes.

    This command generates random Nigerian state codes.

    Args:
        repeat (int): The number of random state codes to return.

    Examples:
        $ naija state_code
        $ naija state_code --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_code = naija.state_code()
        if state_code:
            click.echo(state_code)
        else:
            click.echo("Error: Failed to generate state code.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random state slogans to return. Defaults to 1.",
    type=int,
)
def state_slogan(repeat: int) -> None:
    """Return random state slogans.

    This command generates random Nigerian state slogans.

    Args:
        repeat (int): The number of random state slogans to return.

    Examples:
        $ naija state_slogan
        $ naija state_slogan --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        state_slogan = naija.state_slogan()
        if state_slogan:
            click.echo(state_slogan)
        else:
            click.echo("Error: Failed to generate state slogan.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random regions to return. Defaults to 1.",
    type=int,
)
def region(repeat: int) -> None:
    """Return random regions.

    This command generates random Nigerian regions.

    Args:
        repeat (int): The number of random regions to return.

    Examples:
        $ naija region
        $ naija region --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        region = naija.region()
        if region:
            click.echo(region)
        else:
            click.echo("Error: Failed to generate region.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random region names to return. Defaults to 1.",
    type=int,
)
def region_name(repeat: int) -> None:
    """Return random region names.

    This command generates random Nigerian region names.

    Args:
        repeat (int): The number of random region names to return.

    Examples:
        $ naija region_name
        $ naija region_name --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        region_name = naija.region_name()
        if region_name:
            click.echo(region_name)
        else:
            click.echo("Error: Failed to generate region name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random region abbreviations to return. Defaults to 1.",
    type=int,
)
def region_abbr(repeat: int) -> None:
    """Return random region abbreviations.

    This command generates random Nigerian region abbreviations.

    Args:
        repeat (int): The number of random region abbreviations to return.

    Examples:
        $ naija region_abbr
        $ naija region_abbr --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        region_abbr = naija.region_abbr()
        if region_abbr:
            click.echo(region_abbr)
        else:
            click.echo("Error: Failed to generate region abbreviation.", err=True)


@click.command()
@click.argument("region_abbr")
def state_region(region_abbr: str) -> None:
    """Return a random state from a specific region.

    This command generates a random state from a specified Nigerian region.

    Args:
        region_abbr (str): The abbreviation of the region.

    Examples:
        $ naija state_region SS
    """
    try:
        state_region = naija.state_region(region_abbr)
        if state_region:
            click.echo(state_region)
        else:
            click.echo(
                f"Error: Failed to generate state for region: {region_abbr}",
                err=True,
            )
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


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
def lga(repeat: int) -> None:
    """Return random LGAs.

    This command generates random Nigerian Local Government Areas (LGAs).

    Args:
        repeat (int): The number of random LGAs to return.

    Examples:
        $ naija lga
        $ naija lga --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        lga = naija.lga()
        if lga:
            click.echo(lga)
        else:
            click.echo("Error: Failed to generate LGA.", err=True)


@click.command()
@click.argument("state")
def state_lga(state: str) -> None:
    """Return a random LGA in the specified state.

    This command generates a random Local Government Area (LGA) in a specified Nigerian state.

    Args:
        state (str): The name of the state.

    Examples:
        $ naija state_lga Lagos
    """
    try:
        state_lga = naija.state_lga(state)
        if state_lga:
            click.echo(state_lga)
        else:
            click.echo(f"Error: Failed to generate LGA for state: {state}", err=True)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random postal codes to return. Defaults to 1.",
    type=int,
)
def postal_code(repeat: int) -> None:
    """Return random postal codes.

    This command generates random Nigerian postal codes.

    Args:
        repeat (int): The number of random postal codes to return.

    Examples:
        $ naija postal_code
        $ naija postal_code --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        postal_code = naija.postal_code()
        if postal_code:
            click.echo(postal_code)
        else:
            click.echo("Error: Failed to generate postal code.", err=True)


@click.command()
@click.argument("state")
def state_postal_code(state: str) -> None:
    """Return the postal code of a specific state.

    This command generates the postal code of a specified Nigerian state.

    Args:
        state (str): The name of the state.

    Examples:
        $ naija state_postal_code Lagos
    """
    try:
        state_postal_code = naija.state_postal_code(state)
        if state_postal_code:
            click.echo(state_postal_code)
        else:
            click.echo(
                f"Error: Failed to generate postal code for state: {state}",
                err=True,
            )
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
