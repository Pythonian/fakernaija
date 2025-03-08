"""This module provides a FacultyProvider class for accessing information about faculties and departments in Nigerian schools from a JSON file.

Resource link: https://punchng.com/full-list-newly-restructured-programmes-in-nigerian-varsities/
"""

import difflib
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
        self.faculty_names = [faculty["name"] for faculty in self.faculties_data]

    def get_faculty_names(self) -> list[str]:
        """Get a list of all faculty names.

        Returns:
            list[str]: A list of faculty names.
        """
        return self.faculty_names

    def get_department_names(self, faculty: str | None = None) -> list[str]:
        """Get a list of department names. Optionally filter by faculty.

        Args:
            faculty (str, optional): The name of the faculty. Defaults to None.

        Returns:
            list[str]: A list of department names.

        Raises:
            ValueError: If the faculty name is invalid.
        """
        if faculty and faculty is not None:
            # Normalize faculty names for case-insensitive comparison
            faculty_dict = {f.lower(): f for f in self.faculty_names}

            if faculty.lower() not in faculty_dict:
                # Find close matches to the input faculty name
                suggestions = difflib.get_close_matches(
                    faculty, self.faculty_names, n=3, cutoff=0.6
                )
                msg = (
                    f"Invalid faculty name: {faculty}. Did you mean: {', '.join(suggestions)}?"
                    if suggestions
                    else f"Invalid faculty name: {faculty}. Valid faculties are: {', '.join(self.faculty_names)}"
                )
                raise ValueError(msg)

            faculty_name = faculty_dict[faculty.lower()]
            for fac in self.faculties_data:
                if fac["name"] == faculty_name:
                    return fac["departments"]

        # Return all departments if no faculty is specified
        departments = []
        for fac in self.faculties_data:
            departments.extend(fac["departments"])
        return departments
