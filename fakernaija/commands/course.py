"""Course commands to return random Nigerian schools course data."""

import click

from fakernaija import Faker

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course objects to return. Defaults to 1.",
    type=int,
)
def course(repeat: int) -> None:
    """Returns random course objects.

    Args:
        repeat (int): The number of random course objects to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random course object:

        .. code-block:: bash

            $ naija course
            {'name': 'Advanced Physical Chemistry I', 'code': 'CHM411'}

        To return 3 random course objects:

        .. code-block:: bash

            $ naija course --repeat 3
            {'name': 'Advanced Quantum Mechanics', 'code': 'PHY463'}

            {'name': 'Numerical Analysis II', 'code': 'MTH444'}

            {'name': 'Time Series Analysis I', 'code': 'STA415'}
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course = naija.course()
        if course:
            click.echo(course)
            click.echo()
        else:
            click.echo("Error: Failed to return course object.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course names to return. Defaults to 1.",
    type=int,
)
def course_name(repeat: int) -> None:
    """Returns random course names.

    Args:
        repeat (int): The number of random course names to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random course name:

        .. code-block:: bash

            $ naija course_name
            Methods of Theoretical Physics I

        To return 3 random course names:

        .. code-block:: bash

            $ naija course_name --repeat 3
            Multivariate Analysis
            Optimization to Operation Research
            Multivariate Analysis II
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course_name = naija.course_name()
        if course_name:
            click.echo(course_name)
        else:
            click.echo("Error: Failed to return course name.", err=True)


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of random course codes to return. Defaults to 1.",
    type=int,
)
def course_code(repeat: int) -> None:
    """Returns random course codes.

    Args:
        repeat (int): The number of random course codes to return.
            Must be a positive integer. Defaults to 1.

    Examples:
        To return a single random course code:

        .. code-block:: bash

            $ naija course_code
            CHM302

        To return 3 random course codes:

        .. code-block:: bash

            $ naija course_code --repeat 3
            PHY434
            CHM484
            CHM324
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    for _ in range(repeat):
        course_code = naija.course_code()
        if course_code:
            click.echo(course_code)
        else:
            click.echo("Error: Failed to return course code.", err=True)
