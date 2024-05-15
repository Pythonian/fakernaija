import random
from Faker9ja.providers.names import NameProvider
from Faker9ja.providers.geo import GeoProvider


class Faker:
    """A class for generating fake data exposed by different Providers."""

    def __init__(self):
        """
        Initializes the Faker class.

        Creates an instance of each of the Provider classes.
        """
        self.name_provider = NameProvider()
        self.geo_provider = GeoProvider()

    def full_name(self, ethnic_group=None, gender=None):
        """
        Generates a random full name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.
            gender (str, optional):
                The gender for which to generate the name.

        Returns:
            str: A random full name.
        """
        return self.name_provider.generate_full_name(ethnic_group, gender)

    def male_full_name(self, ethnic_group=None):
        """
        Generates a random male full name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random male full name.
        """
        return self.name_provider.generate_full_name(ethnic_group, gender="male")

    def female_full_name(self, ethnic_group=None):
        """
        Generates a random female full name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random female full name.
        """
        return self.name_provider.generate_full_name(ethnic_group, gender="female")

    def first_name(self, ethnic_group=None):
        """
        Generates a random first name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random first name.
        """
        return self.name_provider.generate_first_name(ethnic_group)

    def last_name(self, ethnic_group=None):
        """
        Generates a random last name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random last name.
        """
        return self.name_provider.generate_last_name(ethnic_group)

    def male_first_name(self, ethnic_group=None):
        """
        Generates a random male first name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random male first name.
        """
        return self.name_provider.generate_first_name(ethnic_group, gender="male")

    def female_first_name(self, ethnic_group=None):
        """
        Generates a random female first name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random female first name.
        """
        return self.name_provider.generate_first_name(ethnic_group, gender="female")

    def prefix(self):
        """
        Generates a random name prefix.

        Returns:
            str: A random name prefix.
        """
        prefixes = ["Mr.", "Mrs.", "Miss", "Master", "Mister", "Madam"]
        return random.choice(prefixes)

    def male_prefix(self):
        """
        Generates a random male name prefix.

        Returns:
            str: A random male name prefix.
        """
        prefixes = ["Mr.", "Master", "Mister"]
        return random.choice(prefixes)

    def female_prefix(self):
        """
        Generates a random female name prefix.

        Returns:
            str: A random female name prefix.
        """
        prefixes = ["Mrs.", "Miss", "Madam"]
        return random.choice(prefixes)

    def state(self, shortcode=False, region_initial=None):
        """
        Get a random state.

        Args:
            shortcode (bool, optional):
                Whether to return the shortcode of the state instead of its name.
                Defaults to False.
            region_initial (str, optional):
                The initial of the region from which to select a state.
                If provided, the method will return a random state from that region.
                Defaults to None.

        Returns:
            str: Random state name or initial.
        """
        if region_initial:
            states = self.geo_provider.get_states_by_region(region_initial)
            random_state = random.choice(states)
            return random_state["name"] if not shortcode else random_state["code"]
        elif shortcode:
            return random.choice(self.geo_provider.get_shortcodes())
        else:
            return random.choice(self.geo_provider.get_states())

    def capital(self, state=None):
        """
        Get a random state capital or the capital of a specific state.

        Args:
            state (str, optional):
                The name of the state for which to get the capital.
                If None, a random capital city will be returned.

        Returns:
            str: Random state capital or the capital of the specified state.
        """
        if state:
            return self.geo_provider.get_state_capital(state)
        else:
            return random.choice(self.geo_provider.get_capitals())

    def lga(self, state=None):
        """
        Get a random Local Government Area (L.G.A).

        Args:
            state (str, optional):
                The name of the state for which to get an LGA.
                If None, a random LGA from any state will be returned.

        Returns:
            str: Random LGA.
        """
        if state:
            lgas = self.geo_provider.get_state_lgas(state)
        else:
            lgas = self.geo_provider.get_lgas()
        return random.choice(lgas) if lgas else None

    def region(self, initial=False):
        """
        Get a random geopolitical region in Nigeria.

        Args:
            initial (bool, optional):
                If True, return the initials of the region (e.g., "SW" for South West).
                If False (default), return the full name of the region.

        Returns:
            str: Random region name or initials.
        """
        regions = self.geo_provider.get_regions()
        if initial:
            return random.choice(regions)
        else:
            return random.choice(
                [state["region"] for state in self.geo_provider.states_data["states"]]
            )

    def postal_code(self, state=None):
        """
        Get a random postal code of any state, or of a specific state if specified.

        Args:
            state (str, optional):
                The name of the state for which to get the postal code.
                If None, a random postal code of any state will be returned.
                Defaults to None.

        Returns:
            str: Random postal code.
        """
        if state:
            return self.geo_provider.get_postal_code_by_state(state)
        else:
            return random.choice(self.geo_provider.get_postal_codes())
