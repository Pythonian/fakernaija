"""SchoolMixin to group related methods for the SchoolProvider."""

import random

from fakernaija.providers.education import SchoolProvider


class School:
    """Methods for the SchoolProvider."""

    def __init__(self) -> None:
        """Initializes the School mixin and its provider."""
        self.school_provider = SchoolProvider()

    def school(self, acronym: bool = False, location: str | None = None) -> str | None:
        """Get a random school name.

        Args:
            acronym (bool, optional): If True, return the acronym instead of the school name.
                                      Defaults to False.
            location (str | None, optional): If provided, get a random school by name at that location.
                                             Defaults to None.

        Returns:
            str | None: Random school name or acronym, or None if no schools are found.

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> school = naija.school()
                >>> print(f"Random school: {school}")
                'Random school: University of Lagos'

                >>> school_acronym = naija.school(acronym=True)
                >>> print(f"Random school acronym: {school_acronym}")
                'Random school acronym: UNILAG'

                >>> school = naija.school(location="Lagos")
                >>> print(f"Random school in Lagos: {school}")
                'Random school in Lagos: Lagos State University'
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

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> federal_school = naija.federal_school()
                >>> print(f"Random federal school: {federal_school}")
                'Random federal school: University of Nigeria'

                >>> federal_school_acronym = naija.federal_school(acronym=True)
                >>> print(f"Random federal school acronym: {federal_school_acronym}")
                'Random federal school acronym: UNN'

                >>> federal_school = naija.federal_school(location="Lagos")
                >>> print(f"Random federal school in Lagos: {federal_school}")
                'Random federal school in Lagos: University of Lagos'
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

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> state_school = naija.state_school()
                >>> print(f"Random state school: {state_school}")
                'Random state school: Lagos State University'

                >>> state_school_acronym = naija.state_school(acronym=True)
                >>> print(f"Random state school acronym: {state_school_acronym}")
                'Random state school acronym: LASU'

                >>> state_school = naija.state_school(location="Lagos")
                >>> print(f"Random state school in Lagos: {state_school}")
                'Random state school in Lagos: Lagos State University'
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

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> private_school = naija.private_school()
                >>> print(f"Random private school: {private_school}")
                'Random private school: Covenant University'

                >>> private_school_acronym = naija.private_school(acronym=True)
                >>> print(f"Random private school acronym: {private_school_acronym}")
                'Random private school acronym: CU'

                >>> private_school = naija.private_school(location="Ogun")
                >>> print(f"Random private school in Ogun: {private_school}")
                'Random private school in Ogun: Babcock University'
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

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
        .. code-block:: python

            >>> from fakernaija.faker import Faker
            >>> naija = Faker()

            >>> university = naija.university()
            >>> print(f"Random university: {university}")
            'Random university: University of Ibadan'

            >>> university_acronym = naija.university(acronym=True)
            >>> print(f"Random university acronym: {university_acronym}")
            'Random university acronym: UI'

            >>> university = naija.university(location="Lagos")
            >>> print(f"Random university in Lagos: {university}")
            'Random university in Lagos: University of Lagos'
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

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
        .. code-block:: python

            >>> from fakernaija.faker import Faker
            >>> naija = Faker()

            >>> polytechnic = naija.polytechnic()
            >>> print(f"Random polytechnic: {polytechnic}")
            'Random polytechnic: Yaba College of Technology'

            >>> polytechnic_acronym = naija.polytechnic(acronym=True)
            >>> print(f"Random polytechnic acronym: {polytechnic_acronym}")
            'Random polytechnic acronym: YABATECH'

            >>> polytechnic = naija.polytechnic(location="Kaduna")
            >>> print(f"Random polytechnic in Kaduna: {polytechnic}")
            'Random polytechnic in Kaduna: Kaduna Polytechnic'
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
            location (str | None, optional): If provided, get a random college of education at that location. Defaults to None.

        Returns:
            str | None: Random college of education name or acronym, or None if no colleges of education are found.

        Note:
            Entering a nonexistent location to the location parameter will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> college = naija.college_of_education()
                >>> print(f"Random college of education: {college}")
                'Random college of education: Adeyemi College of Education'

                >>> college = naija.college_of_education(acronym=True)
                >>> print(f"Random college of education acronym: {college}")
                'Random college of education acronym: ACE'

                >>> college = naija.college_of_education(location="Lagos")
                >>> print(f"College of education in Lagos: {college}")
                'College of education in Lagos: Federal College of Education (Technical), Akoka'

                >>> college = naija.college_of_education(location="Lagos", acronym=True)
                >>> print(f"College of education in Lagos acronym: {college}")
                'College of education in Lagos acronym: FCET'
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
            location (str | None, optional): If provided, get a random federal university at that location. Defaults to None.

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
            location (str | None, optional): If provided, get a random federal polytechnic at that location. Defaults to None.

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
            location (str | None, optional): If provided, get a random federal college of education at that location. Defaults to None.

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
