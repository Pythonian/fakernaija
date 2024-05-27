"""This module provides a NameProvider class for generating Nigerian name combinations."""

import json
import random
from pathlib import Path


class NameProvider:
    """Provides functionality for generating names based on ethnicity and gender."""

    def __init__(self) -> None:
        """Initialize the NameProvider.

        Sets the path to the directory containing name data files.
        """
        self.data_path = Path(__file__).parent / "data" / "names" / "tribes"

    def load_json(self, file_path: str | Path) -> list[dict[str, str]]:
        """Load data from a JSON file.

        Args:
            file_path (Path): The path to the JSON file.

        Returns:
            list[dict[str, str]]: The data loaded from the JSON file.

        Raises:
            FileNotFoundError: If the JSON file is not found.
            ValueError: If the JSON data is invalid.
        """
        try:
            with Path(file_path).open(encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            msg = f"File not found: {file_path}"
            raise FileNotFoundError(msg) from None
        except json.JSONDecodeError as exc:
            msg = f"Error decoding JSON from file: {file_path}"
            raise ValueError(msg) from exc

    def get_first_names(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> list[dict[str, str]]:
        """Get a list of first names optionally filtered by ethnic group and gender.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.

        Returns:
            list[dict[str, str]]: A list of first names matching the specified filters.
        """
        file_path = self.data_path / tribe / "first_names" if tribe else self.data_path
        first_names = []
        for json_file in file_path.rglob("*.json"):
            file_data = self.load_json(json_file)
            if gender:
                file_data = [name for name in file_data if name["gender"] == gender]
            first_names.extend(file_data)
        return first_names

    def get_last_names(self, tribe: str | None = None) -> list[dict[str, str]]:
        """Get a list of last names optionally filtered by ethnic group.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.

        Returns:
            list[dict[str, str]]: A list of last names matching the specified filter.
        """
        file_path = (
            self.data_path / tribe / "last_names.json"
            if tribe
            else self.data_path / "last_names.json"
        )
        return self.load_json(file_path)

    def generate_first_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random first name optionally from a specific ethnic group and gender.

        Args:
            tribe (str | None, optional): The ethnic group of the name. Defaults to None.
            gender (str | None, optional): The gender of the name. Defaults to None.

        Returns:
            str: A random first name.
        """
        first_names = self.get_first_names(tribe, gender)
        return random.choice(first_names)["name"]

    def generate_last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name optionally from a specific ethnic group.

        Args:
            tribe (str | None, optional): The ethnic group of the name. Defaults to None.

        Returns:
            str: A random last name.
        """
        last_names = self.get_last_names(tribe)
        return random.choice(last_names)["name"]

    def generate_full_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random full name optionally from a specific ethnic group and gender.

        Args:
            tribe (str | None, optional): The ethnic group of the name. Defaults to None.
            gender (str | None, optional): The gender of the name. Defaults to None.

        Returns:
            str: A random full name.
        """
        first_name = self.generate_first_name(tribe, gender)
        last_name = self.generate_last_name(tribe)
        return f"{first_name} {last_name}"
