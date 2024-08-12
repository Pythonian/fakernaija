"""This module provides a SchoolProvider class for accessing information about schools in Nigeria from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json


class SchoolProvider:
    """A class to provide information about Schools in Nigeria."""

    def __init__(self) -> None:
        """Initializes the SchoolProvider by loading the school data."""
        self.data_path = Path(__file__).parent.parent / "data" / "schools.json"
        self.schools_data = load_json(
            self.data_path,
            [
                "name",
                "acronym",
                "state",
                "type",
                "ownership",
            ],
        )

    def get_schools(
        self,
        ownership: str | None = None,
        state: str | None = None,
        school_type: str | None = None,
    ) -> list[dict[str, str]]:
        """Get all schools based on filters for ownership, state, and type.

        Args:
            ownership (str | None): Filter by ownership ('federal', 'state', 'private').
            state (str | None): Filter by state.
            school_type (str | None): Filter by type ('university', 'polytechnic', 'college').

        Returns:
            list[dict[str, str]]: A list of dictionaries representing matching schools.
        """
        filtered_schools = self.schools_data

        if ownership:
            filtered_schools = [
                school
                for school in filtered_schools
                if school.get("ownership", "") == ownership.capitalize()
            ]
        if state:
            filtered_schools = [
                school
                for school in filtered_schools
                if school.get("state", "").lower() == state.lower()
            ]
        if school_type:
            filtered_schools = [
                school
                for school in filtered_schools
                if school.get("type", "").lower() == school_type.lower()
            ]

        return filtered_schools

    def get_school_names(
        self,
        ownership: str | None = None,
        state: str | None = None,
        school_type: str | None = None,
        acronym: bool = False,
    ) -> list[str]:
        """Get all school names based on filters and optionally return the acronym.

        Args:
            ownership (str | None): Filter by ownership ('federal', 'state', 'private').
            state (str | None): Filter by state.
            school_type (str | None): Filter by type ('university', 'polytechnic', 'college').
            acronym (bool): Return the school's acronym instead of the full name.

        Returns:
            list[str]: A list of school names or acronyms.
        """
        schools = self.get_schools(ownership, state, school_type)
        return [school["acronym"] if acronym else school["name"] for school in schools]
