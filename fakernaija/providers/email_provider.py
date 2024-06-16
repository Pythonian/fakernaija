"""This module provides an EmailProvider class for generating email addresses with Nigerian name combinations."""

import random
import re

from fakernaija.providers.name_provider import NameProvider


class EmailProvider:
    """Provides functionality for generating email addresses with Nigerian names."""

    def __init__(self) -> None:
        """Initialize the EmailProvider.

        Initializes NameProvider and sets up email domains.
        """
        self.name_provider = NameProvider()
        self.default_domains = [
            "gmail.com",
            "yahoo.com",
            "edu.ng",
            "gov.ng",
            "mail.com",
        ]

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
        return self.name_provider.get_first_names(tribe, gender)

    def get_last_names(self, tribe: str | None = None) -> list[dict[str, str]]:
        """Get a list of last names optionally filtered by ethnic group.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.

        Returns:
            list[dict[str, str]]: A list of last names matching the specified filter.
        """
        return self.name_provider.get_last_names(tribe)

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

    def validate_domain(self, domain: str) -> bool:
        """Validate the domain format.

        Args:
            domain (str): The domain to validate.

        Returns:
            bool: True if the domain is valid, False otherwise.
        """
        regex = (
            r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63}){0,2}\.[A-Za-z]{2,}$"
        )
        return (
            re.match(regex, domain) is not None and domain.count(".") <= 3  # noqa: PLR2004
        )

    def validate_email(self, email: str) -> bool:
        """Validate the complete email address format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(regex, email) is not None

    def generate_email(
        self,
        tribe: str | None = None,
        gender: str | None = None,
        domain: str | None = None,
    ) -> str | None:
        """Generate a random email address with Nigerian names.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.
            domain (str | None, optional): The domain to use for the email. Defaults to None.

        Returns:
            str | None: The generated email address or None if no matching data
                        is found or the domain is invalid.
        """
        # Normalize the gender and tribe inputs to lowercase
        if tribe:
            tribe = tribe.lower()
        if gender:
            gender = gender.lower()

        if domain:
            domain = domain.lower()
            if not self.validate_domain(domain):
                return None

        if tribe:
            first_names, last_names = self.get_names_by_tribe(tribe, gender)
        else:
            # Randomly choose a tribe to ensure names are from the same tribe
            all_tribes = list(
                {name["tribe"] for name in self.name_provider.first_names},
            )
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
        domain = domain or random.choice(self.default_domains)
        email = f"{chosen_format}@{domain}".lower()

        # Optionally, add a random number suffix to ensure uniqueness
        # We set it at 50% probability for adding a suffix to the email
        if random.random() < 0.5:  # noqa: PLR2004
            email = (
                f"{email.split('@')[0]}{random.randint(1, 999)}@{email.split('@')[1]}"
            )

        if not self.validate_email(email):
            return None

        return email
