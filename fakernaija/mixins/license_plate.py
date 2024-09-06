"""LicensePlate mixin to group related methods for the LicensePlateProvider."""

from fakernaija.providers import LicensePlateProvider


class LicensePlate:
    """Mixin class to add license plate generation."""

    def __init__(self) -> None:
        """Initializes the State mixin and its provider."""
        self.license_plate_provider = LicensePlateProvider()

    def license_plate(self, state: str | None = None) -> str:
        """Generate a random license plate.

        Args:
            state (str | None, optional): The state to generate the license plate for.

        Returns:
            str: The generated license plate.

        Raises:
            ValueError: If the specified state does not exist.

        Note:
            - State options: 36 States in Nigeria + FCT.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Naija
                >>> naija = Naija()

                >>> license_plate = naija.license_plate()
                >>> print(f"Random license plate number: {license_plate}")
                Random license plate number: KPU-937UK

                >>> for _ in range(3):
                ...     print(naija.license_plate())
                ...
                SSM-110VK
                ABJ-127HP
                GAN-322LJ

                >>> license_plate = naija.license_plate(state="FCT")
                >>> print(f"Random license plate number from a specific state: {license_plate}")
                Random license plate number from a specific state: EZA-352CC
        """
        return self.license_plate_provider.generate_license_plate(state=state)
