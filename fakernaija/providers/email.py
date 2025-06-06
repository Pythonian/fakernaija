"""This module provides an EmailProvider class for generating email addresses with Nigerian name combinations."""

import difflib
import random
import re

from fakernaija.providers.name import NameProvider
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
        name: str | None = None,
    ) -> str:
        """Generate a random email address with Nigerian names.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.
            domain (str | None, optional): The domain to use for the email. Defaults to None.
            name (str | None, optional): The name to use for the email. Defaults to None.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If the domain is invalid or if no matching data is found for the given tribe or gender.
        """
        # Normalize the inputs
        tribe = normalize_input(tribe)
        gender = normalize_input(gender)
        domain = normalize_input(domain)

        if tribe and tribe not in self.name_provider.tribes:
            # Check if the tribe exists in the list and suggest close matches
            suggestions = difflib.get_close_matches(
                tribe, self.name_provider.tribes, n=3, cutoff=0.6
            )
            msg = (
                f"Unsupported tribe: '{tribe}'. Did you mean: {', '.join(suggestions)}?"
                if suggestions
                else f"Unsupported tribe: '{tribe}'. Available tribes are: {', '.join(self.name_provider.tribes)}."
            )
            raise ValueError(msg)

        if gender and gender not in self.name_provider.genders:
            suggestions = difflib.get_close_matches(
                gender, self.name_provider.genders, n=3, cutoff=0.6
            )
            msg = (
                f"Invalid gender: '{gender}'. Did you mean: {', '.join(suggestions)}?"
                if suggestions
                else f"Invalid gender: '{gender}'. Valid genders are: {', '.join(self.name_provider.genders)}."
            )
            raise ValueError(msg)

        if domain and not self.validate_domain(domain):
            msg = f"Invalid domain: {domain}"
            raise ValueError(msg)

        if name:
            # If a name is provided, use it directly
            name_parts = name.lower().split()
            first_name = name_parts[0]
            last_name = name_parts[-1] if len(name_parts) > 1 else ""
        else:
            # Otherwise, generate the names based on tribe and gender
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
                f"{email.split('@')[0]}{random.randint(1, 9999)}@{email.split('@')[1]}"
            )

        if not self.validate_email(email):
            msg = f"Invalid email format generated: {email}"
            raise ValueError(msg)

        return email
