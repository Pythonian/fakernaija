"""This module provides a StateProvider class for accessing information about states in Nigeria from a JSON file."""

from pathlib import Path
from typing import Any

from fakernaija.utils import load_json


class StateProvider:
    """A class to provide information about states and their attributes."""

    def __init__(self) -> None:
        """Initializes the StateProvider instance by loading state data from a JSON file."""
        self.data_path = Path(__file__).parent.parent / "data" / "states.json"
        self.states_data = load_json(
            self.data_path,
            [
                "name",
                "code",
                "capital",
                "slogan",
                "lgas",
                "region",
                "postal_code",
            ],
        )
        # Generate region initials dynamically
        self._generate_region_abbrs()

    def _get_state(self, state_name: str) -> dict[str, Any]:
        """Get state information by state name and raise an error if not found."""
        for state in self.states_data:
            if state["name"].lower() == state_name.lower():
                return state
        msg = f"State '{state_name}' does not exist in Nigeria."
        raise ValueError(msg)

    def _generate_region_abbrs(self) -> list[dict[str, str]]:
        """Generate unique region abbreviations dynamically based on the region name."""
        unique_regions = {}
        for state in self.states_data:
            region = state["region"]
            region_abbr = "".join(word[0].upper() for word in region.split())
            state["region_abbr"] = region_abbr
            if region_abbr not in unique_regions:
                unique_regions[region_abbr] = region
        return [{"abbr": key, "name": value} for key, value in unique_regions.items()]

    def get_states(self) -> list[dict[str, str]]:
        """Get a list of all states.

        Returns:
            list[dict[str, str]]: A list of states.
        """
        return self.states_data

    def get_state_names(self) -> list[str]:
        """Get a list of all state names.

        Returns:
            list[str]: A list of state names.
        """
        return [state["name"] for state in self.states_data]

    def get_slogans(self) -> list[str]:
        """Get the slogans of all states.

        Returns:
            list[str]: A list of state slogans.
        """
        return [state["slogan"] for state in self.states_data]

    def get_shortcodes(self) -> list[str]:
        """Get the shortcodes of all states.

        Returns:
            list[str]: A list of state shortcodes.
        """
        return [state["code"] for state in self.states_data]

    def get_capitals(self) -> list[str]:
        """Get a list of all state capitals.

        Returns:
            list[str]: A list of state capitals.
        """
        return [state["capital"] for state in self.states_data]

    def get_lgas(self) -> list[str]:
        """Get a list of all Local Government Areas for all states.

        Returns:
            list[str]: A list of all LGAs for all states.
        """
        return [lga for state in self.states_data for lga in state["lgas"]]

    def get_regions(self) -> list[dict[str, str]]:
        """Get a list of all geopolitical regions.

        Returns:
            list[dict[str, str]]: A list of unique regions with their initials.
        """
        return [
            {"abbr": state["region_abbr"], "name": state["region"]}
            for state in self.states_data
        ]

    def get_postal_codes(self) -> list[str]:
        """Get a list of all postal codes of states.

        Returns:
            list[str]: A list of all postal codes.
        """
        return [state["postal_code"] for state in self.states_data]

    def get_states_by_region(self, region_abbr: str) -> list[dict[str, str]]:
        """Get states by a specific region code.

        Args:
            region_abbr (str): The code of the region to filter states.

        Returns:
            list[dict[str, str]]: A list of states belonging to the specified region code.
        """
        return [
            state
            for state in self.states_data
            if state["region_abbr"].upper() == region_abbr.upper()
        ]

    def get_state_by_name(self, state_name: str) -> dict[str, str] | None:
        """Get state information by state name.

        Args:
            state_name (str): The name of the state.

        Returns:
            dict[str, str] | None: Information about the specified state, or None if not found.
        """
        try:
            return self._get_state(state_name)
        except ValueError:
            return None

    def get_postal_code_by_state(self, state_name: str) -> str | None:
        """Get the postal code of a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            str | None: The postal code of the specified state, or None if not found.
        """
        try:
            state_info = self._get_state(state_name)
            return state_info["postal_code"]
        except ValueError:
            return None

    def get_state_lgas(self, state_name: str) -> list[str]:
        """Get a list of Local Government Areas for a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            list[str]: A list of LGAs for the specified state.
        """
        try:
            state_info = self._get_state(state_name)
            return state_info["lgas"]
        except ValueError:
            return []
