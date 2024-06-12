"""Main CLI entry point that includes subcommands from various providers."""

import click

from fakernaija.commands.degree_cli import degree
from fakernaija.commands.email_cli import email
from fakernaija.commands.faculty_cli import department, faculty
from fakernaija.commands.phonenumber_cli import phonenumber


@click.group()
def cli() -> None:
    """A CLI for generating random Nigerian data."""


cli.add_command(degree, name="degree")
cli.add_command(department, name="department")
cli.add_command(email, name="email")
cli.add_command(faculty, name="faculty")
cli.add_command(phonenumber, name="phonenumber")

if __name__ == "__main__":
    cli()
