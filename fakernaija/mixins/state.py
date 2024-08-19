"""State mixin to group related methods for the StateProvider."""

import random

from fakernaija.providers import StateProvider
from fakernaija.utils import get_unique_value


class State:
    """Methods for the StateProvider."""

    def __init__(self) -> None:
        """Initializes the State mixin and its provider."""
        self.state_provider = StateProvider()
        self._used_state_names: set[str] = set()
        self._used_state_capitals: set[str] = set()
        self._used_state_lgas: set[str] = set()
        self._used_state_postal_codes: set[str] = set()

    def state(self, region: str | None = None) -> dict[str, str]:
        """Get a dictionary of random state information, optionally filtered by region.

        Args:
            region (str | None, optional): The region abbreviation to filter by.

        Returns:
            dict[str, str]: Random state information, optionally filtered by region.

        Note:
            - Region options: NW, NE, NC, SW, SE, SS

        Raises:
            ValueError: If the specified region does not exist.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> state = naija.state()
                >>> print(f"Random state: {state}")
                Random state: {'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa']}

                >>> state = naija.state(region="SS")
                >>> print(f"Random state by region: {state}")
                Random state by region: {'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa']}
        """
        if region:
            self.state_provider.validate_region(region)
            states = self.state_provider.get_states_by_region(region)
        else:
            states = self.state_provider.get_states()
        return random.choice(states)

    def state_name(self, region: str | None = None) -> str:
        """Get a random state name, optionally filtered by region.

        Args:
            region (str | None, optional): The region abbreviation to filter by.

        Returns:
            str: Random state name, optionally filtered by region.

        Note:
            - Region options: NW, NE, NC, SW, SE, SS

        Raises:
            ValueError: If the specified region does not exist.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> state_name = naija.state_name()
                >>> print(f"Random state name: {state_name}")
                Random state name: Lagos

                >>> for _ in range(3):
                ...     print(naija.state_name())
                ...
                Borno
                Katsina
                Taraba

                >>> state_name = naija.state_name(region="SW")
                >>> print(f"Random state name by region: {state_name}")
                Random state name by region: Ekiti
        """
        if region:
            self.state_provider.validate_region(region)
            states = self.state_provider.get_states_by_region(region)
            state_names = [state["name"] for state in states]
        else:
            state_names = self.state_provider.get_state_names()
        state_name = get_unique_value(state_names, self._used_state_names)
        self._used_state_names.add(state_name)
        return state_name

    def state_capital(self, region: str | None = None) -> str:
        """Get a random state capital, optionally filtered by region.

        Args:
            region (str | None, optional): The region abbreviation to filter by.

        Returns:
            str: Random state capital, optionally filtered by region.

        Note:
            - Region options: NW, NE, NC, SW, SE, SS

        Raises:
            ValueError: If the specified region does not exist.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> capital = naija.state_capital()
                >>> print(f"Random state capital: {capital}")
                Random state capital: Ikeja

                >>> for _ in range(3):
                ...     print(naija.state_capital())
                ...
                Uyo
                Bernin-Kebbi
                Port-Harcourt

                >>> capital = naija.state_capital(region="SW")
                >>> print(f"Random state capital by region: {capital}")
                Random state capital by region: Ikeja
        """
        if region:
            self.state_provider.validate_region(region)
            states = self.state_provider.get_states_by_region(region)
            state_capitals = [state["capital"] for state in states]
        else:
            state_capitals = self.state_provider.get_capitals()
        state_capital = get_unique_value(state_capitals, self._used_state_capitals)
        self._used_state_capitals.add(state_capital)
        return state_capital

    def state_lga(self, state: str | None = None) -> str:
        """Get a random LGA, optionally filtered by state.

        Args:
            state (str | None, optional): The name of the state to filter by.

        Returns:
            str: Random LGA in the specified state or any state if none is specified.

        Note:
            - State options: 36 States in Nigeria

        Raises:
            ValueError: If the specified state does not exist.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> state_lga = naija.state_lga()
                >>> print(f"Random State LGA: {state_lga}")
                Random State LGA: Surulere

                >>> state_lga = naija.state_lga("lagos")
                >>> print(f"Random State LGA in a specified state: {state_lga}")
                Random State LGA: Alimosho
        """
        if state:
            state_lgas = self.state_provider.get_state_lgas(state.lower())
            if not state_lgas:
                available_states = ", ".join(self.state_provider.get_state_names())
                msg = f"The state '{state}' does not exist in Nigeria. Available states are: {available_states}."
                raise ValueError(msg)
        else:
            state_lgas = self.state_provider.get_lgas()
        state_lga = get_unique_value(state_lgas, self._used_state_lgas)
        self._used_state_lgas.add(state_lga)
        return state_lga

    def state_postal_code(self, state: str | None = None) -> str:
        """Get a random state postal code.

        Args:
            state (str | None, optional): An optional state name.

        Returns:
            str: Postal code of the specified state or any state if none is specified.

        Note:
            - State options: 36 states in Nigeria.

        Raises:
            ValueError: If the specified state does not exist.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> postal_code = naija.state_postal_code()
                >>> print(f"Random postal code: {postal_code}")
                Random postal code: 100001

                >>> for _ in range(3):
                ...     print(naija.state_postal_code())
                ...
                970001
                400001
                320001

                >>> postal_code = naija.state_postal_code('lagos')
                >>> print(f"Postal code of a state: {postal_code}")
                Postal code of a state: 100001
        """
        if state:
            state_postal_code = self.state_provider.get_postal_code_by_state(
                state.lower(),
            )
            if not state_postal_code:
                available_states = ", ".join(self.state_provider.get_state_names())
                msg = f"The state '{state}' does not exist in Nigeria. Available states are: {available_states}."
                raise ValueError(msg)
            return state_postal_code
        return random.choice(self.state_provider.get_postal_codes())
