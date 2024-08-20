"""Faculty mixin to group related methods for the FacultyProvider."""

import random

from fakernaija.providers.faculty import FacultyProvider
from fakernaija.utils import get_unique_value


class Faculty:
    """Methods for the FacultyProvider."""

    def __init__(self) -> None:
        """Initializes the Faculty mixin and its provider."""
        self.faculty_provider = FacultyProvider()
        self._used_faculty_names: set[str] = set()
        self._used_department_names: set[str] = set()

    def faculty(self) -> dict[str, list[str]]:
        """Get a random faculty object with its departments.

        Returns:
            dict[str, list[str]]: A dictionary with faculty name and list of departments.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> faculty = naija.faculty()
                >>> print(f"Random faculty: {faculty}")
                Random faculty: {'faculty_name': 'Basic Medical Sciences', 'departments': ['Human Anatomy', 'Physiology']}
        """
        faculty = random.choice(self.faculty_provider.faculties_data)
        return {"faculty_name": faculty["name"], "departments": faculty["departments"]}

    def faculty_name(self) -> str:
        """Get a random faculty name.

        Returns:
            str: A random faculty name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> faculty_name = naija.faculty_name()
                >>> print(f"Random faculty name: {faculty_name}")
                Random faculty name: Basic Medical Sciences

                >>> for _ in range(3):
                ...     print(naija.faculty_name())
                ...
                Administration and Management
                Social Sciences
                Basic Medical Sciences
        """
        faculty_names = self.faculty_provider.get_faculty_names()
        faculty_name = get_unique_value(faculty_names, self._used_faculty_names)
        self._used_faculty_names.add(faculty_name)
        return faculty_name

    def department_name(self) -> str:
        """Get a random department name.

        Returns:
            str: A random department name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> department_name = naija.department_name()
                >>> print(f"Random department name: {department_name}")
                Random department name: Accounting

                >>> for _ in range(3):
                ...     print(naija.department_name())
                ...
                Biotechnology
                Public Health
                Furniture Design
        """
        department_names = self.faculty_provider.get_department_names()
        department_name = get_unique_value(
            department_names,
            self._used_department_names,
        )
        self._used_department_names.add(department_name)
        return department_name

    def department_by_faculty(self, faculty: str) -> str:
        """Get a random department name by a given faculty.

        Args:
            faculty (str): The name of the faculty.

        Returns:
            str: A random department name from the specified faculty.

        Raises:
            ValueError: If the provided faculty is not found.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> department = naija.department_by_faculty('Basic Medical Sciences')
                >>> print(f"Random department: {department}")
                Random department: Human Anatomy
        """
        for fac in self.faculty_provider.faculties_data:
            if fac["name"].lower() == faculty.lower():
                return random.choice(fac["departments"])
        msg = f"Faculty '{faculty}' not found"
        raise ValueError(msg)
