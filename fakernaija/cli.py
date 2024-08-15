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
    lga,
    phonenumber,
    postal_code,
    prefix,
    region,
    region_abbr,
    region_name,
    school,
    school_name,
    state,
    state_capital,
    state_code,
    state_lga,
    state_name,
    state_postal_code,
    state_region,
    state_slogan,
)


@click.group()
@click.version_option(package_name="fakernaija")
def cli() -> None:
    """A CLI for generating random Nigerian data."""


# Data CLI
cli.add_command(data, name="data")

# Course CLI
cli.add_command(course, name="course")
cli.add_command(course_code, name="course_code")
cli.add_command(course_name, name="course_name")

# Currency CLI
cli.add_command(currency, name="currency")
cli.add_command(currency_code, name="currency_code")
cli.add_command(currency_name, name="currency_name")
cli.add_command(currency_symbol, name="currency_symbol")

# Degree CLI
cli.add_command(degree, name="degree")
cli.add_command(degree_abbr, name="degree_abbr")
cli.add_command(degree_name, name="degree_name")

# Email CLI
cli.add_command(email, name="email")

# Faculty CLI
cli.add_command(department, name="department")
cli.add_command(department_by_faculty, name="department_by_faculty")
cli.add_command(faculty, name="faculty")
cli.add_command(faculty_name, name="faculty_name")

# Name CLI
cli.add_command(firstname, name="firstname")
cli.add_command(fullname, name="fullname")
cli.add_command(lastname, name="lastname")
cli.add_command(prefix, name="prefix")

# Phonenumber CLI
cli.add_command(phonenumber, name="phonenumber")

# School CLI
cli.add_command(school, name="school")
cli.add_command(school_name, name="school_name")

# State CLI
cli.add_command(lga, name="lga")
cli.add_command(postal_code, name="postal_code")
cli.add_command(region, name="region")
cli.add_command(region_abbr, name="region_abbr")
cli.add_command(region_name, name="region_name")
cli.add_command(state, name="state")
cli.add_command(state_capital, name="state_capital")
cli.add_command(state_code, name="state_code")
cli.add_command(state_lga, name="state_lga")
cli.add_command(state_name, name="state_name")
cli.add_command(state_postal_code, name="state_postal_code")
cli.add_command(state_region, name="state_region")
cli.add_command(state_slogan, name="state_slogan")

if __name__ == "__main__":
    cli()
