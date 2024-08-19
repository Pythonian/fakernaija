"""Name mixin to group related methods for the NameProvider."""

from fakernaija.providers import NameProvider
from fakernaija.utils import get_unique_value


class Name:
    """Methods for the NameProvider."""

    def __init__(self) -> None:
        """Initializes the Name mixin and its provider."""
        self.name_provider = NameProvider()
        self._used_prefixes: set[str] = set()

    def first_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random first name with optional parameters.

        Args:
            tribe (str | None, optional): The tribe from which to generate the name.
            gender (str | None, optional): The gender from which to generate the name.

        Returns:
            str: A randomly generated first name.

        Note:
            - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
            - Gender options: male, female

        Raises:
            ValueError: If the specified tribe or gender is not supported.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> first_name = naija.first_name()
                >>> print(f"Random first name: {first_name}")
                Random first name: Nasiru

                >>> for _ in range(3):
                ...     print(naija.first_name())
                ...
                Izuchukwu
                Yinka
                Muhammadu

                >>> first_name_tribe = naija.first_name(tribe="yoruba")
                >>> print(f"Random first name: {first_name_tribe}")
                Random first name: Opeyemi

                >>> female_first_name = naija.first_name(gender="female")
                >>> print(f"Random female first name: {female_first_name}")
                Random female first name: Somtochi

                >>> male_first_name_tribe = naija.first_name(tribe="yoruba", gender="male")
                >>> print(f"Random Yoruba male first name: {male_first_name_tribe}")
                Random Yoruba male first name: Seyi
        """
        return self.name_provider.generate_first_name(
            tribe=tribe,
            gender=gender,
        )

    def last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name with optional parameter.

        Args:
            tribe (str | None, optional): The tribe from which to generate the last name.

        Returns:
            str: A randomly generated last name.

        Note:
            - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> last_name = naija.last_name()
                >>> print(f"Random last name: {last_name}")
                Random last name: Okonkwo

                >>> for _ in range(3):
                ...     print(naija.last_name())
                ...
                Bello
                Ajiteru
                Lawal

                >>> last_name_tribe = naija.last_name(tribe="hausa")
                >>> print(f"Random Hausa last name: {last_name_tribe}")
                Random Hausa last name: Abubakar
        """
        return self.name_provider.generate_last_name(tribe=tribe)

    def full_name(
        self,
        middle_name: bool = False,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random full name with optional parameters.

        Args:
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.
            tribe (str | None, optional): The tribe from which to generate the name.
            gender (str | None, optional): The gender from which to generate the name.

        Returns:
            str: A randomly generated full name.

        Note:
            - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw
            - Gender options: male, female

        Raises:
            ValueError: If the specified tribe or gender is not supported.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> full_name = naija.full_name()
                >>> print(f"Random full name: {full_name}")
                Random full name: Ugochi Maduike

                >>> for _ in range(3):
                ...     print(naija.full_name())
                ...
                Ozioma Anyaegbunam
                Oluwatosin Lemboye
                Osawaru Ikhine

                >>> full_name = naija.full_name(middle_name=True)
                >>> print(f"Random full name with middle name: {full_name}")
                Random full name with middle name: Kosisochukwu Somtochukwu Mbakwe

                >>> full_name = naija.full_name(tribe="yoruba")
                >>> print(f"Random Yoruba full name: {full_name}")
                Random Yoruba full name: Opeyemi Obisesan

                >>> full_name = naija.full_name(tribe="yoruba", middle_name=True)
                >>> print(f"Random Yoruba full name with middle name: {full_name}")
                Random Yoruba full name with middle name: Babajide Olusola Sanwo-olu

                >>> full_name = naija.full_name(gender="female")
                >>> print(f"Random female full name: {full_name}")
                Random female full name: Chisom Nnabude

                >>> full_name = naija.full_name(gender="female", middle_name=True)
                >>> print(f"Random female full name with middle name: {full_name}")
                Random female full name with middle name: Ifeoma Chinecherem Nwankwo

                >>> full_name = naija.full_name(tribe="edo", gender="female", middle_name=True)
                >>> print(f"Random female full name with middle name from Edo tribe: {full_name}")
                Random female full name with middle name from Edo tribe: Osazee Osahon Ogiemwonyi
        """
        return self.name_provider.generate_full_name(
            middle_name=middle_name,
            tribe=tribe,
            gender=gender,
        )

    def prefix(
        self,
        gender: str | None = None,
        title: str | None = None,
    ) -> str:
        """Generates a random name prefix based on optional parameter.

        Args:
            gender (str | None, optional): The gender for which to generate the prefix.
            title (str | None, optional): The title type for which to generate the prefix.

        Returns:
            str: A randomly generated prefix.

        Raises:
            ValueError: If an invalid gender or title is provided.

        Note:
            - Gender options: male, female
            - Title options: traditional, professional

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> name_prefix = naija.prefix()
                >>> print(f"Random name prefix: {name_prefix}")
                Random name prefix: Prof.

                >>> for _ in range(3):
                ...     print(naija.prefix())
                ...
                Master
                Alhaji
                Miss

                >>> male_prefix = naija.prefix(gender="male")
                >>> print(f"Random male name prefix: {male_prefix}")
                Random male name prefix: Mr.

                >>> female_prefix = naija.prefix(gender="female")
                >>> print(f"Random female name prefix: {female_prefix}")
                Random female name prefix: Mrs.

                >>> professional_prefix = naija.prefix(title="professional")
                >>> print(f"Random professional prefix: {professional_prefix}")
                Random professional prefix: Dr.

                >>> male_traditional_prefix = naija.prefix(gender="male", title="traditional")
                >>> print(f"Random male traditional prefix: {male_traditional_prefix}")
                Random male traditional prefix: Waziri

                >>> female_traditional_prefix = naija.prefix(gender="female", title="traditional")
                >>> print(f"Random female traditional prefix: {female_traditional_prefix}")
                Random female traditional prefix: Iyalode
        """
        if title not in {None, "professional", "traditional"}:
            msg = f"Invalid title '{title}'. Must be 'professional' or 'traditional'."
            raise ValueError(msg)

        if gender not in {None, "male", "female"}:
            msg = f"Invalid gender '{gender}'. Must be 'male' or 'female'."
            raise ValueError(msg)

        prefixes = self.name_provider.generate_prefixes(title, gender)
        prefix = get_unique_value(prefixes, self._used_prefixes)
        self._used_prefixes.add(prefix)
        return prefix
