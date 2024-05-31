"""This module provides a `Faker` class that generates random Nigerian data.

The `Faker` class includes methods to retrieve various types of data, such as names, phone numbers, states and capitals, schools, emails etc.
"""

import random

from fakernaija.providers.emails import EmailProvider
from fakernaija.providers.names import NameProvider
from fakernaija.providers.phonenumbers import PhoneNumberProvider
from fakernaija.providers.schools import SchoolProvider
from fakernaija.providers.states import StateProvider


class Faker:
    """A class for generating fake data exposed by different Providers."""

    def __init__(self) -> None:
        """Initializes the Faker class.

        Creates an instance of each of the Provider classes.
        """
        self.email_provider = EmailProvider()
        self.name_provider = NameProvider()
        self.state_provider = StateProvider()
        self.school_provider = SchoolProvider()
        self.phonenumber_provider = PhoneNumberProvider()

    def full_name(self, tribe: str | None = None, gender: str | None = None) -> str:
        """Generate a random full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.
            gender (str | None, optional): The gender for which to generate the name.

        Returns:
            str: A random full name.
        """
        return self.name_provider.generate_full_name(tribe, gender)

    def male_full_name(self, tribe: str | None = None) -> str:
        """Generate a random male full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random male full name.
        """
        return self.name_provider.generate_full_name(tribe, gender="male")

    def female_full_name(self, tribe: str | None = None) -> str:
        """Generate a random female full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random female full name.
        """
        return self.name_provider.generate_full_name(tribe, gender="female")

    def first_name(self, tribe: str | None = None) -> str:
        """Generate a random first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random first name.
        """
        return self.name_provider.generate_first_name(tribe, gender=None)

    def male_first_name(self, tribe: str | None = None) -> str:
        """Generate a random male first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random male first name.
        """
        return self.name_provider.generate_first_name(tribe, gender="male")

    def female_first_name(self, tribe: str | None = None) -> str:
        """Generate a random female first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random female first name.
        """
        return self.name_provider.generate_first_name(tribe, gender="female")

    def last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random last name.
        """
        return self.name_provider.generate_last_name(tribe)

    def prefix(self) -> str:
        """Generates a random name prefix.

        Returns:
            str: A random name prefix.
        """
        prefixes = ["Mr.", "Mrs.", "Miss", "Master", "Mister", "Madam"]
        return random.choice(prefixes)

    def male_prefix(self) -> str:
        """Generates a random male name prefix.

        Returns:
            str: A random male name prefix.
        """
        prefixes = ["Mr.", "Master", "Mister"]
        return random.choice(prefixes)

    def female_prefix(self) -> str:
        """Generates a random female name prefix.

        Returns:
            str: A random female name prefix.
        """
        prefixes = ["Mrs.", "Miss", "Madam"]
        return random.choice(prefixes)

    def state(self, shortcode: bool = False, region_initial: str | None = None) -> str:
        """Get a random state.

        Args:
            shortcode (bool, optional): Whether to return the shortcode of the state instead of its name. Defaults to False.
            region_initial (str | None, optional): The initial of the region from which to select a state. If provided, the method will return a random state from that region. Defaults to None.

        Returns:
            str: Random state name or initial.
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
            state (str | None, optional): The name of the state for which to get the capital.
            If None, a random capital city will be returned.

        Returns:
            str | None: Random state capital or the capital of the specified state.
            Returns None if the specified state does not exist.
        """
        if state:
            return self.state_provider.get_state_capital(state)
        return random.choice(self.state_provider.get_capitals())

    def lga(self, state: str | None = None) -> str | None:
        """Get a random Local Government Area (L.G.A).

        Args:
            state (str | None, optional): The name of the state for which to get an LGA. If None, a random LGA from any state will be returned.

        Returns:
            str | None: Random LGA.
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
        """
        regions = self.state_provider.get_regions()
        if initial:
            return random.choice(
                [
                    state["region_initial"]
                    for state in self.state_provider.states_data["states"]
                ],
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
        """
        if state:
            return self.state_provider.get_postal_code_by_state(state)
        return random.choice(self.state_provider.get_postal_codes())

    def school(self, acronym: bool = False, location: str | None = None) -> str | None:
        """Get a random school name.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random school by name at that location.
            Defaults to None.

        Returns:
            str | None: Random school name or acronym, or None if no schools are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            schools = [
                school["acronym"] if acronym else school["name"] for school in locations
            ]
            return random.choice(schools) if schools else None
        schools = (
            self.school_provider.get_school_acronyms()
            if acronym
            else self.school_provider.get_schools()
        )
        return random.choice(schools) if schools else None

    def federal_school(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random federal school.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random federal school at that location.
            Defaults to None.

        Returns:
            str | None: Random federal school name or acronym, or None if no federal schools are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            federal_schools = [
                school for school in locations if school["ownership"] == "Federal"
            ]
            if not federal_schools:
                return None
        else:
            federal_schools = self.school_provider.get_federal_schools()
            if not federal_schools:
                return None

        schools = [
            school["acronym"] if acronym else school["name"]
            for school in federal_schools
        ]
        return random.choice(schools) if schools else None

    def state_school(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random state school.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random state school at that location.
            Defaults to None.

        Returns:
            str | None: Random state school name or acronym, or None if no state schools are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            state_schools = [
                school for school in locations if school["ownership"] == "State"
            ]
            if not state_schools:
                return None
        else:
            state_schools = self.school_provider.get_state_schools()
            if not state_schools:
                return None

        schools = [
            school["acronym"] if acronym else school["name"] for school in state_schools
        ]
        return random.choice(schools) if schools else None

    def private_school(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random private school.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random private school at that location.
            Defaults to None.

        Returns:
            str | None: Random private school name or acronym, or None if no private schools are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            private_schools = [
                school for school in locations if school["ownership"] == "Private"
            ]
            if not private_schools:
                return None
        else:
            private_schools = self.school_provider.get_private_schools()
            if not private_schools:
                return None

        schools = [
            school["acronym"] if acronym else school["name"]
            for school in private_schools
        ]
        return random.choice(schools) if schools else None

    def university(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random university.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the university name.
            Defaults to False.
            location (str | None, optional): If provided, get a random university at that location.
            Defaults to None.

        Returns:
        str | None: Random university name or acronym, or None if no universities are found.
        """
        if location:
            locations = self.school_provider.get_universities_by_location(location)
            if not locations:
                return None
            universities = [
                school["acronym"] if acronym else school["name"] for school in locations
            ]
            return random.choice(universities) if universities else None

        universities = self.school_provider.get_universities()
        if not universities:
            return None
        university_names = [
            school["acronym"] if acronym else school["name"] for school in universities
        ]
        return random.choice(university_names) if university_names else None

    def polytechnic(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random polytechnic.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the polytechnic name.
            Defaults to False.
            location (str | None, optional): If provided, get a random polytechnic at that location.
            Defaults to None.

        Returns:
            str | None: Random polytechnic name or acronym, or None if no polytechnics are found.
        """
        if location:
            locations = self.school_provider.get_polytechnics_by_location(location)
            if not locations:
                return None
            polytechnics = [
                school["acronym"] if acronym else school["name"] for school in locations
            ]
            return random.choice(polytechnics) if polytechnics else None

        polytechnics = self.school_provider.get_polytechnics()
        if not polytechnics:
            return None
        polytechnic_names = [
            school["acronym"] if acronym else school["name"] for school in polytechnics
        ]
        return random.choice(polytechnic_names) if polytechnic_names else None

    def college_of_education(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random college of education.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random college of education at that location.
            Defaults to None.

        Returns:
            str | None: Random college of education name or acronym, or None if no colleges of education are found.
        """
        if location:
            locations = self.school_provider.get_colleges_of_education_by_location(
                location,
            )
            if not locations:
                return None
            colleges = [
                school["acronym"] if acronym else school["name"] for school in locations
            ]
            return random.choice(colleges) if colleges else None

        colleges_of_education = self.school_provider.get_colleges_of_education()
        if not colleges_of_education:
            return None
        college_names = [
            school["acronym"] if acronym else school["name"]
            for school in colleges_of_education
        ]
        return random.choice(college_names) if college_names else None

    def federal_university(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random federal university.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random federal university at that location.
            Defaults to None.

        Returns:
            str | None: Random federal university name or acronym, or None if no federal universities are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            federal_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "Federal"
            ]
            universities = [
                school["acronym"] if acronym else school["name"]
                for school in federal_universities
            ]
            return random.choice(universities) if universities else None

        federal_universities = self.school_provider.get_federal_universities()
        if not federal_universities:
            return None
        universities = [
            school["acronym"] if acronym else school["name"]
            for school in federal_universities
        ]
        return random.choice(universities) if universities else None

    def federal_polytechnic(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random federal polytechnic.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random federal polytechnic at that location.
            Defaults to None.

        Returns:
            str | None: Random federal polytechnic name or acronym, or None if no federal polytechnics are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            federal_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "Federal"
            ]
            polytechnics = [
                school["acronym"] if acronym else school["name"]
                for school in federal_polytechnics
            ]
            return random.choice(polytechnics) if polytechnics else None

        federal_polytechnics = self.school_provider.get_federal_polytechnics()
        if not federal_polytechnics:
            return None
        polytechnics = [
            school["acronym"] if acronym else school["name"]
            for school in federal_polytechnics
        ]
        return random.choice(polytechnics) if polytechnics else None

    def federal_college_of_education(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random federal college of education.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random federal college of education at that location.
            Defaults to None.

        Returns:
            str | None: Random federal college of education name or acronym, or None if no federal colleges of education are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            federal_colleges_of_education = [
                school
                for school in locations
                if school["type"] == "College of Education"
                and school["ownership"] == "Federal"
            ]
            colleges = [
                school["acronym"] if acronym else school["name"]
                for school in federal_colleges_of_education
            ]
            return random.choice(colleges) if colleges else None

        federal_colleges_of_education = (
            self.school_provider.get_federal_colleges_of_education()
        )
        if not federal_colleges_of_education:
            return None
        colleges = [
            school["acronym"] if acronym else school["name"]
            for school in federal_colleges_of_education
        ]
        return random.choice(colleges) if colleges else None

    def state_university(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random state university.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random state university at that location.
            Defaults to None.

        Returns:
            str | None: Random state university name or acronym, or None if no state universities are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            state_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "State"
            ]
            universities = [
                school["acronym"] if acronym else school["name"]
                for school in state_universities
            ]
            return random.choice(universities) if universities else None

        state_universities = self.school_provider.get_state_universities()
        if not state_universities:
            return None
        universities = [
            school["acronym"] if acronym else school["name"]
            for school in state_universities
        ]
        return random.choice(universities) if universities else None

    def state_polytechnic(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random state polytechnic.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random state polytechnic at that location.
            Defaults to None.

        Returns:
            str | None: Random state polytechnic name or acronym, or None if no state polytechnics are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            state_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "State"
            ]
            polytechnics = [
                school["acronym"] if acronym else school["name"]
                for school in state_polytechnics
            ]
            return random.choice(polytechnics) if polytechnics else None

        state_polytechnics = self.school_provider.get_state_polytechnics()
        if not state_polytechnics:
            return None
        polytechnics = [
            school["acronym"] if acronym else school["name"]
            for school in state_polytechnics
        ]
        return random.choice(polytechnics) if polytechnics else None

    def state_college_of_education(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random state college of education.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random state college of education at that location.
            Defaults to None.

        Returns:
            str | None: Random state college of education name or acronym, or None if no state colleges of education are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            state_colleges_of_education = [
                school
                for school in locations
                if school["type"] == "College of Education"
                and school["ownership"] == "State"
            ]
            colleges = [
                school["acronym"] if acronym else school["name"]
                for school in state_colleges_of_education
            ]
            return random.choice(colleges) if colleges else None

        state_colleges_of_education = (
            self.school_provider.get_state_colleges_of_education()
        )
        if not state_colleges_of_education:
            return None
        colleges = [
            school["acronym"] if acronym else school["name"]
            for school in state_colleges_of_education
        ]
        return random.choice(colleges) if colleges else None

    def private_university(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random private university.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random private university at that location.
            Defaults to None.

        Returns:
            str | None: Random private university name or acronym, or None if no private universities are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            private_universities = [
                school
                for school in locations
                if school["type"] == "University" and school["ownership"] == "Private"
            ]
            universities = [
                school["acronym"] if acronym else school["name"]
                for school in private_universities
            ]
            return random.choice(universities) if universities else None

        private_universities = self.school_provider.get_private_universities()
        if not private_universities:
            return None
        universities = [
            school["acronym"] if acronym else school["name"]
            for school in private_universities
        ]
        return random.choice(universities) if universities else None

    def private_polytechnic(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random private polytechnic.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random private polytechnic at that location.
            Defaults to None.

        Returns:
            str | None: Random private polytechnic name or acronym, or None if no private polytechnics are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            private_polytechnics = [
                school
                for school in locations
                if school["type"] == "Polytechnic" and school["ownership"] == "Private"
            ]
            polytechnics = [
                school["acronym"] if acronym else school["name"]
                for school in private_polytechnics
            ]
            return random.choice(polytechnics) if polytechnics else None

        private_polytechnics = self.school_provider.get_private_polytechnics()
        if not private_polytechnics:
            return None
        polytechnics = [
            school["acronym"] if acronym else school["name"]
            for school in private_polytechnics
        ]
        return random.choice(polytechnics) if polytechnics else None

    def private_college_of_education(
        self,
        acronym: bool = False,
        location: str | None = None,
    ) -> str | None:
        """Get a random private college of education.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
            Defaults to False.
            location (str | None, optional): If provided, get a random private college of education at that location.
            Defaults to None.

        Returns:
            str | None: Random private college of education name or acronym, or None if no federal colleges of education are found.
        """
        if location:
            locations = self.school_provider.get_schools_by_location(location)
            if not locations:
                return None
            private_colleges_of_education = [
                school
                for school in locations
                if school["type"] == "College of Education"
                and school["ownership"] == "Private"
            ]
            colleges = [
                school["acronym"] if acronym else school["name"]
                for school in private_colleges_of_education
            ]
            return random.choice(colleges) if colleges else None

        private_colleges_of_education = (
            self.school_provider.get_private_colleges_of_education()
        )
        if not private_colleges_of_education:
            return None
        colleges = [
            school["acronym"] if acronym else school["name"]
            for school in private_colleges_of_education
        ]
        return random.choice(colleges) if colleges else None

    def phone_number(
        self,
        network: str | None = None,
        prefix: str | None = None,
    ) -> str:
        """Generate a random Nigerian phone number.

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

    def email(self, tribe: str | None = None, gender: str | None = None) -> str | None:
        """Generate a random email address with optional tribe and gender filters.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.

        Returns:
            str | None: The generated email address, or none if no filters match.
        """
        return self.email_provider.generate_email(tribe, gender)
