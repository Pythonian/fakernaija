"""CLI commands for DegreeProvider to generate random Nigerian degrees."""

from pathlib import Path

import click

from fakernaija.faker import Faker
from fakernaija.utils import (
    get_unique_filename,
    validate_degree_type,
    write_data_to_file,
)

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degrees to return. Defaults to 1.",
    type=int,
)
def degree(repeat: int) -> None:
    """Return random degrees.

    This command generates random Nigerian degrees.

    Args:
        repeat (int): The number of random degrees to return.

    Examples:
        $ naija degree
        $ naija degree --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        degrees = [naija.degree() for _ in range(repeat)]
        for degree in degrees:
            click.echo(degree)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degree names to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(["undergraduate", "masters", "doctorate"], case_sensitive=False),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
)
def degree_name(repeat: int, degree_type: str, output: str) -> None:
    """Return random degree names.

    This command generates random Nigerian degree names.

    Args:
        repeat (int): The number of random degree names to return.
        degree_type (str): Type of degree to generate.
        output (str): The format of the output file.

    Examples:
        $ naija degree_name
        $ naija degree_name --repeat 3
        $ naija degree_name --degree-type masters
        $ naija degree_name --repeat 3 --degree-type undergraduate
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        if degree_type:
            degree_type = validate_degree_type(degree_type, naija.valid_degree_types)
            degree_names = [
                naija.degree_name_by_type(degree_type=degree_type)
                for _ in range(repeat)
            ]
        else:
            degree_names = [naija.degree_name() for _ in range(repeat)]

        if output:
            file_extensions = {
                "json": ".json",
                "text": ".txt",
                "csv": ".csv",
            }

            base_filename = Path(f"degree_names{file_extensions[output]}")
            output_path = get_unique_filename(Path.cwd() / base_filename)
            write_data_to_file(degree_names, output_path, output, "degree_name")

        else:
            for degree_name in degree_names:
                click.echo(degree_name)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random degree abbreviations to return. Defaults to 1.",
    type=int,
)
@click.option(
    "--degree-type",
    "-t",
    default=None,
    help="Type of degree to generate.",
    type=click.Choice(["undergraduate", "masters", "doctorate"], case_sensitive=False),
)
@click.option(
    "--output",
    "-o",
    default=None,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
)
def degree_abbr(repeat: int, degree_type: str, output: str) -> None:
    """Return random degree abbreviations.

    This command generates random Nigerian degree abbreviations.

    Args:
        repeat (int): The number of random degree abbreviations to return.
        degree_type (str): Type of degree to generate.
        output (str): The format of the output file.

    Examples:
        $ naija degree_abbr
        $ naija degree_abbr --repeat 3
        $ naija degree_abbr --degree-type masters
        $ naija degree_abbr --repeat 3 --degree-type undergraduate
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    try:
        if degree_type:
            degree_type = validate_degree_type(degree_type, naija.valid_degree_types)
            degree_abbrs = [
                naija.degree_abbr_by_type(degree_type=degree_type)
                for _ in range(repeat)
            ]
        else:
            degree_abbrs = [naija.degree_abbr() for _ in range(repeat)]

        if output:
            file_extensions = {
                "json": ".json",
                "text": ".txt",
                "csv": ".csv",
            }

            base_filename = Path(f"degree_abbrs{file_extensions[output]}")
            output_path = get_unique_filename(Path.cwd() / base_filename)
            write_data_to_file(degree_abbrs, output_path, output, "degree_abbr")

        else:
            for degree_abbr in degree_abbrs:
                click.echo(degree_abbr)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
