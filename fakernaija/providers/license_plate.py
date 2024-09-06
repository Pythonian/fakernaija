"""LicensePlateProvider."""

import random
from pathlib import Path

from fakernaija.providers.state import StateProvider
from fakernaija.utils import load_json, normalize_input


class LicensePlateProvider:
    """Provider class to generate Nigerian license plates."""

    def __init__(self) -> None:
        """Initialize the LicensePlateProvider with LGA data."""
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
        self.state_provider = StateProvider()
        self.state_names = self.state_provider.get_state_names()
        self.lga_codes = self.state_provider.get_lga_codes()

    def generate_license_plate(self, state: str | None = None) -> str:
        """Generate a random Nigerian license plate.

        Args:
            state (str | None, optional): The name of the state for which to
                generate the license plate. Defaults to None.

        Returns:
            str: A randomly generated Nigerian license plate.
        """
        state = normalize_input(state)

        # Ensure that the state name comparison is case-insensitive
        if state:
            # Map lowercase state names to original case
            state_dict = {s.lower(): s for s in self.state_names}
            if state.lower() not in state_dict:
                msg = f"Invalid state name: {state}. Valid states are: {', '.join(self.state_names)}"
                raise ValueError(msg)
            # Use the correctly cased state name to access LGA codes
            state_name = state_dict[state.lower()]
            lga_code = random.choice(self.lga_codes[state_name])
        else:
            # Randomly choose an LGA code from all available ones if no state is specified
            all_lgas = [code for codes in self.lga_codes.values() for code in codes]
            lga_code = random.choice(all_lgas)

        digits = "".join(random.choices("0123456789", k=3))
        letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        return f"{lga_code}-{digits}{letters}"
