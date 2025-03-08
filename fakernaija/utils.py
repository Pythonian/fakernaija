"""Utility file that provides functions to common functionalities."""

import csv
import json
import random
import unicodedata
from collections.abc import Callable
from pathlib import Path
from typing import Any

import click


def load_json(
    file_path: str | Path,
    required_keys: list[str],
) -> list[dict[str, Any]]:
    """Load data from a JSON file and validate its structure.

    Args:
        file_path (str | Path): The path to the JSON file.
        required_keys (list[str]): The keys that each entry in the JSON data
                                   must have.

    Returns:
        list[dict[str, Any]]: The data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        ValueError: If the JSON data is invalid or missing required keys.
    """
    try:
        with Path(file_path).open(encoding="utf-8") as file:
            data = json.load(file)
            validate_json_structure(data, required_keys)
            return data
    except FileNotFoundError:
        msg = f"File not found: {file_path}"
        raise FileNotFoundError(msg) from None
    except json.JSONDecodeError as exc:
        msg = f"Error decoding JSON from file: {file_path}"
        raise ValueError(msg) from exc


def validate_json_structure(
    data: list[dict[str, Any]],
    required_keys: list[str],
) -> None:
    """Validate the structure of the JSON data.

    Args:
        data (list[dict[str, Any]]): The JSON data to validate.
        required_keys (list[str]): The keys that each entry in the JSON data
                                   must have.

    Raises:
        ValueError: If any entry is missing a required key or contains
                    extra keys.
    """
    required_keys_set = set(required_keys)
    for entry in data:
        entry_keys = set(entry.keys())
        missing_keys = required_keys_set - entry_keys
        invalid_keys = entry_keys - required_keys_set

        if missing_keys or invalid_keys:
            msg = f"Entry: {entry} "
            if missing_keys:
                msg += f"Missing keys: {missing_keys}. "
            if invalid_keys:
                msg += f"Invalid keys: {invalid_keys}."
            raise ValueError(msg)


def get_unique_value(values: list[str], used_values: set[str]) -> str:
    """Helper method to get a unique value from a list of strings.

    Ensures the generated value is unique within the session by:
        * Checking available values against used values.
        * Resetting used values if all options are exhausted.

    Args:
        values (list[str]): The list of possible values.
        used_values (set[str]): The set of values that have already been used.

    Returns:
        str: A unique value from the list.
    """
    # Calculate the set difference to find values that have not been used
    available_values = set(values) - used_values

    # If no values are available, reset the used values set
    if not available_values:
        used_values.clear()
        available_values = set(values)

    # Return a randomly chosen value from the available values
    return random.choice(list(available_values))


def normalize_input(value: str | None) -> str | None:
    """Normalize input value to lowercase.

    Args:
        value (str | None): The value to normalize.

    Returns:
        str | None: The normalized value or None if the input is None.
    """
    if value is None:
        return None

    # Ensure the input is a string
    if not isinstance(value, str):
        msg = f"Expected a string or None, got {type(value).__name__}"
        raise TypeError(msg)

    # Normalize and strip whitespace
    value = value.strip()

    # Remove accents
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )

    # Convert to lowercase
    return value.lower() if value else None


def get_unique_filename(base_path: Path) -> Path:
    """Generate a unique file name by appending numbers if the file exists."""
    counter = 1
    unique_path = base_path
    while unique_path.exists():
        unique_path = base_path.with_stem(f"{base_path.stem}_{counter}")
        counter += 1
    return unique_path


def write_data_to_file(
    data: list[Any],
    output_path: Path,
    output: str,
    data_type: str,
) -> None:
    """Write data to file in specified format.

    Args:
        data (list[Any]): The data to write. Can be a list of dicts or a list of strings.
        output_path (Path): The path to the output file.
        output (str): The format of the output file (e.g., json, csv, text).
        data_type (str): The type of data being written.

    Raises:
        OSError: If there is an error writing to the file.
    """
    try:
        if output == "json":
            with output_path.open("w") as f:
                json.dump(data, f, indent=4)
        elif output == "csv":
            with output_path.open("w", newline="") as f:
                writer = csv.writer(f)
                if data:
                    if isinstance(data[0], dict):
                        writer.writerow(
                            [
                                key.capitalize().replace("_", " ") + "s"
                                for key in data[0]
                            ],
                        )
                        for record in data:
                            writer.writerow(record.values())
                    else:
                        writer.writerow([data_type.title()])
                        for record in data:
                            writer.writerow([record])
        elif output == "text":
            with output_path.open("w") as f:
                if isinstance(data[0], dict):
                    for record in data:
                        f.write(
                            " | ".join(
                                f"{key.capitalize().replace('_', ' ')}: {value}"
                                for key, value in record.items()
                            )
                            + "\n",
                        )
                else:
                    for record in data:
                        f.write(record + "\n")
        click.echo(f"Generated data saved to {output_path}")
    except OSError as e:
        click.echo(
            f"Error: Could not write to file {output_path}. {e}",
            err=True,
        )


def generate_command_data(
    repeat: int,
    generator_func: Callable[..., str | dict[str, Any] | None],
    **kwargs: Any,  # noqa: ANN401
) -> list[str | dict[str, Any]]:
    """Generates CLI data using the provided generator function.

    Args:
        repeat (int): The number of times to generate the data.
        generator_func (Callable): The function to generate data.
        **kwargs: Additional keyword arguments to pass to the generator function.

    Returns:
        list: A list of generated data.
    """
    if repeat < 1:
        click.echo(
            "Error: Repeat count must be a positive integer greater than 0.",
            err=True,
        )
        return []
    data = []
    try:
        for _ in range(repeat):
            item = generator_func(**kwargs)
            if item is not None:
                data.append(item)
            else:
                return []
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        return []
    if not data:
        click.echo("Error: No data was generated.", err=True)
    return data


def handle_command_output(
    data: list[str | dict[str, Any]],
    output: str | None,
    base_filename_prefix: str,
    data_type: str,
) -> None:
    """Handles output to a file or console based on user options.

    Args:
        data (list): The list of data to output.
        output (str): The format of the output file, if provided.
        base_filename_prefix (str): The base name prefix for the output file.
        data_type (str): The type of data for header labeling.
    """
    if output:
        file_extensions = {
            "json": ".json",
            "text": ".txt",
            "csv": ".csv",
        }
        base_filename = Path(f"{base_filename_prefix}{file_extensions[output]}")
        output_path = get_unique_filename(Path.cwd() / base_filename)
        write_data_to_file(data, output_path, output, data_type)
    else:
        for item in data:
            click.echo(item)
