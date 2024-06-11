"""This module provides a CourseProvider class for accessing information about courses taken in Nigerian schools from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json


class CourseProvider:
    """A class to provide information about Courses taken in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the CourseProvider.

        Sets the path to the directory containing Courses data.
        """
        self.data_path = Path(__file__).parent / "data" / "courses.json"
        self.courses_data = load_json(
            self.data_path,
            [
                "name",
                "department",
                "code",
                "faculty",
                "credit_units",
                "level",
                "semester",
            ],
        )

    def get_courses(self) -> list[str]:
        """Get a list of all the courses.

        Returns:
            list[str]: A list of courses.
        """
        return [course["name"] for course in self.courses_data]
