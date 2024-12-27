"""Email mixin to group related methods for the EmailProvider."""

from fakernaija.providers import EmailProvider


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
        name: str | None = None,
    ) -> str:
        """Generate a random email address with optional parameters.

        Args:
            tribe (str | None, optional): The ethnic group to filter by.
                Defaults to None.
            gender (str | None, optional): The gender to filter by.
                Defaults to None.
            domain (str | None, optional): The domain to use for the email.
                Defaults to None.
            name (str | None, optional): The name to use for the email.
                Defaults to None.

        Returns:
            str: The generated email address.

        Raises:
            ValueError: If the domain is invalid or if no matching data
                        is found for the given tribe or gender.

        Note:
            - Gender options: male, female
            - Tribe options: yoruba, igbo, hausa, edo, fulani, ijaw

        Examples:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> email = naija.email()
                >>> print(f"Random email: {email}")
                Random email: ugochi.maduike@gmail.com

                >>> for _ in range(3):
                ...     print(naija.email())
                ...
                osazeeiyamu26@gov.ng
                ogba.ogburu@edu.ng
                bello.moussa@mail.com

                >>> email = naija.email(name="Ugochi Maduike")
                >>> print(f"Generate email from given name: {email}")
                Generate email from given name: maduike.ugochi6@yahoo.com

                >>> email = naija.email(tribe="igbo")
                >>> print(f"Random email with tribe filter: {email}")
                Random email with tribe filter: ugochi.maduike@gmail.com

                >>> email = naija.email(domain="edu.ng")
                >>> print(f"Random email with domain filter: {email}")
                Random email with domain filter: maduike.ugochi1999@edu.ng

                >>> email = naija.email(gender="female")
                >>> print(f"Random email with gender filter: {email}")
                Random email with gender filter: ugochi.maduike@gmail.com

                >>> email = naija.email(tribe="igbo", gender="female", domain="unn.edu.ng")
                >>> print(f"Random email with multiple filters: {email}")
                Random email with multiple filters: ugochi.maduike@unn.edu.ng
        """
        return self.email_provider.generate_email(
            tribe,
            gender,
            domain,
            name,
        )
