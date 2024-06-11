"""This module provides a SchoolProvider class for accessing information about schools in Nigeria from a JSON file."""

from pathlib import Path
from typing import Any

from fakernaija.utils import load_json


class SchoolProvider:
    """A class to provide information about Schools in Nigeria."""

    def __init__(self) -> None:
        """Initializes the SchoolProvider.

        Sets the path to the directory containing schools data.
        """
        self.data_path = Path(__file__).parent / "data" / "schools.json"
        self.schools_data = load_json(
            self.data_path,
            [
                "name",
                "acronym",
                "location",
                "type",
                "ownership",
                "year_founded",
            ],
        )

    def get_schools(self) -> list[str]:
        """Get a list of all the schools' names.

        Returns:
            list[str]: A list of school names.
        """
        return [school["name"] for school in self.schools_data]

    def get_school_by_name(self, name: str) -> dict[str, Any] | None:
        """Get information about a school by its name.

        Args:
            name (str): The name of the school.

        Returns:
            dict[str, Any] | None: Information about the school or None if not found.
        """
        for school in self.schools_data:
            if school["name"] == name:
                return school
        return None

    def _filter_schools(self, **filters: str) -> list[dict[str, Any]]:
        """Filter schools based on provided criteria.

        Args:
            **filters (Any): Key-value pairs to filter schools by.

        Returns:
            list[dict[str, Any]]: A list of filtered schools.
        """
        results = self.schools_data
        for key, value in filters.items():
            results = [school for school in results if school.get(key) == value]
        return results

    def get_school_acronyms(self) -> list[str]:
        """Get a list of all school acronyms.

        Returns:
            list[str]: A list of school acronyms.
        """
        return [school["acronym"] for school in self.schools_data]

    def get_schools_by_location(self, location: str) -> list[dict[str, Any]]:
        """Get a list of schools located at the specified location.

        Args:
            location (str): The location to filter schools by.

        Returns:
            list[dict[str, Any]]: A list of schools at the specified location.
        """
        return self._filter_schools(location=location)

    def get_federal_schools(self) -> list[dict[str, Any]]:
        """Get a list of all federal schools.

        Returns:
            list[dict[str, Any]]: A list of federal schools.
        """
        return self._filter_schools(ownership="Federal")

    def get_state_schools(self) -> list[dict[str, Any]]:
        """Get a list of all state schools.

        Returns:
            list[dict[str, Any]]: A list of state schools.
        """
        return self._filter_schools(ownership="State")

    def get_private_schools(self) -> list[dict[str, Any]]:
        """Get a list of all private schools.

        Returns:
            list[dict[str, Any]]: A list of private schools.
        """
        return self._filter_schools(ownership="Private")

    def get_universities(self) -> list[dict[str, Any]]:
        """Get a list of all universities.

        Returns:
            list[dict[str, Any]]: A list of universities.
        """
        return self._filter_schools(type="University")

    def get_universities_by_location(self, location: str) -> list[dict[str, Any]]:
        """Get a list of universities at a specific location.

        Args:
            location (str): The location to filter universities.

        Returns:
            list[dict[str, Any]]: A list of universities at the specified location.
        """
        return self._filter_schools(location=location, type="University")

    def get_polytechnics(self) -> list[dict[str, Any]]:
        """Get a list of all the polytechnics.

        Returns:
            list[dict[str, Any]]: A list of polytechnics.
        """
        return self._filter_schools(type="Polytechnic")

    def get_polytechnics_by_location(self, location: str) -> list[dict[str, Any]]:
        """Get a list of polytechnics in a specific location.

        Args:
            location (str): The location to filter polytechnics.

        Returns:
            list[dict[str, Any]]: A list of polytechnics at the specified location.
        """
        return self._filter_schools(location=location, type="Polytechnic")

    def get_colleges_of_education(self) -> list[dict[str, Any]]:
        """Get a list of all colleges of education.

        Returns:
            list[dict[str, Any]]: A list of colleges of education.
        """
        return self._filter_schools(type="College of Education")

    def get_colleges_of_education_by_location(
        self,
        location: str,
    ) -> list[dict[str, Any]]:
        """Get a list of colleges of education at a specific location.

        Args:
            location (str): The location to filter colleges of education.

        Returns:
            list[dict[str, Any]]: A list of colleges of education at the specified location.
        """
        return self._filter_schools(location=location, type="College of Education")

    def get_federal_universities(self) -> list[dict[str, Any]]:
        """Get a list of all federal universities.

        Returns:
            list[dict[str, Any]]: A list of federal universities.
        """
        return self._filter_schools(type="University", ownership="Federal")

    def get_federal_polytechnics(self) -> list[dict[str, Any]]:
        """Get a list of all federal polytechnics.

        Returns:
            list[dict[str, Any]]: A list of federal polytechnics.
        """
        return self._filter_schools(type="Polytechnic", ownership="Federal")

    def get_federal_colleges_of_education(self) -> list[dict[str, Any]]:
        """Get a list of all federal colleges of education.

        Returns:
            list[dict[str, Any]]: A list of federal colleges of education.
        """
        return self._filter_schools(type="College of Education", ownership="Federal")

    def get_state_universities(self) -> list[dict[str, Any]]:
        """Get a list of all state universities.

        Returns:
            list[dict[str, Any]]: A list of state universities.
        """
        return self._filter_schools(type="University", ownership="State")

    def get_state_polytechnics(self) -> list[dict[str, Any]]:
        """Get a list of all state polytechnics.

        Returns:
            list[dict[str, Any]]: A list of state polytechnics.
        """
        return self._filter_schools(type="Polytechnic", ownership="State")

    def get_state_colleges_of_education(self) -> list[dict[str, Any]]:
        """Get a list of all state colleges of education.

        Returns:
            list[dict[str, Any]]: A list of state colleges of education.
        """
        return self._filter_schools(type="College of Education", ownership="State")

    def get_private_universities(self) -> list[dict[str, Any]]:
        """Get a list of all private universities.

        Returns:
            list[dict[str, Any]]: A list of private universities.
        """
        return self._filter_schools(type="University", ownership="Private")

    def get_private_polytechnics(self) -> list[dict[str, Any]]:
        """Get a list of all private polytechnics.

        Returns:
            list[dict[str, Any]]: A list of private polytechnics.
        """
        return self._filter_schools(type="Polytechnic", ownership="Private")

    def get_private_colleges_of_education(self) -> list[dict[str, Any]]:
        """Get a list of all private colleges of education.

        Returns:
            list[dict[str, Any]]: A list of dictionaries of private colleges of education.
        """
        return self._filter_schools(type="College of Education", ownership="Private")


