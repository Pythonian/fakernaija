"""Main CLI entry point that includes subcommands from various providers."""

import importlib
import pkgutil

import click

from fakernaija import commands


@click.group()
@click.version_option(package_name="fakernaija")
def cli() -> None:
    """A CLI for generating random Nigerian data."""


# Dynamically discover and load all commands from the commands module
for _, module_name, _ in pkgutil.iter_modules(commands.__path__):
    module = importlib.import_module(f"fakernaija.commands.{module_name}")
    # Adding each function in the module as a CLI command
    for name in dir(module):
        command = getattr(module, name)
        if isinstance(command, click.Command):
            cli.add_command(command, name=name)

if __name__ == "__main__":
    cli()
