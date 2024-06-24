"""EmailMixin to group related methods for the EmailProvider."""

from fakernaija.providers.email_provider import EmailProvider


class Email:
    """Methods for the EmailProvider."""

    def __init__(self) -> None:
        """Initializes the Email mixin and its provider."""
        self.email_provider = EmailProvider()

    def email(
        self,
        tribe: str | None = None,
        gender: str | None = None,
        domain: str | None = None,
    ) -> str:
        """Generate a random email address with optional tribe, gender, and domain filters.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.
            domain (str | None, optional): The domain to use for the email. Defaults to None.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If the domain is invalid or if no matching data is found for the given tribe or gender.

        Note:
            - Supported genders: male, female
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> email = naija.email()
                >>> print(f"Random email: {email}")
                'Random email: ugochi.maduike@gmail.com'

                >>> email = naija.email(tribe="igbo", gender="female", domain="unn.edu.ng")
                >>> print(f"Random email with multiple filters: {email}")
                'Random email with multiple filters: maduikeugochi99@unn.edu.ng'
        """
        return self.email_provider.generate_email(tribe, gender, domain)

    def email_by_tribe(self, tribe: str) -> str:
        """Generate a random email address filtered by tribe.

        Args:
            tribe (str): The ethnic group to filter by.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If no matching data is found for the given tribe.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> email = naija.email_by_tribe("igbo")
                >>> print(f"Random email: {email}")
                'Random email: chinedu.okafor@gmail.com'
        """
        return self.email_provider.generate_email(tribe=tribe)

    def email_by_gender(self, gender: str) -> str:
        """Generate a random email address filtered by gender.

        Args:
            gender (str): The gender to filter by.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If no matching data is found for the given gender.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> email = naija.email_by_gender("female")
                >>> print(f"Random email: {email}")
                'Random email: ugochi.maduike@gmail.com'
        """
        return self.email_provider.generate_email(gender=gender)

    def email_by_domain(self, domain: str) -> str:
        """Generate a random email address filtered by domain.

        Args:
            domain (str): The domain to use for the email.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If the domain is invalid.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> email = naija.email_by_domain("unn.edu.ng")
                >>> print(f"Random email: {email}")
                'Random email: ugochimaduike99@unn.edu.ng'
        """
        return self.email_provider.generate_email(domain=domain)
