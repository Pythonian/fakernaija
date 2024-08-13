"""This module provides an EmailProvider class for generating email addresses with Nigerian name combinations."""

import random
import re

from fakernaija.providers.name_provider import NameProvider
from fakernaija.utils import normalize_input


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
            "hotmail.com",
            "edu.ng",
            "gov.ng",
            "mail.com",
        ]

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
    ) -> str:
        """Generate a random email address with Nigerian names.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.
            domain (str | None, optional): The domain to use for the email. Defaults to None.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If the domain is invalid or if no matching data is found for the given tribe or gender.
        """
        # Normalize the gender and tribe inputs to lowercase
        tribe = normalize_input(tribe)
        gender = normalize_input(gender)
        domain = normalize_input(domain)

        if domain and not self.validate_domain(domain):
            msg = f"Invalid domain: {domain}"
            raise ValueError(msg)

        if tribe:
            first_names = self.name_provider.get_first_names(tribe, gender)
            last_names = self.name_provider.get_last_names(tribe)
        else:
            # Randomly choose a tribe to ensure names are from the same tribe
            all_tribes = self.name_provider.tribes
            chosen_tribe = random.choice(all_tribes)
            first_names = self.name_provider.get_first_names(chosen_tribe, gender)
            last_names = self.name_provider.get_last_names(chosen_tribe)

        if not first_names or not last_names:
            msg = f"No matching data found for tribe: {tribe} or gender: {gender}"
            raise ValueError(msg)

        first_name = random.choice([name["name"] for name in first_names])
        last_name = random.choice([name["name"] for name in last_names])

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
                f"{email.split('@')[0]}{random.randint(1, 99)}@{email.split('@')[1]}"
            )

        if not self.validate_email(email):
            msg = f"Invalid email format generated: {email}"
            raise ValueError(msg)

        return email
