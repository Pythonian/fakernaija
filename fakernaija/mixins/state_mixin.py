"""State mixin to group related methods for the StateProvider."""

import random

from fakernaija.providers.state_provider import StateProvider


class State:
    """Methods for the StateProvider."""

    def __init__(self) -> None:
        """Initializes the State mixin and its provider."""
        self.state_provider = StateProvider()

    def state(self) -> dict[str, str]:
        """Get a dictionary of random state information.

        Returns:
            dict[str, str]: Random state information.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state = naija.state()
                >>> print(f"Random state: {state}")
                '{'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'region_initial': 'SS', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa']}'
        """
        return random.choice(self.state_provider.get_states())

    def state_name(self) -> str:
        """Get a random state name.

        Returns:
            str: Random state name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_name = naija.state_name()
                >>> print(f"Random state name: {state_name}")
                'Random state name: Lagos'
        """
        return random.choice(self.state_provider.get_state_names())

    def state_code(self) -> str:
        """Get a random state code.

        Returns:
            str: Random state code.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_code = naija.state_code()
                >>> print(f"Random state code: {state_code}")
                'Random state code: LA'
        """
        return random.choice(self.state_provider.get_shortcodes())

    def state_slogan(self) -> str:
        """Get a random state slogan.

        Returns:
            str: Random state slogan.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_slogan = naija.state_slogan()
                >>> print(f"Random state slogan: {state_slogan}")
                'Random state slogan: Center of Excellence'
        """
        return random.choice(self.state_provider.get_slogans())

    def region(self) -> dict[str, str]:
        """Get a random geopolitical region in Nigeria.

        Returns:
            dict[str, str]: Random region abbreviation and full name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> region = naija.region()
                >>> print(f"Random region: {region}")
                "Random region: {'abbr': 'SS', 'name': 'South South'}"
        """
        return random.choice(self.state_provider.get_regions())

    def region_name(self) -> str:
        """Get a random geopolitical region name in Nigeria.

        Returns:
            str: Random region name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> region_name = naija.region_name()
                >>> print(f"Random region name: {region_name}")
                'Random region name: South West'
        """
        return random.choice(
            [region["name"] for region in self.state_provider.get_regions()],
        )

    def region_abbr(self) -> str:
        """Get a random geopolitical region abbreviation in Nigeria.

        Returns:
            str: Random region abbreviation.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> region_abbr = naija.region_abbr()
                >>> print(f"Random region abbreviation: {region_abbr}")
                'Random region abbreviation: SW'
        """
        return random.choice(
            [region["abbr"] for region in self.state_provider.get_regions()],
        )

    def state_region(self, region_abbr: str) -> dict[str, str]:
        """Get a random state from a specific region.

        Args:
            region_abbr (str): The abbr of the region.

        Returns:
            dict[str, str]: Random state information from the specified region.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_region = naija.state_region('SS')
                >>> print(f"Random state information from a specific region: {state_region}")
                "Random state information from a specific region: {'code': 'BY', 'name': 'Bayelsa', 'capital': 'Yenagoa', 'slogan': 'Glory of All Lands', 'region': 'South South', 'postal_code': '561001', 'lgas': ['Brass', 'Ekeremor', 'Kolokuma Opokuma', 'Nembe', 'Ogbia', 'Sagbama', 'Southern-Ijaw', 'Yenagoa'], 'region_abbr': 'SS'}"

        Raises:
            ValueError: If the specified region abbr does not exist.
        """
        states = self.state_provider.get_states_by_region(region_abbr)
        if not states:
            unique_abbrs = {r["abbr"] for r in self.state_provider.get_regions()}
            available_options = ", ".join(unique_abbrs)
            msg = f"Invalid region abbreviation: {region_abbr}. Available options are: {available_options}"
            raise ValueError(msg)
        return random.choice(states)

    def state_capital(self) -> str:
        """Get a random state capital.

        Returns:
            str: Random state capital

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> capital = naija.state_capital()
                >>> print(f"Random state capital: {capital}")
                'Random state capital: Ikeja'
        """
        return random.choice(self.state_provider.get_capitals())

    def lga(self) -> str:
        """Get a random Local Government Area (LGA).

        Returns:
            str: Random LGA.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> lga = naija.lga()
                >>> print(f"Random LGA: {lga}")
                'Random LGA: Surulere'
        """
        return random.choice(self.state_provider.get_lgas())

    def state_lga(self, state: str) -> str:
        """Get a random Local Government Area (LGA) in the specified state.

        Args:
            state (str): The name of the state.

        Returns:
            str: Random LGA in the specified state.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_lga = naija.state_lga('lagos')
                >>> print(f"Random State LGA: {state_lga}")
                'Random State LGA: Surulere'

        Raises:
            ValueError: If the specified state does not exist.
        """
        lgas = self.state_provider.get_state_lgas(state.lower())
        if not lgas:
            msg = f"The state: {state} does not exist in Nigeria."
            raise ValueError(msg)
        return random.choice(lgas)

    def postal_code(self) -> str:
        """Get a random postal code.

        Returns:
            str: Random postal code.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> postal_code = naija.postal_code()
                >>> print(f"Random postal code: {postal_code}")
                'Random postal code: 100001'
        """
        return random.choice(self.state_provider.get_postal_codes())

    def state_postal_code(self, state: str) -> str:
        """Get the postal code of a specific state.

        Args:
            state (str): The name of the state for which to get the postal code.

        Returns:
            str: Postal code of the specified state.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_postal_code = naija.state_postal_code("Lagos")
                >>> print(f"Random postal code for Lagos: {state_postal_code}")
                'Random postal code for Lagos: 101010'

        Raises:
            ValueError: If the specified state does not exist.
        """
        postal_code = self.state_provider.get_postal_code_by_state(state.lower())
        if not postal_code:
            msg = f"The state: {state} does not exist in Nigeria."
            raise ValueError(msg)
        return postal_code
