"""NameMixin to group related methods for the NameProvider."""

import random

from fakernaija.providers.names import NameProvider


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

    def male_full_name(
        self,
        tribe: str | None = None,
        middle_name: bool = False,
    ) -> str:
        """Generate a random male full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random male full name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> male_name = naija.male_full_name()
                >>> print(f"Random male full name: {male_name}")
                'Random male full name: Chukwudi Okeke'

                >>> male_name = naija.male_full_name(tribe="yoruba")
                >>> print(f"Random Yoruba male full name: {male_name}")
                'Random Yoruba male full name: Adeyemi Bakare'

                >>> male_name = naija.male_full_name(middle_name=True)
                >>> print(f"Random male full name with middle name: {male_name}")
                'Random male full name with middle name: Oluwaseun Adebayo Adekunle'

                >>> male_name = naija.male_full_name(tribe="igbo", middle_name=True)
                >>> print(f"Random Igbo male full name with middle name: {male_name}")
                'Random Igbo male full name: Ifeanyi Dumebi Eze'
        """
        return self.name_provider.generate_full_name(
            tribe,
            gender="male",
            middle_name=middle_name,
        )

    def female_full_name(
        self,
        tribe: str | None = None,
        middle_name: bool = False,
    ) -> str:
        """Generate a random female full name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.
            middle_name (bool, optional): Whether to include a middle name. Defaults to False.

        Returns:
            str: A random female full name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> female_name = naija.female_full_name()
                >>> print(f"Random female full name: {female_name}")
                'Random female full name: Chioma Okafor'

                >>> female_name = naija.female_full_name(tribe="yoruba")
                >>> print(f"Random Yoruba female full name: {female_name}")
                'Random Yoruba female full name: Adetutu Akinwale'

                >>> female_name = naija.female_full_name(middle_name=True)
                >>> print(f"Random female full name with middle name: {female_name}")
                'Random female full name with middle name: Eniola Adebisi Ademola'

                >>> female_name = naija.female_full_name(tribe="igbo", middle_name=True)
                >>> print(f"Random Igbo female full name with middle name: {female_name}")
                'Random Igbo female full name: Ugochi Ngozi Maduike'
        """
        return self.name_provider.generate_full_name(
            tribe,
            gender="female",
            middle_name=middle_name,
        )

    def first_name(self, tribe: str | None = None) -> str:
        """Generate a random first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random first name.

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
        """
        return self.name_provider.generate_first_name(tribe, gender=None)

    def male_first_name(self, tribe: str | None = None) -> str:
        """Generate a random male first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random male first name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> male_name = naija.male_first_name()
                >>> print(f"Random male first name: {male_name}")
                'Random male first name: Ade'

                >>> male_name = naija.male_first_name(tribe="igbo")
                >>> print(f"Random Igbo male first name: {male_name}")
                'Random Igbo male first name: Chidi'
        """
        return self.name_provider.generate_first_name(tribe, gender="male")

    def female_first_name(self, tribe: str | None = None) -> str:
        """Generate a random female first name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random female first name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> female_name = naija.female_first_name()
                >>> print(f"Random female first name: {female_name}")
                'Random female first name: Amina'

                >>> female_name = naija.female_first_name(tribe="yoruba")
                >>> print(f"Random Yoruba female first name: {female_name}")
                'Random Yoruba female first name: Sayo'
        """
        return self.name_provider.generate_first_name(tribe, gender="female")

    def last_name(self, tribe: str | None = None) -> str:
        """Generate a random last name.

        Args:
            tribe (str | None, optional): The ethnic group for which to generate the name.

        Returns:
            str: A random last name.

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
        titles = ["Chief", "Oba", "Otunba", "Prince", "Alhaji", "Igwe"]
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
        titles = ["Chief", "Erelu", "Princess", "Lady (Mrs.)", "Hajia", "Alhaja"]
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
