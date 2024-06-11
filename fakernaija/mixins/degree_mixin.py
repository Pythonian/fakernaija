"""DegreeMixin to group related methods for the DegreeProvider."""

import random

from fakernaija.providers.education import DegreeProvider


class Degree:
    """Methods for the DegreeProvider."""

    def __init__(self) -> None:
        """Initializes the Degree mixin and its provider."""
        self.degree_provider = DegreeProvider()

    def degree(self) -> str:
        """Generates a random degree.

        Returns:
            str: A random degree.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> degree = naija.degree()
                >>> print(f"Random degree: {degree}")
                'Random degree: Bachelor of Science in Computer Science'
        """
        degrees = self.degree_provider.get_degrees()
        return random.choice(degrees)

    def undergraduate_degree(self) -> str:
        """Generates a random undergraduate degree.

        Returns:
            str: A random undergraduate degree.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> undergrad_degree = naija.undergraduate_degree()
                >>> print(f"Random undergraduate degree: {undergrad_degree}")
                'Random undergraduate degree: Bachelor of Science in Biology'
        """
        degrees = self.degree_provider.get_undergraduate_degrees()
        return random.choice(degrees)

    def masters_degree(self) -> str:
        """Generates a random masters degree.

        Returns:
            str: A random masters degree.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> masters_degree = naija.masters_degree()
                >>> print(f"Random masters degree: {masters_degree}")
                'Random masters degree: Master of Science in Economics'
        """
        degrees = self.degree_provider.get_masters_degrees()
        return random.choice(degrees)

    def doctorate_degree(self) -> str:
        """Generates a random doctorate degree.

        Returns:
            str: A random doctorate degree.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> doctorate_degree = naija.doctorate_degree()
                >>> print(f"Random doctorate degree: {doctorate_degree}")
                'Random doctorate degree: Doctor of Philosophy in Physics'
        """
        degrees = self.degree_provider.get_doctorate_degrees()
        return random.choice(degrees)
