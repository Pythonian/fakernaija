"""This module provides a StateProvider class for accessing information about states in Nigeria from a JSON file."""

from pathlib import Path
from typing import Any

from fakernaija.utils import load_json


class StateProvider:
    """A class to provide information about states and their attributes."""

    def __init__(self) -> None:
        """Initializes the StateProvider instance with data."""
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
        self._generate_region_abbrs()

    def _generate_region_abbrs(self) -> None:
        """Generate unique region abbreviations dynamically based on the region name."""
        for state in self.states_data:
            region = state["region"]
            region_abbr = "".join(word[0].upper() for word in region.split())
            state["region_abbr"] = region_abbr

    def _get_state(self, state_name: str) -> dict[str, Any]:
        """Get state information by state name and raise an error if not found."""
        for state in self.states_data:
            if state["name"].lower() == state_name.lower():
                return state
        available_states = ", ".join(self.get_state_names())
        msg = f"State '{state_name}' does not exist in Nigeria. Available states are: {available_states}."
        raise ValueError(msg)

    def validate_region(self, region: str) -> None:
        """Validate if the provided region is in the list of valid regions.

        Args:
            region (str): The region abbreviation to validate.

        Raises:
            ValueError: If the region is not valid.
        """
        valid_regions = {state["region_abbr"] for state in self.states_data}
        if region.upper() not in valid_regions:
            available_options = ", ".join(sorted(valid_regions))
            msg = f"Invalid region abbreviation: {region}. Available options are: {available_options}"
            raise ValueError(msg)

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
        return [state["name"] for state in self.get_states()]

    def get_capitals(self) -> list[str]:
        """Get a list of all state capitals.

        Returns:
            list[str]: A list of state capitals.
        """
        return [state["capital"] for state in self.get_states()]

    def get_lgas(self) -> list[str]:
        """Get a list of all Local Government Areas for all states.

        Returns:
            list[str]: A list of all LGAs for all states.
        """
        return [lga for state in self.get_states() for lga in state["lgas"]]

    def get_regions(self) -> list[dict[str, str]]:
        """Get a list of all geopolitical regions.

        Returns:
            list[dict[str, str]]: A list of unique regions with their initials.
        """
        return [
            {"abbr": state["region_abbr"], "name": state["region"]}
            for state in self.get_states()
        ]

    def get_postal_codes(self) -> list[str]:
        """Get a list of all postal codes of states.

        Returns:
            list[str]: A list of all postal codes.
        """
        return [state["postal_code"] for state in self.get_states()]

    def get_states_by_region(self, region_abbr: str) -> list[dict[str, str]]:
        """Get states by a specific region code.

        Args:
            region_abbr (str): The code of the region to filter states.

        Returns:
            list[dict[str, str]]: A list of states belonging to the specified region code.
        """
        return [
            state
            for state in self.get_states()
            if state["region_abbr"].upper() == region_abbr.upper()
        ]

    def get_postal_code_by_state(self, state_name: str) -> str:
        """Get the postal code of a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            str: The postal code of the specified state.

        Raises:
            ValueError: If the specified state does not exist.
        """
        state_info = self._get_state(state_name)
        return state_info["postal_code"]

    def get_state_lgas(self, state_name: str) -> list[str]:
        """Get a list of Local Government Areas for a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            list[str]: A list of LGAs for the specified state.

        Raises:
            ValueError: If the specified state does not exist.
        """
        state_info = self._get_state(state_name)
        return state_info["lgas"]
