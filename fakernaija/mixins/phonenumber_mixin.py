"""PhoneNumberMixin to group related methods for the PhoneNumberProvider."""

from fakernaija.providers.phonenumbers import PhoneNumberProvider


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
        """Generate a random Nigerian phone number.

        Args:
            network (str, optional):
                The name of the network. Defaults to None.
            prefix (str, optional):
                The prefix of the phone number. Defaults to None.

        Returns:
            str: A valid Nigerian phone number.

        Note:
            Available networks are: mtn, glo, airtel, etisalat

        Caution:
            Ensure that the prefix provided is valid for the selected network, else a ValueError will be raised.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> phone = naija.phone_number()
                >>> print(f"Random phone number: {phone}")
                'Random phone number: 08051234567'

                >>> phone = naija.phone_number(network="mtn")
                >>> print(f"Random MTN phone number: {phone}")
                'Random MTN phone number: 08031234567'

                >>> phone = naija.phone_number(prefix="0703")
                >>> print(f"Random phone number with prefix 0703: {phone}")
                'Random phone number with prefix 0703: 07031234567'

                >>> phone = naija.phone_number(network="airtel", prefix="0902")
                >>> print(f"Random Airtel phone number with prefix 0902: {phone}")
                'Random Airtel phone number with prefix 0902: 09021234567'
        """
        return self.phonenumber_provider.phone_number(network=network, prefix=prefix)
