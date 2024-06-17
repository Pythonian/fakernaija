"""Name mixin to group related methods for the NameProvider."""

import random

from fakernaija.providers.name_provider import NameProvider


class Name:
    """Methods for the NameProvider."""

    def __init__(self) -> None:
        """Initializes the Name mixin and its provider."""
        self.name_provider = NameProvider()

    def full_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.
            gender (str | None, optional): The gender for which to generate the name.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random full name.

        Note:
            - Supported genders: male, female
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe or gender is not supported or if no names are available.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> full_name = naija.full_name()
                >>> print(f"Random full name: {full_name}")
                'Random full name: Ugochi Maduike'

                >>> full_name = naija.full_name(tribe="yoruba")
                >>> print(f"Random Yoruba full name: {full_name}")
                'Random Yoruba full name: Opeyemi Obisesan'

                >>> full_name = naija.full_name(gender="female")
                >>> print(f"Random female full name: {full_name}")
                'Random female full name: Ihuoma Maduabuchi'

                >>> full_name = naija.full_name(middle_name=True)
                >>> print(f"Random full name with middle name: {full_name}")
                'Random full name with middle name: Oluwaseyi Atanda Abilujegbe'

                >>> full_name = naija.full_name(tribe="igbo", gender="male")
                >>> print(f"Random Igbo male full name: {full_name}")
                'Random Igbo male full name: Ekene Muolokwu'
        """
        return self.name_provider.generate_full_name(tribe, gender, middle_name)

    def first_name(
        self,
        tribe: str | None = None,
        gender: str | None = None,
    ) -> str:
        """Generate a random first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.
            gender (str | None, optional): The gender of the name.

        Returns:
            str: A random first name.

        Note:
            - Supported genders: male, female
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe or gender is not supported or if no names are available.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> first_name = naija.first_name()
                >>> print(f"Random first name: {first_name}")
                'Random first name: Nasiru'

                >>> first_name = naija.first_name(tribe="yoruba")
                >>> print(f"Random Yoruba first name: {first_name}")
                'Random Yoruba first name: Adebayo'

                >>> first_name = naija.first_name(gender="male")
                >>> print(f"Random male first name: {first_name}")
                'Random male first name: Ade'

                >>> first_name = naija.first_name(tribe="igbo", gender="male")
                >>> print(f"Random Igbo male first name: {first_name}")
                'Random Igbo male first name: Chidi'
        """
        return self.name_provider.generate_first_name(tribe, gender)

    def last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random last name.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported or if no names are available.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> last_name = naija.last_name()
                >>> print(f"Random last name: {last_name}")
                'Random last name: Okonkwo'

                >>> last_name = naija.last_name(tribe="hausa")
                >>> print(f"Random Hausa last name: {last_name}")
                'Random Hausa last name: Abubakar'
        """
        return self.name_provider.generate_last_name(tribe)

    def prefix(self) -> str:
        """Generates a random name prefix.

        Returns:
            str: A random name prefix.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> name_prefix = naija.prefix()
                >>> print(f"Random name prefix: {name_prefix}")
                'Random name prefix: Prof.'
        """
        prefixes = [
            "Mr.",
            "Mrs.",
            "Miss",
            "Master",
            "Mister",
            "Madam",
            "Prof.",
            "J.P",
            "Chief",
            "Oba",
            "Otunba",
            "Erelu",
            "Prince",
            "Princess",
            "Lolo",
            "Igwe",
            "Obi",
            "Obong",
            "Iyalode",
            "Emir",
            "Waziri",
            "Olu",
            "Alhaja",
            "Alhaji",
            "Hajia",
            "Lady",
            "Dr.",
            "Engr.",
            "Tpl",
            "Barrister",
        ]
        return random.choice(prefixes)

    def male_prefix(self) -> str:
        """Generates a random male name prefix.

        Returns:
            str: A random male name prefix.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> male_name_prefix = naija.male_prefix()
                >>> print(f"Random male name prefix: {male_name_prefix}")
                'Random male name prefix: Mr.'
        """
        prefixes = [
            "Mr.",
            "Master",
            "Mister",
            "Chief",
            "Oba",
            "Otunba",
            "Prince",
            "Prof.",
            "Dr.",
            "Alhaji",
            "Engr.",
            "Tpl",
            "Barrister",
            "Igwe",
            "Obi",
            "Obong",
            "Emir",
            "Waziri",
            "Olu",
        ]
        return random.choice(prefixes)

    def female_prefix(self) -> str:
        """Generates a random female name prefix.

        Returns:
            str: A random female name prefix.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> female_name_prefix = naija.female_prefix()
                >>> print(f"Random female name prefix: {female_name_prefix}")
                'Random female name prefix: Princess'
        """
        prefixes = [
            "Mrs.",
            "Miss",
            "Madam",
            "Chief",
            "Lady",
            "Princess",
            "Erelu",
            "Prof.",
            "Dr. (Mrs.)",
            "Hajia",
            "Lady (Mrs.)",
            "Alhaja",
            "Lolo",
            "Iyalode",
        ]
        return random.choice(prefixes)

    def traditional_male_title(self) -> str:
        """Generates a random traditional male title or honorific.

        Returns:
            str: A random traditional male title or honorific.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> male_title = naija.traditional_male_title()
                >>> print(f"Random traditional male title: {male_title}")
                'Random traditional male title: Otunba'
        """
        titles = [
            "Chief",
            "Oba",
            "Otunba",
            "Prince",
            "Alhaji",
            "Igwe",
            "Obi",
            "Obong",
            "Emir",
            "Waziri",
            "Olu",
        ]
        return random.choice(titles)

    def traditional_female_title(self) -> str:
        """Generates a random traditional female title or honorific.

        Returns:
            str: A random traditional female title or honorific.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> female_title = naija.traditional_female_title()
                >>> print(f"Random traditional female title: {female_title}")
                'Random traditional female title: Erelu'
        """
        titles = [
            "Chief",
            "Erelu",
            "Princess",
            "Lady (Mrs.)",
            "Hajia",
            "Alhaja",
            "Lolo",
            "Iyalode",
        ]
        return random.choice(titles)

    def professional_title(self) -> str:
        """Generates a random professional title.

        Returns:
            str: A random professional title.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> professional_title = naija.professional_title()
                >>> print(f"Random professional title: {professional_title}")
                'Random professional title: Barrister'
        """
        titles = ["Dr.", "Engr.", "Tpl", "Barrister", "Prof."]
        return random.choice(titles)
