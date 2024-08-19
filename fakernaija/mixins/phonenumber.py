"""PhoneNumber mixin to group related methods for the PhoneNumberProvider."""

from fakernaija.providers import PhoneNumberProvider


class PhoneNumber:
    """Methods for the PhoneNumberProvider."""

    def __init__(self) -> None:
        """Initializes the PhoneNumber mixin and its provider."""
        self.phonenumber_provider = PhoneNumberProvider()

    def phone_number(
        self,
        network: str | None = None,
        prefix: str | None = None,
    ) -> str:
        """Generate a random phone number with optional network and prefix filters.

        Args:
            network (str, optional): The name of the network. Defaults to None.
            prefix (str, optional): The prefix of the phone number. Defaults to None.

        Returns:
            str: A valid Nigerian phone number.

        Note:
            Available networks and prefixes:
                - mtn: 0703, 0706, 0803, 0806, 0813, 0816, 0810, 0814, 0903, 0906, 0913, 0916
                - glo: 0705, 0805, 0807, 0811, 0815, 0905, 0915
                - airtel: 0802, 0808, 0812, 0708, 0701, 0901, 0902, 0907
                - etisalat: 0809, 0817, 0818, 0908, 0909

        Raises:
            ValueError: If the given prefix is not valid or the network and prefix
                combination does not match.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> phone = naija.phone_number()
                >>> print(f"Random phone number: {phone}")
                Random phone number: 08051234567

                >>> for _ in range(3):
                ...     print(naija.phone_number())
                ...
                09054519464
                09025038192
                09016604216

                >>> phone = naija.phone_number(network="mtn")
                >>> print(f"Random MTN phone number: {phone}")
                Random MTN phone number: 08031234567

                >>> phone = naija.phone_number(prefix="0909")
                >>> print(f"Random phone number with prefix 0909: {phone}")
                Random phone number with prefix 0909: 09091234567

                >>> phone = naija.phone_number(network="airtel", prefix="0902")
                >>> print(f"Random Airtel phone number with prefix 0902: {phone}")
                Random Airtel phone number with prefix 0902: 09021234567
        """
        return self.phonenumber_provider.generate_phone_number(
            network=network,
            prefix=prefix,
        )
