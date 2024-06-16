"""Faculty mixin to group related methods for the FacultyProvider."""

import random

from fakernaija.providers.faculty_provider import FacultyProvider


class Faculty:
    """Methods for the FacultyProvider."""

    def __init__(self) -> None:
        """Initializes the Faculty mixin and its provider."""
        self.faculty_provider = FacultyProvider()
        self._used_faculties: set[str] = set()
        self._used_departments: set[str] = set()

    def faculty(self) -> str:
        """Get a random faculty.

        Returns:
            str: A random faculty.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> faculty = naija.faculty()
                >>> print(f"Random faculty: {faculty}")
                'Random faculty: Architecture'
        """
        faculties = self.faculty_provider.get_faculties()
        faculty = self._get_unique_value(faculties, self._used_faculties)
        self._used_faculties.add(faculty)
        return faculty

    def department(self) -> str:
        """Get a random department.

        Returns:
            str: A random department.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> department = naija.department()
                >>> print(f"Random department: {department}")
                'Random department: Accounting'
        """
        departments = self.faculty_provider.get_departments()
        department = self._get_unique_value(departments, self._used_departments)
        self._used_departments.add(department)
        return department

    def _get_unique_value(self, values: list[str], used_values: set[str]) -> str:
        """Helper method to get a unique value from a list of values.

        Args:
            values (list[str]): The list of possible values.
            used_values (set[str]): The set of values that have already been used.

        Returns:
            str: A unique value from the list.
        """
        available_values = set(values) - used_values
        if not available_values:
            # If all values have been used, reset the used values set
            used_values.clear()
            available_values = set(values)
        return random.choice(list(available_values))