class DegreeProvider:
    """A class to provide information about Degrees awarded in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the DegreeProvider.

        Sets the path to the directory containing degrees data.
        """
        self.data_path = Path(__file__).parent / "data" / "degrees.json"
        self.degrees_data = load_json(
            self.data_path,
            [
                "name",
                "degree_type",
                "initials",
            ],
        )

    def get_degrees(self) -> list[str]:
        """Get a list of all the degrees.

        Returns:
            list[str]: A list of degrees.
        """
        return [degree["name"] for degree in self.degrees_data]

    def _get_degrees_by_type(self, degree_type: str) -> list[str]:
        """Filter degrees based on degree type.

        Args:
            degree_type (str): The degree type value to filter by.

        Returns:
            list[str]: A list of filtered degrees.
        """
        return [
            degree["name"]
            for degree in self.degrees_data
            if degree["degree_type"] == degree_type
        ]

    def get_undergraduate_degrees(self) -> list[str]:
        """Get a list of all undergraduate degrees.

        Returns:
            list[str]: A list of undergraduate degrees.
        """
        return self._get_degrees_by_type(degree_type="undergraduate")

    def get_masters_degrees(self) -> list[str]:
        """Get a list of all masters degrees.

        Returns:
            list[str]: A list of masters degrees.
        """
        return self._get_degrees_by_type(degree_type="masters")

    def get_doctorate_degrees(self) -> list[str]:
        """Get a list of all doctorate degrees.

        Returns:
            list[str]: A list of doctorate degrees.
        """
        return self._get_degrees_by_type(degree_type="doctorate")


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
