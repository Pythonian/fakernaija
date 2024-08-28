"""Degree mixin module.

This module defines a mixin class which groups related methods for
fetching and returning degree-related data from its provider.
"""

import random

from fakernaija.providers import DegreeProvider
from fakernaija.utils import get_unique_value


class Degree:
    """A mixin providing methods to fetch and return degree-related data."""

    def __init__(self) -> None:
        """Initializes the Degree mixin and sets up its provider."""
        self.degree_provider = DegreeProvider()
        self._used_degree_names: set[str] = set()
        self._used_degree_abbrs: set[str] = set()

    def degree(self, degree_type: str | None = None) -> dict:
        """Returns a random degree object, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            dict[str, str]: A dictionary with degree name, type and abbreviation.

        Raises:
            ValueError: If an unsupported degree type is passed to the parameter.

        Note:
            - Degree type options: undergraduate, masters, doctorate

        Example:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> degree = naija.degree()
                >>> print(f"Random degree: {degree}")
                Random degree: {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}

                >>> degree = naija.degree(degree_type="masters")
                >>> print(f"Random masters degree: {degree}")
                Random masters degree: {'name': 'Master of Business Administration', 'degree_type': 'masters', 'abbr': 'MBA'}
        """
        return random.choice(self.degree_provider.get_degrees(degree_type))

    def degree_name(self, degree_type: str | None = None) -> str:
        """Generates a random degree name, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            str: A random degree name.

        Raises:
            ValueError: If an unsupported degree type is passed to the parameter.

        Note:
            - Degree type options: undergraduate, masters, doctorate

        Example:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> degree_name = naija.degree_name()
                >>> print(f"Random degree name: {degree_name}")
                Random degree name: Bachelor of Science

                >>> degree_name = naija.degree_name(degree_type="doctorate")
                >>> print(f"Random doctorate degree name: {degree_name}")
                Random doctorate degree name: Doctor of Philosophy
        """
        degree_names = self.degree_provider.get_degree_names(degree_type)
        degree_name = get_unique_value(degree_names, self._used_degree_names)
        self._used_degree_names.add(degree_name)
        return degree_name

    def degree_abbr(self, degree_type: str | None = None) -> str:
        """Generates a random degree abbreviation, optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                Defaults to None.

        Returns:
            str: A random degree abbreviation.

        Raises:
            ValueError: If an unsupported degree type is passed to the parameter.

        Note:
            - Degree type options: undergraduate, masters, doctorate

        Example:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> degree_abbr = naija.degree_abbr()
                >>> print(f"Random degree abbreviation: {degree_abbr}")
                Random degree abbreviation: B.Sc.

                >>> degree_abbr = naija.degree_abbr(degree_type="masters")
                >>> print(f"Random masters degree abbreviation: {degree_abbr}")
                Random masters degree abbreviation: MBA
        """
        degree_abbrs = self.degree_provider.get_degree_abbrs(degree_type)
        degree_abbr = get_unique_value(degree_abbrs, self._used_degree_abbrs)
        self._used_degree_abbrs.add(degree_abbr)
        return degree_abbr
