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
                "lgas",
                "region",
                "region_initial",
                "postal_code",
            ],
        )

    def get_states(self) -> list[str]:
        """Get a list of all state names.

        Returns:
            list[str]: A list of state names.
        """
        return [state["name"] for state in self.states_data]

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

    def get_regions(self) -> list[str]:
        """Get a list of all geopolitical regions.

        Returns:
            list[str]: A list of unique regions.
        """
        return list(
            {state["region"] for state in self.states_data},
        )

    def get_postal_codes(self) -> list[str]:
        """Get a list of all postal codes of states.

        Returns:
            list[str]: A list of all postal codes.
        """
        return [state["postal_code"] for state in self.states_data]

    def get_states_by_region(self, region_initial: str) -> list[dict[str, Any]]:
        """Get states by a specific region code.

        Args:
            region_initial (str): The code of the region to filter states.

        Returns:
            list[dict[str, Any]]: A list of states belonging to the specified region code.
        """
        return [
            state
            for state in self.states_data
            if state["region_initial"] == region_initial
        ]

    def get_state_by_name(self, state_name: str) -> dict[str, Any] | None:
        """Get state information by state name.

        Args:
            state_name (str): The name of the state.

        Returns:
            dict[str, Any] | None: Information about the specified state, or None if not found.
        """
        for state in self.states_data:
            if state["name"].lower() == state_name.lower():
                return state
        return None

    def get_postal_code_by_state(self, state_name: str) -> str | None:
        """Get the postal code of a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            str | None: The postal code of the specified state, or None if not found.
        """
        state_info = self.get_state_by_name(state_name)
        return state_info.get("postal_code") if state_info else None

    def get_state_capital(self, state: str) -> str | None:
        """Get the capital city of a specific state.

        Args:
            state (str): The name of the state.

        Returns:
            str | None: The capital city of the specified state, or None if not found.
        """
        state_info = self.get_state_by_name(state)
        return state_info.get("capital") if state_info else None

    def get_state_lgas(self, state_name: str) -> list[str]:
        """Get a list of Local Government Areas for a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            list[str]: A list of LGAs for the specified state.
        """
        state_info = self.get_state_by_name(state_name)
        return state_info.get("lgas", []) if state_info else []
