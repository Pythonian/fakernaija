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
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name.

        Args:
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random full name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> full_name = naija.full_name()
                >>> print(f"Random full name: {full_name}")
                'Random full name: Ugochi Maduike'

                >>> full_name = naija.full_name(middle_name=True)
                >>> print(f"Random full name with middle name: {full_name}")
                'Random full name with middle name: Oluwaseyi Atanda Abilujegbe'
        """
        return self.name_provider.generate_full_name(middle_name=middle_name)

    def male_full_name(
        self,
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name for a male.

        Args:
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random male full name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> male_full_name = naija.male_full_name()
                >>> print(f"Random male full name: {male_full_name}")
                'Random male full name: Habeeb Bello'

                >>> male_full_name = naija.male_full_name(middle_name=True)
                >>> print(f"Random full name with middle name: {male_full_name}")
                'Random male full name with middle name: Oluwaseyi Atanda Abilujegbe'
        """
        return self.name_provider.generate_full_name(
            gender="male",
            middle_name=middle_name,
        )

    def female_full_name(
        self,
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name for a female.

        Args:
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random female full name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> female_full_name = naija.female_full_name()
                >>> print(f"Random female full name: {female_full_name}")
                'Random female full name: Ugochi Maduike'

                >>> female_full_name = naija.female_full_name(middle_name=True)
                >>> print(f"Random full name with middle name: {female_full_name}")
                'Random female full name with middle name: Ugochi Ihuoma Maduabuchi'
        """
        return self.name_provider.generate_full_name(
            gender="female",
            middle_name=middle_name,
        )

    def full_name_tribe(
        self,
        tribe: str,
        middle_name: bool = False,
    ) -> str:
        """Generate a random full name for a specific tribe.

        Args:
            tribe (str): The ethnic group for which to generate the name.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random full name for a specific tribe.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> full_name_tribe = naija.full_name_tribe('igbo')
                >>> print(f"Random full name: {full_name_tribe}")
                'Random full name: Ugochi Maduike'

                >>> full_name_tribe = naija.full_name_tribe(tribe='yoruba', middle_name=True)
                >>> print(f"Random yoruba full name with middle name: {full_name_tribe}")
                'Random yoruba full name with middle name: Oluwaseyi Atanda Obisesan'
        """
        return self.name_provider.generate_full_name(
            tribe=tribe,
            middle_name=middle_name,
        )

    def first_name(self) -> str:
        """Generate a random first name.

        Returns:
            str: A random first name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> first_name = naija.first_name()
                >>> print(f"Random first name: {first_name}")
                'Random first name: Nasiru'
        """
        return self.name_provider.generate_first_name()

    def first_name_tribe(self, tribe: str) -> str:
        """Generate a random first name by specified tribe.

        Args:
            tribe (str): The ethnic group from which to generate the name.

        Returns:
            str: A random first name by tribe.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> first_name_tribe = naija.first_name_tribe('yoruba')
                >>> print(f"Random first name: {first_name_tribe}")
                'Random first name: Opeyemi'
        """
        return self.name_provider.generate_first_name(tribe=tribe)

    def male_first_name(self) -> str:
        """Generate a random first name for a male.

        Returns:
            str: A random male first name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> male_first_name = naija.male_first_name()
                >>> print(f"Random male first name: {male_first_name}")
                'Random male first name: Ejike'
        """
        return self.name_provider.generate_first_name(gender="male")

    def female_first_name(self) -> str:
        """Generate a random first name for a female.

        Returns:
            str: A random female first name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> female_first_name = naija.female_first_name()
                >>> print(f"Random female first name: {female_first_name}")
                'Random female first name: Ugochi'
        """
        return self.name_provider.generate_first_name(gender="female")

    def male_first_name_tribe(self, tribe: str) -> str:
        """Generate a random first name for a male from a specific tribe.

        Args:
            tribe (str): The ethnic group for which to generate the name.

        Returns:
            str: A random male first name from specified tribe.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> first_name = naija.first_name()
                >>> print(f"Random first name: {first_name}")
                'Random first name: Nasiru'

                >>> male_first_name_tribe = naija.male_first_name_tribe("yoruba")
                >>> print(f"Random Yoruba male first name: {male_first_name_tribe}")
                'Random Yoruba male first name: Seyi'
        """
        return self.name_provider.generate_first_name(tribe=tribe, gender="male")

    def female_first_name_tribe(self, tribe: str) -> str:
        """Generate a random first name for a female from a specific tribe.

        Args:
            tribe (str): The ethnic group for which to generate the name.

        Returns:
            str: A random female first name from specified tribe.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> first_name = naija.first_name()
                >>> print(f"Random first name: {first_name}")
                'Random first name: Nasiru'

                >>> female_first_name_tribe = naija.female_first_name_tribe("yoruba")
                >>> print(f"Random Yoruba female first name: {female_first_name_tribe}")
                'Random Yoruba female first name: Sayo'
        """
        return self.name_provider.generate_first_name(tribe=tribe, gender="female")

    def last_name(self) -> str:
        """Generate a random last name.

        Returns:
            str: A random last name.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> last_name = naija.last_name()
                >>> print(f"Random last name: {last_name}")
                'Random last name: Okonkwo'
        """
        return self.name_provider.generate_last_name()

    def last_name_tribe(self, tribe: str) -> str:
        """Generate a random last name.

        Args:
            tribe (str): The ethnic group for which to generate the name.

        Returns:
            str: A random last name of a specified tribe.

        Note:
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Raises:
            ValueError: If the specified tribe is not supported.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> last_name_tribe = naija.last_name_tribe("hausa")
                >>> print(f"Random Hausa last name: {last_name_tribe}")
                'Random Hausa last name: Abubakar'
        """
        return self.name_provider.generate_last_name(tribe)

    def prefix(self) -> str:
        """Generates a random name prefix.

        Returns:
            str: A random name prefix.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
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

                >>> from fakernaija import Faker
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

                >>> from fakernaija import Faker
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

                >>> from fakernaija import Faker
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

                >>> from fakernaija import Faker
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

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> professional_title = naija.professional_title()
                >>> print(f"Random professional title: {professional_title}")
                'Random professional title: Barrister'
        """
        titles = ["Dr.", "Engr.", "Tpl", "Barrister", "Prof.", "Esq."]
        return random.choice(titles)
