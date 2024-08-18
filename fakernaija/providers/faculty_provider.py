"""This module provides a FacultyProvider class for accessing information about faculties and departments in Nigerian schools from a JSON file.

Resource link: https://punchng.com/full-list-newly-restructured-programmes-in-nigerian-varsities/
"""

from pathlib import Path

from fakernaija.utils import load_json


class FacultyProvider:
    """A class to provide information about Faculties and Departments in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the FacultyProvider.

        Sets the path to the directory containing Faculties data.
        """
        self.data_path = Path(__file__).parent.parent / "data" / "faculties.json"
        self.faculties_data = load_json(
            self.data_path,
            [
                "name",
                "departments",
            ],
        )

    def get_faculty_names(self) -> list[str]:
        """Get a list of all faculty names.

        Returns:
            list[str]: A list of faculty names.
        """
        return [faculty["name"] for faculty in self.faculties_data]

    def get_department_names(self) -> list[str]:
        """Get a list of all department names.

        Returns:
            list[str]: A list of department names.
        """
        departments = []
        for faculty in self.faculties_data:
            departments.extend(faculty["departments"])
        return departments
