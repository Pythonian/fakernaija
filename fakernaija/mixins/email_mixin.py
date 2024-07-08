"""Email mixin to group related methods for the EmailProvider."""

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

                >>> email = naija.email(tribe="igbo")
                >>> print(f"Random email with tribe filter: {email}")
                'Random email with tribe filter: ugochi.maduike@gmail.com'

                >>> email = naija.email(gender="female")
                >>> print(f"Random email with gender filter: {email}")
                'Random email with gender filter: ugochi.maduike@gmail.com'

                >>> email = naija.email(tribe="igbo", gender="female", domain="unn.edu.ng")
                >>> print(f"Random email with multiple filters: {email}")
                'Random email with multiple filters: ugochi.maduike@unn.edu.ng'
        """
        return self.email_provider.generate_email(tribe, gender, domain)
