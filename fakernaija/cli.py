"""Main CLI entry point that includes subcommands from various providers."""

import click

from fakernaija.commands.degree_cli import degree


@click.group()
def cli() -> None:
    """A CLI for generating random Nigerian academic data."""


cli.add_command(degree, name="degree")

if __name__ == "__main__":
    cli()
