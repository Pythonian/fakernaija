"""Utility file that provides functions to common functionalities."""

import csv
import json
from pathlib import Path
from typing import Any

import click


def load_json(file_path: str | Path, required_keys: list[str]) -> list[dict[str, Any]]:
    """Load data from a JSON file and validate its structure.

    Args:
        file_path (str | Path): The path to the JSON file.
        required_keys (list[str]): The keys that each entry in the JSON data must have.

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
        required_keys (list[str]): The keys that each entry in the JSON data must have.

    Raises:
        ValueError: If any entry is missing a required key or contains extra keys.
    """
    for entry in data:
        entry_keys = set(entry.keys())
        required_keys_set = set(required_keys)

        missing_keys = required_keys_set - entry_keys
        invalid_keys = entry_keys - required_keys_set

        if missing_keys:
            msg = f"Missing keys {missing_keys} in entry: {entry}"
            raise ValueError(msg)
        if invalid_keys:
            msg = f"Invalid keys {invalid_keys} in entry: {entry}"
            raise ValueError(msg)


def validate_degree_type(degree_type: str, valid_degree_types: list[str]) -> str:
    """Validate and convert degree type to lowercase.

    Args:
        degree_type (str): The type of degree to validate.
        valid_degree_types (list[str]): List of valid degree types.

    Returns:
        str: The validated and lowercased degree type.

    Raises:
        ValueError: If the degree type is not valid.
    """
    degree_type = degree_type.lower()
    if degree_type not in valid_degree_types:
        msg = f"Invalid degree_type. Must be one of {valid_degree_types}."
        raise ValueError(msg)
    return degree_type


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
                        writer.writerow([data_type.capitalize()])
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
        click.echo(f"Generated {data_type}s saved to {output_path}")
    except OSError as e:
        click.echo(f"Error: Could not write to file {output_path}. {e}", err=True)
