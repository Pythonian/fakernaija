import random
from Faker9ja.providers.names import NameProvider
from Faker9ja.providers.geo import GeoProvider
from Faker9ja.providers.schools import SchoolProvider
from Faker9ja.providers.phonenumbers import PhoneNumberProvider


class Faker:
    """A class for generating fake data exposed by different Providers."""

    def __init__(self):
        """
        Initializes the Faker class.

        Creates an instance of each of the Provider classes.
        """
        self.name_provider = NameProvider()
        self.geo_provider = GeoProvider()
        self.school_provider = SchoolProvider()
        self.phonenumber_provider = PhoneNumberProvider()

    def full_name(self, tribe=None, gender=None):
        """
        Generates a random full name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.
            gender (str, optional):
                The gender for which to generate the name.

        Returns:
            str: A random full name.
        """
        return self.name_provider.generate_full_name(tribe, gender)

    def male_full_name(self, tribe=None):
        """
        Generates a random male full name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random male full name.
        """
        return self.name_provider.generate_full_name(tribe, gender="male")

    def female_full_name(self, tribe=None):
        """
        Generates a random female full name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random female full name.
        """
        return self.name_provider.generate_full_name(tribe, gender="female")

    def first_name(self, tribe=None):
        """
        Generates a random first name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random first name.
        """
        return self.name_provider.generate_first_name(tribe)

    def last_name(self, tribe=None):
        """
        Generates a random last name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random last name.
        """
        return self.name_provider.generate_last_name(tribe)

    def male_first_name(self, tribe=None):
        """
        Generates a random male first name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random male first name.
        """
        return self.name_provider.generate_first_name(tribe, gender="male")

    def female_first_name(self, tribe=None):
        """
        Generates a random female first name.

        Args:
            tribe (str, optional):
                The ethnic group for which to generate the name.

        Returns:
            str: A random female first name.
        """
        return self.name_provider.generate_first_name(tribe, gender="female")

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

    def school(self, acronym=False, location=None):
        """
        Get a random school name.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random school by name at that location.
                Defaults to None.

        Returns:
            str: Random school name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if acronym:
                return random.choice([school["acronym"] for school in locations])
            else:
                return random.choice([school["name"] for school in locations])
        else:
            if acronym:
                return random.choice(self.school_provider.get_school_acronyms())
            else:
                return random.choice(self.school_provider.get_schools())

    def federal_school(self, acronym=False, location=None):
        """
        Get a random federal school.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random federal school at that location.
                Defaults to None.

        Returns:
            str: Random federal school name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            federal_schools = [
                school for school in locations if school["ownership"] == "Federal"
            ]
            if federal_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_schools]
                    )
                else:
                    return random.choice([school["name"] for school in federal_schools])
            else:
                return None
        else:
            federal_schools = self.school_provider.get_federal_schools()
            if federal_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_schools]
                    )
                else:
                    return random.choice([school["name"] for school in federal_schools])
            else:
                return None

    def state_school(self, acronym=False, location=None):
        """
        Get a random state school.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random state school at that location.
                Defaults to None.

        Returns:
            str: Random state school name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            state_schools = [
                school for school in locations if school["ownership"] == "State"
            ]
            if state_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_schools]
                    )
                else:
                    return random.choice([school["name"] for school in state_schools])
            else:
                return None
        else:
            state_schools = self.school_provider.get_state_schools()
            if state_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_schools]
                    )
                else:
                    return random.choice([school["name"] for school in state_schools])
            else:
                return None

    def private_school(self, acronym=False, location=None):
        """
        Get a random private school.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random private school at that location.
                Defaults to None.

        Returns:
            str: Random private school name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            private_schools = [
                school for school in locations if school["ownership"] == "Private"
            ]
            if private_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_schools]
                    )
                else:
                    return random.choice([school["name"] for school in private_schools])
            else:
                return None
        else:
            private_schools = self.school_provider.get_private_schools()
            if private_schools:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_schools]
                    )
                else:
                    return random.choice([school["name"] for school in private_schools])
            else:
                return None

    def university(self, acronym=False, location=None):
        """
        Get a random university.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the university name.
                Defaults to False.
            location (str, optional):
                If provided, get a random university at that location.
                Defaults to None.

        Returns:
            str: Random university name or acronym.
        """
        if location:
            locations = self.school_provider.get_universities_by_location(location)
            if locations:
                if acronym:
                    return random.choice([school["acronym"] for school in locations])
                else:
                    return random.choice([school["name"] for school in locations])
            else:
                return None
        else:
            universities = self.school_provider.get_universities()
            if universities:
                if acronym:
                    return random.choice([school["acronym"] for school in universities])
                else:
                    return random.choice([school["name"] for school in universities])
            else:
                return None

    def polytechnic(self, acronym=False, location=None):
        """
        Get a random polytechnic.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the polytechnic name.
                Defaults to False.
            location (str, optional):
                If provided, get a random polytechnic at that location.
                Defaults to None.

        Returns:
            str: Random polytechnic name or acronym.
        """
        if location:
            locations = self.school_provider.get_polytechnics_by_location(location)
            if locations:
                if acronym:
                    return random.choice([school["acronym"] for school in locations])
                else:
                    return random.choice([school["name"] for school in locations])
            else:
                return None
        else:
            polytechnics = self.school_provider.get_polytechnics()
            if polytechnics:
                if acronym:
                    return random.choice([school["acronym"] for school in polytechnics])
                else:
                    return random.choice([school["name"] for school in polytechnics])
            else:
                return None

    def college_of_education(self, acronym=False, location=None):
        """
        Get a random college of education.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random college of education at that location.
                Defaults to None.

        Returns:
            str: Random college of education name or acronym.
        """
        if location:
            locations = self.school_provider.get_colleges_of_education_by_location(
                location
            )
            if locations:
                if acronym:
                    return random.choice([school["acronym"] for school in locations])
                else:
                    return random.choice([school["name"] for school in locations])
            else:
                return None
        else:
            colleges_of_education = self.school_provider.get_colleges_of_education()
            if colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in colleges_of_education]
                    )
            else:
                return None

    def federal_university(self, acronym=False, location=None):
        """
        Get a random federal university.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random federal university at that location.
                Defaults to None.

        Returns:
            str: Random federal university name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            federal_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "Federal"
            ]
            if federal_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_universities]
                    )
            else:
                return None
        else:
            federal_universities = self.school_provider.get_federal_universities()
            if federal_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_universities]
                    )
            else:
                return None

    def federal_polytechnic(self, acronym=False, location=None):
        """
        Get a random federal polytechnic.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random federal polytechnic at that location.
                Defaults to None.

        Returns:
            str: Random federal polytechnic name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            federal_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "Federal"
            ]
            if federal_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_polytechnics]
                    )
            else:
                return None
        else:
            federal_polytechnics = self.school_provider.get_federal_polytechnics()
            if federal_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_polytechnics]
                    )
            else:
                return None

    def federal_college_of_education(self, acronym=False, location=None):
        """
        Get a random federal college of education.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random federal college of education at that location.
                Defaults to None.

        Returns:
            str: Random federal college of education name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            federal_colleges_of_education = [
                school
                for school in locations
                if school["type"] == "College of Education"
                and school["ownership"] == "Federal"
            ]
            if federal_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_colleges_of_education]
                    )
            else:
                return None
        else:
            federal_colleges_of_education = (
                self.school_provider.get_federal_colleges_of_education()
            )
            if federal_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in federal_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in federal_colleges_of_education]
                    )
            else:
                return None

    def state_university(self, acronym=False, location=None):
        """
        Get a random state university.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random state university at that location.
                Defaults to None.

        Returns:
            str: Random state university name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            state_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "State"
            ]
            if state_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_universities]
                    )
            else:
                return None
        else:
            state_universities = self.school_provider.get_state_universities()
            if state_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_universities]
                    )
            else:
                return None

    def state_polytechnic(self, acronym=False, location=None):
        """
        Get a random state polytechnic.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random state polytechnic at that location.
                Defaults to None.

        Returns:
            str: Random state polytechnic name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            state_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "State"
            ]
            if state_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_polytechnics]
                    )
            else:
                return None
        else:
            state_polytechnics = self.school_provider.get_state_polytechnics()
            if state_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_polytechnics]
                    )
            else:
                return None

    def state_college_of_education(self, acronym=False, location=None):
        """
        Get a random state college of education.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random state college of education at that location.
                Defaults to None.

        Returns:
            str: Random state college of education name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            state_colleges_of_education = [
                school
                for school in locations
                if school["type"] == "College of Education"
                and school["ownership"] == "State"
            ]
            if state_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_colleges_of_education]
                    )
            else:
                return None
        else:
            state_colleges_of_education = (
                self.school_provider.get_state_colleges_of_education()
            )
            if state_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in state_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in state_colleges_of_education]
                    )
            else:
                return None

    def private_university(self, acronym=False, location=None):
        """
        Get a random private university.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random private university at that location.
                Defaults to None.

        Returns:
            str: Random private university name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            private_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "Private"
            ]
            if private_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_universities]
                    )
            else:
                return None
        else:
            private_universities = self.school_provider.get_private_universities()
            if private_universities:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_universities]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_universities]
                    )
            else:
                return None

    def private_polytechnic(self, acronym=False, location=None):
        """
        Get a random private polytechnic.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random private polytechnic at that location.
                Defaults to None.

        Returns:
            str: Random private polytechnic name or acronym.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            private_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "Private"
            ]
            if private_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_polytechnics]
                    )
            else:
                return None
        else:
            private_polytechnics = self.school_provider.get_private_polytechnics()
            if private_polytechnics:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_polytechnics]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_polytechnics]
                    )
            else:
                return None

    def private_college_of_education(self, acronym=False, location=None):
        """
        Get a random private college of education.

        Args:
            acronym (bool, optional):
                If True, return the acronym instead of the school name.
                Defaults to False.
            location (str, optional):
                If provided, get a random private college of education at that location.
                Defaults to None.

        Returns:
            str: Random private college of education name or acronym.
        """
        if location:
            colleges_at_location = self.school_provider.get_schools_by_location(
                location
            )
            private_colleges_of_education = [
                school
                for school in colleges_at_location
                if school["type"] == "College of Education"
                and school["ownership"] == "Private"
            ]
            if private_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_colleges_of_education]
                    )
            else:
                return None
        else:
            private_colleges_of_education = (
                self.school_provider.get_private_colleges_of_education()
            )
            if private_colleges_of_education:
                if acronym:
                    return random.choice(
                        [school["acronym"] for school in private_colleges_of_education]
                    )
                else:
                    return random.choice(
                        [school["name"] for school in private_colleges_of_education]
                    )
            else:
                return None

    def phone_number(self, network=None, prefix=None):
        """
        Generate a random Nigerian phone number, or a phone number
        based on the specified network or prefix.
        Args:
            network (str, optional):
                The name of the network ('mtn', 'glo', 'airtel', '9mobile').
                Defaults to None.
            prefix (str, optional):
                The prefix of the phone number. Defaults to None.
        Returns:
            str: A valid Nigerian phone number.
        """
        return self.phonenumber_provider.phone_number(network=network, prefix=prefix)
