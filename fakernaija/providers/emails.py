"""This module provides an EmailProvider class for generating email addresses with Nigerian name combinations."""

import json
import random
from pathlib import Path


class EmailProvider:
    """Provides functionality for generating email addresses with Nigerian names."""

    def __init__(self) -> None:
        """Initialize the NameProvider.

        Sets the path to the directory containing name data files
        and loads the name data.
        """
        self.data_path = Path(__file__).parent / "data" / "names"
        self.first_names = self.load_json(self.data_path / "first_names.json")
        self.last_names = self.load_json(self.data_path / "last_names.json")
        self.domains = ["gmail.com", "yahoo.com", "outlook.com"]

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
        if tribe:
            return [name for name in self.last_names if name["tribe"] == tribe]
        return self.last_names

    def get_names_by_tribe(
        self,
        tribe: str,
        gender: str | None = None,
    ) -> tuple[list[str], list[str]]:
        """Get first and last names filtered by tribe and optionally by gender.

        Args:
            tribe (str): The ethnic group to filter by.
            gender (str | None, optional): The gender to filter by. Defaults to None.

        Returns:
            tuple[list[str], list[str]]: A tuple containing lists of first and last names.
        """
        first_names = [name["name"] for name in self.get_first_names(tribe, gender)]
        last_names = [name["name"] for name in self.get_last_names(tribe)]
        return first_names, last_names

    def generate_email(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str | None:
        """Generate a random email address with Nigerian names.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.

        Returns:
        str | None: The generated email address or None if no matching data is found.
        """
        if tribe:
            first_names, last_names = self.get_names_by_tribe(tribe, gender)
        else:
            # Randomly choose a tribe to ensure names are from the same tribe
            all_tribes = list({name["tribe"] for name in self.first_names})
            chosen_tribe = random.choice(all_tribes)
            first_names, last_names = self.get_names_by_tribe(chosen_tribe, gender)

        if not first_names or not last_names:
            return None

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        formats = [
            f"{first_name}.{last_name}",
            f"{first_name}{last_name}",
            f"{last_name}.{first_name}",
            f"{last_name}{first_name}",
        ]

        chosen_format = random.choice(formats)
        domain = random.choice(self.domains)
        email = f"{chosen_format}@{domain}".lower()

        # Optionally, add a random number suffix to ensure uniqueness
        # We set it at 50% probability for adding a suffix to the email
        if random.random() < 0.5:  # noqa: PLR2004
            email = (
                email.split("@")[0]
                + str(random.randint(1, 999))
                + "@"
                + email.split("@")[1]
            )

        return email
