"""This module provides a NameProvider class for generating Nigerian name combinations."""

import random
from pathlib import Path

from fakernaija.utils import load_json


class NameProvider:
    """Provides functionality for generating names based on ethnicity and gender."""

    def __init__(self) -> None:
        """Initialize the NameProvider.

        Sets the path to the directory containing name data files.
        """
        self.data_path = Path(__file__).parent.parent / "data" / "names"
        self.first_names = load_json(
            self.data_path / "first_names.json",
            ["tribe", "gender", "name"],
        )
        self.last_names = load_json(
            self.data_path / "last_names.json",
            ["tribe", "name"],
        )

    def normalize_input(self, value: str | None) -> str | None:
        """Normalize input value to lowercase.

        Args:
            value (str | None): The value to normalize.

        Returns:
            str | None: The normalized value or None if the input is None.
        """
        return value.lower() if value is not None else None

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
        tribe = self.normalize_input(tribe)
        gender = self.normalize_input(gender)

        names = self.first_names
        if tribe:
            names = [name for name in names if name["tribe"] == tribe]
        if gender:
            names = [name for name in names if name["gender"] == gender]
        return names

    def get_last_names(self, tribe: str | None = None) -> list[dict[str, str]]:
        """Get a list of last names optionally filtered by ethnic group.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.

        Returns:
            list[dict[str, str]]: A list of last names matching the specified filter.
        """
        tribe = self.normalize_input(tribe)

        if tribe:
            return [name for name in self.last_names if name["tribe"] == tribe]
        return self.last_names

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
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name optionally from a specific ethnic group, gender, and with a middle name.

        Args:
            tribe (str | None, optional): The ethnic group of the name. Defaults to None.
            gender (str | None, optional): The gender of the name. Defaults to None.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random full name.
        """
        first_name = self.generate_first_name(tribe, gender)
        last_name = self.generate_last_name(tribe)
        if middle_name:
            optional_middle_name = self.generate_first_name(tribe, gender)
            return f"{first_name} {optional_middle_name} {last_name}"
        return f"{first_name} {last_name}"
