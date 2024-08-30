"""This module provides a SchoolProvider class for accessing information about schools in Nigeria from a JSON file."""

from pathlib import Path

from fakernaija.providers.state import StateProvider
from fakernaija.utils import load_json, normalize_input


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
        self.ownerships = ["federal", "state", "private"]
        self.school_types = ["university", "polytechnic", "college"]
        self.state_provider = StateProvider()
        self.state_names = self.state_provider.get_state_names()

    def get_schools(
        self,
        ownership: str | None = None,
        state: str | None = None,
        school_type: str | None = None,
    ) -> list[dict[str, str]]:
        """Get all schools based on filters for ownership, state, and school_type.

        Args:
            ownership (str | None): Filter by ownership ('federal', 'state', 'private').
            state (str | None): Filter by state.
            school_type (str | None): Filter by type ('university', 'polytechnic', 'college').

        Returns:
            list[dict[str, str]]: A list of dictionaries representing matching schools.

        Raises:
            ValueError: If an unsupported ownership, state, or school_type is provided.
        """
        ownership = normalize_input(ownership)
        school_type = normalize_input(school_type)
        state = normalize_input(state)

        # Ensure that the state name comparison is case-insensitive
        if state:
            matching_state_names = [s.lower() for s in self.state_names]
            if state.lower() not in matching_state_names:
                msg = f"Invalid state name: {state}. Valid states are: {', '.join(self.state_names)}"
                raise ValueError(msg)
        if ownership and ownership not in self.ownerships:
            msg = f"Unsupported ownership: {ownership}. Supported values are: {', '.join(self.ownerships)}"
            raise ValueError(msg)
        if school_type and school_type not in self.school_types:
            msg = f"Unsupported school type: {school_type}. Supported values are: {', '.join(self.school_types)}"
            raise ValueError(msg)

        filtered_schools = self.schools_data

        if ownership:
            filtered_schools = [
                school
                for school in filtered_schools
                if school.get("ownership", "").lower() == ownership
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
                if school.get("type", "").lower() == school_type
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

        Raises:
            ValueError: If an unsupported ownership or state or school_type is provided.
        """
        return [
            school["acronym"] if acronym else school["name"]
            for school in self.get_schools(ownership, state, school_type)
        ]
