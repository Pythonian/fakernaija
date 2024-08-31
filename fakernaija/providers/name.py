"""This module provides a NameProvider class for generating Nigerian name combinations."""

import random
from pathlib import Path

from fakernaija.utils import load_json, normalize_input


class NameProvider:
    """Provides functionality for generating names based on tribe and gender."""

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
        self.tribes = ["yoruba", "igbo", "hausa", "edo", "fulani", "ijaw"]
        self.genders = ["male", "female"]

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

        Raises:
            ValueError: If the specified tribe or gender is not supported.
        """
        tribe = normalize_input(tribe)
        gender = normalize_input(gender)

        if tribe and tribe not in self.tribes:
            msg = f"Unsupported tribe: {tribe}. Supported values are: {', '.join(self.tribes)}"
            raise ValueError(msg)

        if gender and gender not in self.genders:
            msg = f"Unsupported gender: {gender}. Supported values are: {', '.join(self.genders)}"
            raise ValueError(msg)

        return [
            name
            for name in self.first_names
            if (tribe is None or name["tribe"] == tribe)
            and (gender is None or name["gender"] == gender)
        ]

    def get_last_names(self, tribe: str | None = None) -> list[dict[str, str]]:
        """Get a list of last names optionally filtered by ethnic group.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.

        Returns:
            list[dict[str, str]]: A list of last names matching the specified filter.

        Raises:
            ValueError: If the specified tribe is not supported.
        """
        tribe = normalize_input(tribe)

        if tribe and tribe not in self.tribes:
            msg = f"Unsupported tribe: {tribe}. Supported tribes are: {', '.join(self.tribes)}"
            raise ValueError(msg)

        return [
            name for name in self.last_names if tribe is None or name["tribe"] == tribe
        ]

    def generate_first_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random first name optionally from a specific tribe and gender.

        Args:
            tribe (str | None, optional): The tribe name. Defaults to None.
            gender (str | None, optional): The gender of the name. Defaults to None.

        Returns:
            str: A random first name.

        Raises:
            ValueError: If the specified tribe or gender is not supported or if no names are available.
        """
        tribe = normalize_input(tribe)
        gender = normalize_input(gender)

        if tribe and tribe not in self.tribes:
            msg = f"Unsupported tribe: {tribe}. Supported values are: {', '.join(self.tribes)}"
            raise ValueError(msg)

        if gender and gender not in self.genders:
            msg = f"Unsupported gender: {gender}. Supported values are: {', '.join(self.genders)}"
            raise ValueError(msg)

        first_names = self.get_first_names(tribe, gender)
        if not first_names:
            msg = "No first names available for the specified criteria."
            raise ValueError(msg)
        return random.choice(first_names)["name"]

    def generate_last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name optionally from a specific tribe.

        Args:
            tribe (str | None, optional): The tribe name. Defaults to None.

        Returns:
            str: A random last name.

        Raises:
            ValueError: If the specified tribe is not supported or if no names are available.
        """
        tribe = normalize_input(tribe)

        if tribe and tribe not in self.tribes:
            msg = f"Unsupported tribe: {tribe}. Supported values are: {', '.join(self.tribes)}"
            raise ValueError(msg)

        last_names = self.get_last_names(tribe)
        if not last_names:
            msg = "No last names available for the specified criteria."
            raise ValueError(msg)
        return random.choice(last_names)["name"]

    def generate_full_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name optionally from a specific tribe, gender, and with a middle name.

        Args:
            tribe (str | None, optional): The tribe name. Defaults to None.
            gender (str | None, optional): The gender of the name. Defaults to None.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random full name.

        Raises:
            ValueError: If the specified tribe or gender is not supported or if no names are available.
        """
        tribe = normalize_input(tribe)
        gender = normalize_input(gender)

        if gender and gender not in self.genders:
            msg = f"Unsupported gender: {gender}. Supported values are: {', '.join(self.genders)}"
            raise ValueError(msg)

        if tribe is None:
            tribe = random.choice(self.tribes)
        elif tribe not in self.tribes:
            msg = f"Unsupported tribe: {tribe}. Supported values are: {', '.join(self.tribes)}"
            raise ValueError(msg)

        first_name = self.generate_first_name(tribe, gender)
        last_name = self.generate_last_name(tribe)

        if middle_name:
            optional_middle_name = self.generate_first_name(tribe, gender)
            while optional_middle_name == first_name:
                optional_middle_name = self.generate_first_name(tribe, gender)
            return f"{first_name} {optional_middle_name} {last_name}"

        return f"{first_name} {last_name}"

    def generate_prefixes(
        self,
        title: str | None,
        gender: str | None,
    ) -> list[str]:
        """Helper method to get the appropriate prefix list based on title and gender.

        Raises:
            ValueError: If an invalid gender or title is provided.
        """
        if title not in {None, "professional", "traditional"}:
            msg = f"Invalid title '{title}'. Must be 'professional' or 'traditional'."
            raise ValueError(msg)

        if gender not in {None, "male", "female"}:
            msg = f"Invalid gender '{gender}'. Must be 'male' or 'female'."
            raise ValueError(msg)

        if title == "professional":
            return [
                "Prof.",
                "Dr.",
                "Engr.",
                "Tpl",
                "Barrister",
                "Esq.",
            ]
        if title == "traditional":
            return self.get_traditional_prefixes(gender)
        return self.get_general_prefixes(gender)

    def get_traditional_prefixes(self, gender: str | None) -> list[str]:
        """Helper method to get traditional prefixes based on gender."""
        male_prefixes = [
            "Chief",
            "Oba",
            "Otunba",
            "Prince",
            "Alhaji",
            "Igwe",
            "Obi",
            "Obong",
            "Emir",
            "Waziri",
            "Olu",
        ]
        female_prefixes = [
            "Chief",
            "Erelu",
            "Princess",
            "Dr. (Mrs.)",
            "Lady (Mrs.)",
            "Hajia",
            "Alhaja",
            "Lolo",
            "Iyalode",
        ]
        return (
            male_prefixes
            if gender == "male"
            else female_prefixes
            if gender == "female"
            else male_prefixes + female_prefixes
        )

    def get_general_prefixes(self, gender: str | None) -> list[str]:
        """Helper method to get general prefixes based on gender."""
        male_prefixes = [
            "Mr.",
            "Master",
            "Mister",
            "Chief",
            "Oba",
            "Otunba",
            "Prince",
            "Prof.",
            "Dr.",
            "Alhaji",
            "Engr.",
            "Tpl",
            "Barrister",
            "Igwe",
            "Obi",
            "Obong",
            "Emir",
            "Waziri",
            "Olu",
        ]
        female_prefixes = [
            "Mrs.",
            "Miss",
            "Madam",
            "Chief",
            "Lady",
            "Princess",
            "Erelu",
            "Prof.",
            "Dr. (Mrs.)",
            "Hajia",
            "Lady (Mrs.)",
            "Alhaja",
            "Lolo",
            "Iyalode",
        ]
        general_prefixes = male_prefixes + female_prefixes
        if gender == "male":
            return male_prefixes
        if gender == "female":
            return female_prefixes
        return general_prefixes
