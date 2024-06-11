"""StateMixin to group related methods for the StateProvider."""

import random

from fakernaija.providers.states import StateProvider


class State:
    """Methods for the StateProvider."""

    def __init__(self) -> None:
        """Initializes the State mixin and its provider."""
        self.state_provider = StateProvider()

    def state(self, shortcode: bool = False, region_initial: str | None = None) -> str:
        """Get a random state.

        Args:
            shortcode (bool, optional): Whether to return the shortcode of the state instead of its name. Defaults to False.
            region_initial (str | None, optional): The initial of the region from which to select a state. If provided, the method will return a random state from that region. Defaults to None.

        Returns:
            str: Random state name or initial.

        Note:
            Available region initials are: NE, NW, NC, SE, SW, SS

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_name = naija.state()
                >>> print(f"Random state name: {state_name}")
                'Random state name: Lagos'

                >>> state_shortcode = naija.state(shortcode=True)
                >>> print(f"Random state shortcode: {state_shortcode}")
                'Random state shortcode: LA'

                >>> state_name = naija.state(region_initial="SS")
                >>> print(f"Random state name from South South region: {state_name}")
                'Random state name from South South region: Edo'

                >>> state_shortcode = naija.state(shortcode=True, region_initial="SE")
                >>> print(f"Random state shortcode from South East region: {state_shortcode}")
                'Random state shortcode from South East region: AB'
        """
        if region_initial:
            states = self.state_provider.get_states_by_region(region_initial)
            random_state = random.choice(states)
            return random_state["name"] if not shortcode else random_state["code"]
        if shortcode:
            return random.choice(self.state_provider.get_shortcodes())
        return random.choice(self.state_provider.get_states())

    def capital(self, state: str | None = None) -> str | None:
        """Get a random state capital or the capital of a specific state.

        Args:
            state (str | None, optional): The name of the state for which to get the capital. If None, a random capital city will be returned.

        Returns:
            str | None: Random state capital or the capital of the specified state. Returns None if the specified state does not exist.

        Note:
            Entering a nonexistent state to the state parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> capital = naija.capital()
                >>> print(f"Random state capital: {capital}")
                'Random state capital: Ikeja'

                >>> capital = naija.capital(state="Lagos")
                >>> print(f"Capital of Lagos: {capital}")
                'Capital of Lagos: Ikeja'
        """
        if state:
            return self.state_provider.get_state_capital(state)
        return random.choice(self.state_provider.get_capitals())

    def lga(self, state: str | None = None) -> str | None:
        """Get a random Local Government Area (L.G.A).

        Args:
            state (str | None, optional): The name of the state for which to get an LGA. If None, a random LGA from any state will be returned.

        Returns:
            str | None: A random Local Government Area.

        Note:
            Entering a nonexistent state to the state parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> lga = naija.lga()
                >>> print(f"Random LGA: {lga}")
                'Random LGA: Ikeja'

                >>> lga = naija.lga(state="Lagos")
                >>> print(f"Random LGA in Lagos: {lga}")
                'Random LGA in Lagos: Surulere'
        """
        if state:
            lgas = self.state_provider.get_state_lgas(state)
        else:
            lgas = self.state_provider.get_lgas()
        return random.choice(lgas) if lgas else None

    def region(self, initial: bool = False) -> str:
        """Get a random geopolitical region in Nigeria.

        Args:
            initial (bool, optional):
                If True, return the initials of the region (e.g., "SW" for South West).
                If False (default), return the full name of the region.

        Returns:
            str: Random region name or initials.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> region = naija.region()
                >>> print(f"Random region: {region}")
                'Random region: North Central'

                >>> region_initial = naija.region(initial=True)
                >>> print(f"Random region initial: {region_initial}")
                'Random region initial: NC'
        """
        regions = self.state_provider.get_regions()
        if initial:
            return random.choice(
                [state["region_initial"] for state in self.state_provider.states_data],
            )
        return random.choice(regions)

    def postal_code(self, state: str | None = None) -> str | None:
        """Get a random postal code of any state, or of a specific state if specified.

        Args:
            state (str | None, optional): The name of the state for which to get the postal code.
            If None (default), return a random postal code of any state.

        Returns:
            str | None: Random postal code or the postal code of the specified state.
            Returns None if the specified state does not exist.

        Note:
            Entering a nonexistent state to the state parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> postal_code = naija.postal_code()
                >>> print(f"Random postal code: {postal_code}")
                'Random postal code: 100001'

                >>> postal_code = naija.postal_code(state="Lagos")
                >>> print(f"Random postal code for Lagos: {postal_code}")
                'Random postal code for Lagos: 101010'
        """
        if state:
            return self.state_provider.get_postal_code_by_state(state)
        return random.choice(self.state_provider.get_postal_codes())
