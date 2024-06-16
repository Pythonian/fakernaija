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
@click.option(
    "--code",
    "-c",
    is_flag=True,
    help="Return course codes instead of names.",
)
def course(repeat: int, code: bool) -> None:
    """Return random courses.

    This command generates random Nigerian courses.

    Args:
        repeat (int): The number of random courses to return.
        code (bool): If set, return course codes instead of course names.

    Examples:
        $ naija course
        $ naija course --repeat 3
        $ naija course --code
        $ naija course --repeat 3 --code
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course = naija.course(code=code)
        if course:
            click.echo(course)
        else:
            click.echo("Error: Failed to generate course.", err=True)
