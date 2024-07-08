"""Degree mixin to group related methods for the DegreeProvider."""

import random

from fakernaija.providers.degree_provider import DegreeProvider
from fakernaija.utils import get_unique_value, validate_degree_type


class Degree:
    """Methods for the DegreeProvider."""

    def __init__(self) -> None:
        """Initializes the Degree mixin and its provider."""
        self.degree_provider = DegreeProvider()
        self.valid_degree_types = ["undergraduate", "masters", "doctorate"]
        self._used_degree_names: set[str] = set()
        self._used_degree_abbrs: set[str] = set()
        self._used_degree_name_by_types: set[str] = set()
        self._used_degree_abbr_by_types: set[str] = set()

    def degree(self) -> dict:
        """Generates a random degree.

        Returns:
            dict: A random degree dictionary.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree = naija.degree()
                >>> print(f"Random degree: {degree}")
                'Random degree: {'name': 'Bachelor of Science', 'degree_type': 'undergraduate', 'abbr': 'B.Sc.'}'
        """
        degrees = self.degree_provider.get_degrees()
        return random.choice(degrees)

    def degree_name(self) -> str:
        """Generates a random degree name.

        Returns:
            str: A random degree name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree_name = naija.degree_name()
                >>> print(f"Random degree name: {degree_name}")
                'Random degree name: Bachelor of Science'
        """
        degree_names = self.degree_provider.get_degree_names()
        degree_name = get_unique_value(degree_names, self._used_degree_names)
        self._used_degree_names.add(degree_name)
        return degree_name

    def degree_abbr(self) -> str:
        """Generates a random degree abbreviation.

        Returns:
            str: A random degree abbreviation.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree_abbr = naija.degree_abbr()
                >>> print(f"Random degree abbreviation: {degree_abbr}")
                'Random degree abbreviation: B.Sc.'
        """
        degree_abbrs = self.degree_provider.get_degree_abbrs()
        degree_abbr = get_unique_value(degree_abbrs, self._used_degree_abbrs)
        self._used_degree_abbrs.add(degree_abbr)
        return degree_abbr

    def degree_name_by_type(self, degree_type: str) -> str:
        """Generates a random degree name filtered by degree type.

        Args:
            degree_type (str): The type of degree to filter by.

        Returns:
            str: A random degree name filtered by type.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree_name = naija.degree_name_by_type("undergraduate")
                >>> print(f"Random undergraduate degree name: {degree_name}")
                'Random undergraduate degree name: Bachelor of Science'
        """
        degree_type = validate_degree_type(degree_type, self.valid_degree_types)
        degree_names = self.degree_provider.get_degree_names(degree_type)
        degree_name = get_unique_value(degree_names, self._used_degree_name_by_types)
        self._used_degree_name_by_types.add(degree_name)
        return degree_name

    def degree_abbr_by_type(self, degree_type: str) -> str:
        """Generates a random degree abbreviation filtered by degree type.

        Args:
            degree_type (str): The type of degree to filter by.

        Returns:
            str: A random degree abbreviation filtered by type.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree_abbr = naija.degree_abbr_by_type("undergraduate")
                >>> print(f"Random undergraduate degree abbreviation: {degree_abbr}")
                'Random undergraduate degree abbreviation: B.Sc.'
        """
        degree_type = validate_degree_type(degree_type, self.valid_degree_types)
        degree_abbrs = self.degree_provider.get_degree_abbrs(degree_type)
        degree_abbr = get_unique_value(degree_abbrs, self._used_degree_abbr_by_types)
        self._used_degree_abbr_by_types.add(degree_abbr)
        return degree_abbr
