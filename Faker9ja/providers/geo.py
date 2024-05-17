import json
import os


class GeoProvider:
    """
    A class to provide information about states and their attributes.
    """

    def __init__(self):
        """Initializes the GeoProvider instance."""

        # The path to the JSON file containing state data.
        self.data_path = os.path.join(
            os.path.dirname(__file__), "data", "geo", "states.json"
        )
        # Loads the json data into the states_data variable
        self.states_data = self.load_json(self.data_path)

    def load_json(self, file_path):
        """
        Load JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The loaded JSON data.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_states(self):
        """
        Get a list of all states.

        Returns:
            list: A list of state names.
        """
        return [state["name"] for state in self.states_data["states"]]

    def get_shortcodes(self):
        """
        Get the shortcodes of all states.

        Returns:
            list: A list of state shortcodes.
        """
        return [state["code"] for state in self.states_data["states"]]

    def get_capitals(self):
        """
        Get a list of all state capitals.

        Returns:
            list: A list of state capitals.
        """
        return [state["capital"] for state in self.states_data["states"]]

    def get_lgas(self):
        """
        Get a list of all Local Government Areas for all states.

        Returns:
            list: A list of all LGAs for all states.
        """
        # return [state["lgas"] for state in self.states_data["states"]]
        all_lgas = []
        for state in self.states_data["states"]:
            all_lgas.extend(state["lgas"])
        return all_lgas

    def get_regions(self):
        """
        Get a list of all geopolitical regions.

        Returns:
            list: A list of unique region codes.
        """
        return [state["region_initial"] for state in self.states_data["states"]]

    def get_postal_codes(self):
        """
        Get a list of all postal codes of states.

        Returns:
            list: A list of all postal codes.
        """
        return [state["postal_code"] for state in self.states_data["states"]]

    def get_states_by_region(self, region_initial):
        """
        Get states by a specific region code.

        Args:
            region_initial (str): The code of the region to filter states.

        Returns:
            list: A list of states belonging to the specified region code.
        """
        return [
            state
            for state in self.states_data["states"]
            if state["region_initial"] == region_initial
        ]

    def get_state_by_name(self, state_name):
        """
        Get state information by state name.

        Args:
            state_name (str): The name of the state.

        Returns:
            dict: Information about the specified state, or None if not found.
        """
        for state in self.states_data["states"]:
            if state["name"].lower() == state_name.lower():
                return state
        return None

    def get_postal_code_by_state(self, state_name):
        """
        Get the postal code of a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            str: The postal code of the specified state, or None if not found.
        """
        state_info = self.get_state_by_name(state_name)
        if state_info:
            return state_info.get("postal_code")
        else:
            return None

    def get_state_capital(self, state):
        """
        Get the capital city of a specific state.

        Args:
            state (str): The name of the state.

        Returns:
            str or None:
                The capital city of the specified state, or None if not found.
        """
        state_info = self.get_state_by_name(state)
        if state_info:
            return state_info.get("capital", None)
        else:
            return None

    def get_state_lgas(self, state_name):
        """
        Get a list of Local Government Areas for a specific state.

        Args:
            state_name (str): The name of the state.

        Returns:
            list: A list of LGAs for the specified state.
        """
        state_info = self.get_state_by_name(state_name)
        if state_info:
            return state_info["lgas"]
        else:
            return []
