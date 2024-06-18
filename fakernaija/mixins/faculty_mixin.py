"""Faculty mixin to group related methods for the FacultyProvider."""

import random

from fakernaija.providers.faculty_provider import FacultyProvider


class Faculty:
    """Methods for the FacultyProvider."""

    def __init__(self) -> None:
        """Initializes the Faculty mixin and its provider."""
        self.faculty_provider = FacultyProvider()

    def faculty(self) -> dict[str, list[str]]:
        """Get a random faculty with its departments.

        Returns:
            dict[str, list[str]]: A dictionary with faculty name and list of departments.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> faculty = naija.faculty()
                >>> print(f"Random faculty: {faculty}")
                "Random faculty: {'name': 'Basic Medical Sciences', 'departments': ['Human Anatomy', 'Physiology']}"
        """
        faculty = random.choice(self.faculty_provider.faculties_data)
        return {"faculty_name": faculty["name"], "departments": faculty["departments"]}

    def faculty_name(self) -> str:
        """Get a random faculty name.

        Returns:
            str: A random faculty name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> faculty_name = naija.faculty_name()
                >>> print(f"Random faculty name: {faculty_name}")
                'Random faculty name: Basic Medical Sciences'
        """
        faculties = self.faculty_provider.get_faculties()
        return random.choice(faculties)

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
        return random.choice(departments)

    def department_by_faculty(self, faculty: str) -> str:
        """Get a random department by a given faculty.

        Args:
            faculty (str): The name of the faculty.

        Returns:
            str: A random department from the specified faculty.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> department = naija.department_by_faculty('Basic Medical Sciences')
                >>> print(f"Random department: {department}")
                'Random department: Human Anatomy'
        """
        for fac in self.faculty_provider.faculties_data:
            if fac["name"].lower() == faculty.lower():
                return random.choice(fac["departments"])
        msg = f"Faculty '{faculty}' not found"
        raise ValueError(msg)
