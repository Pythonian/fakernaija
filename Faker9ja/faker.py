import random
from Faker9ja.providers.names import NameProvider
from Faker9ja.providers.states import StateProvider


class Faker:
    """
    A class for generating Nigerian names.

    This class provides methods to generate Nigerian names,
    including first names, last names, and full names.

    Usage:
        from Faker9ja.faker import Faker

        naija = Faker()

        # Get a random full name irrespective of ethnic_group or gender
        full_name = naija.full_name()

        # Get a random Igbo full name irrespective of gender
        igbo_full_name = naija.full_name(ethnic_group="igbo")

        # Get a male full name irrespective of ethnic_group
        male_full_name = naija.male_full_name()

        # Get an Igbo male full name
        igbo_male_full_name = naija.male_full_name(ethnic_group="igbo")

        # Get a female full name irrespective of ethnic_group
        female_full_name = naija.female_full_name()

        # Get an Igbo female full name
        igbo_female_full_name = naija.female_full_name(ethnic_group="igbo")

        # Get a random first name irrespective of ethnic_group or gender
        first_name = naija.first_name()

        # Get a random Yoruba first name irrespective of gender
        yoruba_first_name = naija.first_name(ethnic_group="yoruba")

        # Get a random last name irrespective of ethnic_group
        last_name = naija.last_name()

        # Get a random Yoruba last name
        yoruba_last_name = naija.last_name(ethnic_group="yoruba")

        # Get a random male first name irrespective of ethnic_group
        male_first_name = naija.male_first_name()

        # Get a random Hausa male first name
        hausa_male_first_name = naija.male_first_name(ethnic_group="hausa")

        # Get a random female first name irrespective of ethnic_group
        female_first_name = naija.female_first_name()

        # Get a random Hausa female first name
        hausa_female_first_name = naija.female_first_name(ethnic_group="hausa")

        # Get a random name prefix
        prefix = naija.prefix()

        # Get a random male name prefix
        male_prefix = naija.male_prefix()

        # Get a random female name prefix
        female_prefix = naija.female_prefix()
    """

    def __init__(self):
        """
        Initializes the Faker class.

        Creates an instance of the NameProvider class for generating names.
        """
        self.name_provider = NameProvider()

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
        random_state_by_region = state_generator.state(region_initial="SW")
        print("Random state by Region:", random_state_by_region)

        # Get a random LGA
        random_lga = state_generator.lga()
        print("Random LGA:", random_lga)

        # Get a random LGA in a specific state
        random_lga_in_state = state_generator.lga(state="Abia")
        print("Random LGA in Abia:", random_lga_in_state)
    """

    def __init__(self):
        """
        Initializes the StateGenerator class.

        Creates an instance of the StateProvider class.
        """
        self.state_provider = StateProvider()

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
            states = self.state_provider.get_states_by_region(region_initial)
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
