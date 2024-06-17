"""CLI commands for CourseProvider to generate random Nigerian courses."""

import click

from fakernaija.faker import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random courses to return. Defaults to 1.",
    type=int,
)
def course(repeat: int) -> None:
    """Return random courses.

    This command generates random Nigerian courses.

    Args:
        repeat (int): The number of random courses to return.

    Examples:
        $ naija course
        $ naija course --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course = naija.course()
        if course:
            click.echo(course)
        else:
            click.echo("Error: Failed to generate course.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course names to return. Defaults to 1.",
    type=int,
)
def course_name(repeat: int) -> None:
    """Return random course names.

    This command generates random Nigerian course names.

    Args:
        repeat (int): The number of random course names to return.

    Examples:
        $ naija course_name
        $ naija course_name --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course_name = naija.course_name()
        if course_name:
            click.echo(course_name)
        else:
            click.echo("Error: Failed to generate course name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course codes to return. Defaults to 1.",
    type=int,
)
def course_code(repeat: int) -> None:
    """Return random course codes.

    This command generates random Nigerian course codes.

    Args:
        repeat (int): The number of random course codes to return.

    Examples:
        $ naija course_code
        $ naija course_code --repeat 3
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course_code = naija.course_code()
        if course_code:
            click.echo(course_code)
        else:
            click.echo("Error: Failed to generate course code.", err=True)
