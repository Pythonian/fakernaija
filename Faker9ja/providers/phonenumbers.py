import random


class PhoneNumberProvider:
    def __init__(self):
        self.network_prefixes = {
            "mtn": ["0803", "0806", "0813", "0816", "0810", "0814", "0903", "0906"],
            "glo": ["0805", "0807", "0811", "0815", "0905"],
            "airtel": ["0802", "0808", "0812", "0708", "0701", "0902", "0907"],
            "9mobile": ["0809", "0817", "0818", "0908", "0909"],
        }
        self.all_prefixes = [
            prefix for prefixes in self.network_prefixes.values() for prefix in prefixes
        ]

    def generate_phone_number(self, prefix):
        """
        Generates a phone number with the given prefix.
        Args:
            prefix (str): The prefix of the phone number.
        Returns:
            str: A valid Nigerian phone number with the specified prefix.
        """
        return prefix + "".join(random.choices("0123456789", k=7))

    def phone_number(self, network=None, prefix=None):
        """
        Generates a random Nigerian phone number, or a phone number
        based on the specified network or prefix.
        Args:
            network (str, optional):
                The name of the network ('mtn', 'glo', 'airtel', '9mobile').
                Defaults to None.
            prefix (str, optional):
                The prefix of the phone number. Defaults to None.
        Returns:
            str: A valid Nigerian phone number.
        """
        if network and prefix:
            if prefix not in self.network_prefixes.get(network.lower(), []):
                raise ValueError(
                    f"The prefix '{prefix}' is not valid for the network '{network}'. "
                    f"Please use one of the following prefixes for {network}: {self.network_prefixes[network.lower()]}"
                )

        if prefix:
            if prefix in self.all_prefixes:
                return self.generate_phone_number(prefix)
            else:
                raise ValueError(
                    f"Prefix '{prefix}' is not recognized. Please use one of the following: {self.all_prefixes}"
                )

        if network:
            if network.lower() in self.network_prefixes:
                prefix = random.choice(self.network_prefixes[network.lower()])
                return self.generate_phone_number(prefix)
            else:
                raise ValueError(
                    f"Network '{network}' is not recognized. Please use one of the following: {list(self.network_prefixes.keys())}"
                )

        prefix = random.choice(self.all_prefixes)
        return self.generate_phone_number(prefix)
