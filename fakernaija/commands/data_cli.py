"""CLI command to generate random Nigerian data combinations."""

from pathlib import Path
from typing import TYPE_CHECKING

import click

from fakernaija.faker import Faker
from fakernaija.utils import get_unique_filename, write_data_to_file

if TYPE_CHECKING:
    from collections.abc import Callable

naija = Faker()


@click.command()
@click.option(
    "--repeat",
    "-r",
    default=1,
    help="Number of times the data should be repeated. Defaults to 1.",
    type=int,
)
@click.option(
    "--output",
    "-o",
    required=True,
    help="The format of the output file.",
    type=click.Choice(["json", "text", "csv"], case_sensitive=False),
)
@click.option(
    "--fields",
    "-f",
    default="",
    help="Comma-separated list of fields to include in the output.",
    type=str,
)
def data(repeat: int, output: str, fields: str) -> None:
    """Generate and output job data in the specified format.

    Examples:
        naija data --repeat 30 --output csv --fields fullname,email,phonenumber
    """
    if repeat < 1:
        click.echo("Error: Repeat count must be a positive integer.", err=True)
        return

    available_fields: dict[str, Callable[[], str]] = {
        "fullname": naija.full_name,
        "email": naija.email,
        "phonenumber": naija.phone_number,
    }

    field_list = fields.split(",") if fields else []
    selected_fields = {
        field: available_fields[field]
        for field in field_list
        if field in available_fields
    }

    if not selected_fields:
        click.echo("Error: No valid fields specified.", err=True)
        return

    jobs = []
    for _ in range(repeat):
        job_data = {field: func() for field, func in selected_fields.items()}
        jobs.append(job_data)

    file_extensions = {
        "json": ".json",
        "text": ".txt",
        "csv": ".csv",
    }

    base_filename = Path(f"data{file_extensions[output]}")
    output_path = get_unique_filename(Path.cwd() / base_filename)
    write_data_to_file(jobs, output_path, output, "data")
