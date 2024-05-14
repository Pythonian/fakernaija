import random
from Faker9ja.providers.names import NameProvider
from Faker9ja.providers.states import StateProvider


class NameGenerator:
    """
    A class for generating Nigerian names.

    This class provides methods to generate Nigerian names,
    including first names, last names, and full names.

    Usage:
        from Faker9ja.faker import NameGenerator

        name = NameGenerator()

        # Get a random Yoruba male fullname
        full_name = name.full_name(ethnic_group="yoruba", gender="male")

        # Get a random Igbo lastname
        last_name = name.last_name("igbo")

        # Get 5 random Hausa female firstname
        for i in range(5):
            first_name = name.first_name(ethnic_group="hausa", gender="female")
            print(first_name)
    """

    def __init__(self):
        """
        Initializes the NameGenerator class.

        Creates an instance of the NameProvider class for generating names.
        """
        self.name_provider = NameProvider()

    def first_name(self, ethnic_group=None, gender=None):
        """
        Generates a Nigerian first name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.
            gender (str, optional):
                The gender for which to generate the name.

        Returns:
            str: A Nigerian first name.
        """
        return self.name_provider.generate_first_name(ethnic_group, gender)

    def full_name(self, ethnic_group=None, gender=None):
        """
        Generates a Nigerian full name (first name + last name).

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.
            gender (str, optional):
                The gender for which to generate the name.

        Returns:
            str: A Nigerian full name.
        """
        return self.name_provider.generate_full_name(ethnic_group, gender)

    def last_name(self, ethnic_group=None):
        """
        Generates a Nigerian last name.

        Args:
            ethnic_group (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A Nigerian last name.
        """
        return self.name_provider.generate_last_name(ethnic_group)


class StateGenerator:
    """
    A class for generating random Nigerian state information.

    Attributes:
        state_provider (StateProvider):
            An instance of the StateProvider class used for accessing state information.

    Usage:
        from Faker9ja.faker import StateGenerator

        state_generator = StateGenerator()

        # Get a random state
        random_state = state_generator.state()
        print("Random state:", random_state)

        # Get a random state capital
        random_capital = state_generator.capital()
        print("Random capital city:", random_capital)

        # Get the capital of a specific state
        capital = state_generator.capital(state="Lagos")
        print("The capital of Lagos is:", capital)

        # Get a random state short code
        random_state_shortcode = state_generator.state(shortcode=True)
        print("Random state shortcode:", random_state_shortcode)

        # Get a random state from a specific region (e.g., South West)
        random_state_by_region = state_generator.state(region_code="SW")
        print("Random state by Region:", random_state_by_region)

        # Get a random LGA
        random_lga = state_generator.lga()
        print("Random LGA:", random_lga)

        # Get a random LGA in a specific state
        random_lga_in_state = state_generator.lga(state="Abia")
        print("Random LGA in Abia:", random_lga_in_state)

        # Get all the Geopolitical regions
        regions = state_provider.get_regions()
        print("Geopolitical regions:", regions)

    """

    def __init__(self):
        """
        Initializes the StateGenerator class.

        Creates an instance of the StateProvider class.
        """
        self.state_provider = StateProvider()

    def state(self, shortcode=False, region_code=None):
        """
        Get a random state.

        Args:
            shortcode (bool, optional):
                Whether to return the shortcode of the state instead of its name.
                Defaults to False.
            region_code (str, optional):
                The code of the region from which to select a state.
                If provided, the method will return a random state from that region.
                Defaults to None.

        Returns:
            str: Random state name or short code.
        """
        if region_code:
            states = self.state_provider.get_states_by_region(region_code)
            random_state = random.choice(states)
            return random_state["name"] if not shortcode else random_state["code"]
        elif shortcode:
            return random.choice(self.state_provider.get_shortcodes())
        else:
            return random.choice(self.state_provider.get_states())

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
            return self.state_provider.get_state_capital(state)
        else:
            return random.choice(self.state_provider.get_capitals())

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
            lgas = self.state_provider.get_state_lgas(state)
        else:
            lgas = [
                lga
                for state_code in self.state_provider.get_states()
                for lga in self.state_provider.get_state_lgas(state_code) or []
            ]
        return random.choice(lgas) if lgas else None
