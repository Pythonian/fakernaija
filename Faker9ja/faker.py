from Faker9ja.providers.names import NameProvider


class NameGenerator:
    """
    A class for generating Nigerian names.

    This class provides methods to generate Nigerian names,
    including first names, last names, and full names.

    Usage:
        from Faker9ja.faker import NameGenerator

        faker = NameGenerator()

        print("Random Yoruba names:")
        for i in range(5):
            full_name = faker.full_name(ethnic_group="yoruba")
            print(full_name)
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
