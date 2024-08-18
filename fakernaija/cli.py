"""Main CLI entry point that includes subcommands from various providers."""

import click

from fakernaija.commands import (
    course,
    course_code,
    course_name,
    currency,
    currency_code,
    currency_name,
    currency_symbol,
    data,
    degree,
    degree_abbr,
    degree_name,
    department,
    department_by_faculty,
    email,
    faculty,
    faculty_name,
    firstname,
    fullname,
    lastname,
    phonenumber,
    prefix,
    school,
    school_name,
    state,
    state_capital,
    state_lga,
    state_name,
    state_postal_code,
)


@click.group()
@click.version_option(package_name="fakernaija")
def cli() -> None:
    """A CLI for generating random Nigerian data."""


# Mapping of command names to their respective command functions
commands = {
    "data": data,
    "course": course,
    "course_code": course_code,
    "course_name": course_name,
    "currency": currency,
    "currency_code": currency_code,
    "currency_name": currency_name,
    "currency_symbol": currency_symbol,
    "degree": degree,
    "degree_abbr": degree_abbr,
    "degree_name": degree_name,
    "email": email,
    "department": department,
    "department_by_faculty": department_by_faculty,
    "faculty": faculty,
    "faculty_name": faculty_name,
    "firstname": firstname,
    "fullname": fullname,
    "lastname": lastname,
    "prefix": prefix,
    "phonenumber": phonenumber,
    "school": school,
    "school_name": school_name,
    "state": state,
    "state_capital": state_capital,
    "state_lga": state_lga,
    "state_name": state_name,
    "state_postal_code": state_postal_code,
}

# Loop to add commands to the CLI group
for name, command in commands.items():
    cli.add_command(command, name=name)

if __name__ == "__main__":
    cli()
