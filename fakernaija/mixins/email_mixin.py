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
    ) -> str | None:
        """Generate a random email address with optional tribe and gender filters.

        Args:
            tribe (str | None, optional): The ethnic group to filter by. Defaults to None.
            gender (str | None, optional): The gender to filter by. Defaults to None.
            domain (str | None, optional): The domain to use for the email. Defaults to None.

        Returns:
            str | None: The generated email address or None if no matching data is found or the domain is invalid.

        Note:
            - Supported genders: male, female
            - Supported tribes: yoruba, igbo, hausa, edo, fulani, ijaw

        Caution:
            Entering a gender or an ethnic group which is not (yet) supported or an invalid domain will return None.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> email = naija.email()
                >>> print(f"Random email: {email}")
                'Random email: chinedu.okafor@gmail.com'

                >>> email = naija.email(tribe="yoruba")
                >>> print(f"Random Yoruba email: {email}")
                'Random Yoruba email: adetutu.akinwale@yahoo.com'

                >>> email = naija.email(gender="female")
                >>> print(f"Random female email: {email}")
                'Random female email: chioma.okeke@gmail.com'

                >>> email = naija.email(domain="abia.gov.ng")
                >>> print(f"Random email with custom domain: {email}")
                'Random email with custom domain: ifeanyi.nwosu@abia.gov.ng'

                >>> email = naija.email(tribe="igbo", gender="male", domain="unn.edu.ng")
                >>> print(f"Random Igbo male email with custom domain: {email}")
                'Random Igbo male email with custom domain: ekene.muolokwu@unn.edu.ng'
        """
        return self.email_provider.generate_email(tribe, gender, domain)
