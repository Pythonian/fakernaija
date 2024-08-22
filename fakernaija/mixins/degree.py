"""Degree mixin module.

This module defines a mixin class which groups related methods for
fetching and returning degree-related data from its provider.
"""

import random

from fakernaija.providers import DegreeProvider
from fakernaija.utils import validate_degree_type


class Degree:
    """A mixin providing methods to fetch and return degree-related data."""

    def __init__(self) -> None:
        """Initializes the Degree mixin and sets up its provider."""
        self.degree_provider = DegreeProvider()
        self.valid_degree_types = ["undergraduate", "masters", "doctorate"]

    def degree(self, degree_type: str | None = None) -> dict:
        """Returns a random degree object, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            dict[str, str]: A dictionary with degree name, type and abbreviation.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> degree = naija.degree()
                >>> print(f"Random degree: {degree}")
                'Random degree: {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}'

                >>> degree = naija.degree(degree_type="masters")
                >>> print(f"Random masters degree: {degree}")
                'Random masters degree: {'name': 'Master of Business Administration', 'degree_type': 'masters', 'abbr': 'MBA'}'
        """
        if degree_type:
            degree_type = validate_degree_type(
                degree_type,
                self.valid_degree_types,
            )
        return random.choice(self.degree_provider.get_degrees(degree_type))

    def degree_name(self, degree_type: str | None = None) -> str:
        """Generates a random degree name, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            str: A random degree name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> degree_name = naija.degree_name()
                >>> print(f"Random degree name: {degree_name}")
                'Random degree name: Bachelor of Science'

                >>> degree_name = naija.degree_name(degree_type="doctorate")
                >>> print(f"Random doctorate degree name: {degree_name}")
                'Random doctorate degree name: Doctor of Philosophy'
        """
        if degree_type:
            degree_type = validate_degree_type(
                degree_type,
                self.valid_degree_types,
            )
        return random.choice(self.degree_provider.get_degree_names(degree_type))

    def degree_abbr(self, degree_type: str | None = None) -> str:
        """Generates a random degree abbreviation, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            str: A random degree abbreviation.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> degree_abbr = naija.degree_abbr()
                >>> print(f"Random degree abbreviation: {degree_abbr}")
                'Random degree abbreviation: B.Sc.'

                >>> degree_abbr = naija.degree_abbr(degree_type="masters")
                >>> print(f"Random masters degree abbreviation: {degree_abbr}")
                'Random masters degree abbreviation: MBA'
        """
        if degree_type:
            degree_type = validate_degree_type(
                degree_type,
                self.valid_degree_types,
            )
        return random.choice(self.degree_provider.get_degree_abbrs(degree_type))
