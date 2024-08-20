"""SchoolMixin to group related methods for the SchoolProvider."""

import random

from fakernaija.providers import SchoolProvider
from fakernaija.utils import get_unique_value


class School:
    """Mixin class for generating random Nigerian schools and school names."""

    def __init__(self) -> None:
        """Initializes the School mixin and its provider."""
        self.school_provider = SchoolProvider()
        self._used_school_names: set[str] = set()

    def school(
        self,
        ownership: str | None = None,
        state: str | None = None,
        school_type: str | None = None,
    ) -> dict[str, str] | None:
        """Get a random school object based on optional parameters.

        Args:
            ownership (str | None, optional): Filter by ownership.
            state (str | None, optional): Filter by state.
            school_type (str | None, optional): Filter by type.

        Returns:
            dict[str, str] | None: A dictionary representing a random school or None if no match found.

        Raises:
            ValueError: If an unsupported ownership or school_type is provided.

        Note:
            - Ownership options: federal, state, private
            - School type options: university, polytechnic, college
            - State options: 36 states in Nigeria + FCT

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> school = naija.school()
                >>> print(f"Random school: {school}")
                Random school: {'name': 'University of Lagos', 'acronym': 'UNILAG', 'state': 'Lagos', 'type': 'university', 'ownership': 'Federal'}

                >>> school = naija.school(ownership="federal")
                >>> print(f"Random federal school: {school}")
                Random federal school: {'name': 'Ahmadu Bello University', 'acronym': 'ABU', 'state': 'Kaduna', 'type': 'university', 'ownership': 'Federal'}

                >>> school = naija.school(state="lagos")
                >>> print(f"Random school in Lagos: {school}")
                Random school in Lagos: {'name': 'Lagos State University', 'acronym': 'LASU', 'state': 'Lagos', 'type': 'university', 'ownership': 'State'}

                >>> school = naija.school(school_type="polytechnic")
                >>> print(f"Random polytechnic: {school}")
                Random polytechnic: {'name': 'Yaba College of Technology', 'acronym': 'YABATECH', 'state': 'Lagos', 'type': 'polytechnic', 'ownership': 'Federal'}

                >>> school = naija.school(ownership="federal", state="lagos", school_type="university")
                >>> print(f"Random federal university in Lagos: {school}")
                Random federal university in Lagos: {'name': 'University of Lagos', 'acronym': 'UNILAG', 'state': 'Lagos', 'type': 'university', 'ownership': 'Federal'}
        """
        schools = self.school_provider.get_schools(
            ownership,
            state,
            school_type,
        )
        return random.choice(schools) if schools else None

    def school_name(
        self,
        acronym: bool = False,
        ownership: str | None = None,
        state: str | None = None,
        school_type: str | None = None,
    ) -> str | None:
        """Get a random school name or acronym based on optional parameters.

        Args:
            acronym (bool, optional): If True, return the acronym instead
                of the full name. Defaults to False.
            ownership (str | None, optional): Filter by ownership.
            state (str | None, optional): Filter by state.
            school_type (str | None, optional): Filter by type.

        Returns:
            str | None: A random school name or acronym or None
                if no match found.

        Raises:
            ValueError: If an unsupported ownership or school_type is provided.

        Note:
            - Ownership options: federal, state, private
            - School type options: university, polytechnic, college
            - State options: 36 states in Nigeria + FCT

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> school_name = naija.school_name()
                >>> print(f"Random school name: {school_name}")
                Random school name: University of Lagos

                >>> for _ in range(3):
                ...     print(naija.school_name())
                ...
                Federal College of Education, Abeokuta
                Kwara State Polytechnic
                Yaba College of Technology

                >>> school_acronym = naija.school_name(acronym=True)
                >>> print(f"Random school acronym: {school_acronym}")
                Random school acronym: UNILAG

                >>> school_name = naija.school_name(state="Lagos")
                >>> print(f"Random school in Lagos: {school_name}")
                Random school in Lagos: Lagos State University

                >>> school_name = naija.school_name(school_type="university")
                >>> print(f"Random university name: {school_name}")
                Random university name: University of Ibadan

                >>> school_name = naija.school_name(ownership="private")
                >>> print(f"Random private school: {school_name}")
                Random private school: Al-Hikmah University

                >>> school_acronym = naija.school_name(acronym=True, ownership="federal", state="Lagos", school_type="university")
                >>> print(f"Random federal university acronym in Lagos: {school_acronym}")
                Random federal university acronym in Lagos: UNILAG
        """
        school_names = self.school_provider.get_school_names(
            ownership,
            state,
            school_type,
            acronym,
        )

        if not school_names:
            return None

        school_name = get_unique_value(school_names, self._used_school_names)
        self._used_school_names.add(school_name)
        return school_name
