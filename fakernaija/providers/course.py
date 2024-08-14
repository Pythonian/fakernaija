"""This module provides a CourseProvider class for accessing information about courses taken in Nigerian schools from a JSON file.

Resource link: https://entangle-pair.blogspot.com/2014/07/academic-programmes-and-course-outline.html
"""

from pathlib import Path

from fakernaija.utils import load_json


class CourseProvider:
    """A provider class to manage and access Nigerian school courses data.

    This class loads course data from a JSON file and provides methods to retrieve
    course data.

    Attributes:
        data_path (Path): The path to the directory containing the courses JSON data.
        courses_data (list[dict[str, str]]): The loaded course data, each entry containing
            the course name and code.

    Data Structure:
        .. code-block:: python

            [
                {"name": "Introduction to Computer Science", "code": "COS101"},
                {"name": "Introduction to Computer Systems", "code": "COS102"},
            ]
    """

    def __init__(self) -> None:
        """Initializes the CourseProvider.

        Sets the path to the directory containing Courses data.
        """
        self.data_path = Path(__file__).parent.parent / "data" / "courses.json"
        self.courses_data = load_json(self.data_path, ["name", "code"])

    def get_courses_name(self) -> list[str]:
        """Get a list of all course names.

        Returns:
            list[str]: A list of course names.
        """
        return [course["name"] for course in self.courses_data]

    def get_courses_code(self) -> list[str]:
        """Get a list of all the courses code.

        Returns:
            list[str]: A list of courses code.
        """
        return [course["code"] for course in self.courses_data]

    def get_courses(self) -> list[dict[str, str]]:
        """Get a list of all courses with their names and codes.

        Returns:
            list[dict[str, str]]: A list of courses with their names and codes.
        """
        return self.courses_data
