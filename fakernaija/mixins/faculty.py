"""Faculty mixin to group related methods for the FacultyProvider."""

import random

from fakernaija.providers import FacultyProvider
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
            dict[str, list[str]]: A dictionary with faculty name and
                list of departments.

        Example:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> faculty = naija.faculty()
                >>> print(f"Random faculty: {faculty}")
                Random faculty: {'faculty_name': 'Basic Medical Sciences', 'departments': ['Human Anatomy', 'Physiology']}
        """
        faculty = random.choice(self.faculty_provider.faculties_data)
        return {
            "faculty_name": faculty["name"],
            "departments": faculty["departments"],
        }

    def faculty_name(self) -> str:
        """Get a random faculty name.

        Returns:
            str: A random faculty name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

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
        faculty_name = get_unique_value(
            faculty_names,
            self._used_faculty_names,
        )
        self._used_faculty_names.add(faculty_name)
        return faculty_name

    def department_name(self, faculty: str | None = None) -> str:
        """Get a random department name.

        Args:
            faculty (str | None, optional): The name of the faculty to filter
                departments. Defaults to None.

        Returns:
            str: A random department name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> department_name = naija.department_name()
                >>> print(f"Random department name: {department_name}")
                Random department name: Accounting

                >>> for _ in range(3):
                ...     print(naija.department_name())
                ...
                Biotechnology
                Public Health
                Furniture Design

                >>> department_name = naija.department_name(faculty="Social Sciences")
                >>> print(f"Random department in a specific Faculty: {department_name}")
                Random department in a specific Faculty: Psychology
        """
        department_names = self.faculty_provider.get_department_names(faculty)
        department_name = get_unique_value(
            department_names,
            self._used_department_names,
        )
        self._used_department_names.add(department_name)
        return department_name
