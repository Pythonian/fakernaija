"""This module provides a PhoneNumberProvider class for generating Nigerian phone numbers based on specified network prefixes."""

import difflib
import random


class PhoneNumberProvider:
    """A class to provide Nigerian phone numbers."""

    def __init__(self) -> None:
        """Initializes the PhoneNumberProvider instance."""
        self.network_prefixes = {
            "mtn": [
                "0703",
                "0706",
                "0803",
                "0806",
                "0813",
                "0816",
                "0810",
                "0814",
                "0903",
                "0906",
                "0913",
                "0916",
            ],
            "glo": ["0705", "0805", "0807", "0811", "0815", "0905", "0915"],
            "airtel": ["0802", "0808", "0812", "0708", "0701", "0901", "0902", "0907"],
            "etisalat": ["0809", "0817", "0818", "0908", "0909"],
        }
        self.all_prefixes = [
            prefix for prefixes in self.network_prefixes.values() for prefix in prefixes
        ]

    def generate_random_phone_number(self, prefix: str) -> str:
        """Generates a random phone number with the given prefix.

        Args:
            prefix (str): The prefix of the phone number.

        Returns:
            str: A random phone number with the specified prefix.
        """
        return prefix + "".join(random.choices("0123456789", k=7))

    def generate_phone_number(
        self,
        network: str | None = None,
        prefix: str | None = None,
    ) -> str:
        """Generate a random Nigerian phone number.

        The phone number is either random or based on the specified network or prefix.

        Args:
            network (str | None, optional): The name of the network. Defaults to None.
            prefix (str | None, optional): The prefix of the phone number. Defaults to None.

        Returns:
            str: A valid Nigerian phone number.

        Raises:
            ValueError: If the provided prefix or network is not valid.
        """
        if (network and prefix) and prefix not in self.network_prefixes.get(
            network.lower(),
            [],
        ):
            msg = f"The prefix '{prefix}' is not valid for the network '{network}'. Please use one of the following prefixes for {network}: {self.network_prefixes[network.lower()]}"
            raise ValueError(msg)

        if prefix:
            if prefix in self.all_prefixes:
                return self.generate_random_phone_number(prefix)
            msg = (
                f"Prefix '{prefix}' is not recognized. "
                f"Please use one of the following: {self.all_prefixes}"
            )
            raise ValueError(msg)

        if network:
            network = network.lower()
            if network in self.network_prefixes:
                prefix = random.choice(self.network_prefixes[network])
                return self.generate_random_phone_number(prefix)

            # Suggest similar networks
            suggestions = difflib.get_close_matches(
                network, self.network_prefixes.keys(), n=3, cutoff=0.6
            )
            msg = (
                f"Network '{network}' is not recognized. "
                f"Did you mean: {', '.join(suggestions)}?"
                if suggestions
                else f"Network '{network}' is not recognized. "
                f"Please use one of the following: {list(self.network_prefixes.keys())}"
            )
            raise ValueError(msg)

        prefix = random.choice(self.all_prefixes)
        return self.generate_random_phone_number(prefix)
