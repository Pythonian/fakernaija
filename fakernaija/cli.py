"""Main CLI entry point that includes subcommands from various providers."""

import click

from fakernaija.commands.course_cli import course, course_code, course_name
from fakernaija.commands.currency_cli import (
    currency,
    currency_code,
    currency_name,
    currency_symbol,
)
from fakernaija.commands.degree_cli import degree, degree_abbr, degree_name
from fakernaija.commands.email_cli import email
from fakernaija.commands.faculty_cli import department, faculty
from fakernaija.commands.name_cli import firstname, fullname, lastname, prefix
from fakernaija.commands.phonenumber_cli import calling_code, phonenumber


@click.group()
def cli() -> None:
    """A CLI for generating random Nigerian data."""


cli.add_command(calling_code, name="calling_code")
cli.add_command(course, name="course")
cli.add_command(course_code, name="course_code")
cli.add_command(course_name, name="course_name")
cli.add_command(currency, name="currency")
cli.add_command(currency_code, name="currency_code")
cli.add_command(currency_name, name="currency_name")
cli.add_command(currency_symbol, name="currency_symbol")
cli.add_command(degree, name="degree")
cli.add_command(degree_abbr, name="degree_abbr")
cli.add_command(degree_name, name="degree_name")
cli.add_command(department, name="department")
cli.add_command(email, name="email")
cli.add_command(faculty, name="faculty")
cli.add_command(firstname, name="firstname")
cli.add_command(fullname, name="fullname")
cli.add_command(lastname, name="lastname")
cli.add_command(prefix, name="prefix")
cli.add_command(phonenumber, name="phonenumber")

if __name__ == "__main__":
    cli()
