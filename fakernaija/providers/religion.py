"""ReligionProvider module."""


class ReligionProvider:
    """A provider class to access religion data."""

    def __init__(self) -> None:
        """Initializes the ReligionProvider."""
        self.religions = [
            "Christian",
            "Muslim",
            "Traditionalist",
            "Atheist",
            "Secularist",
            "Humanist",
            "Judaist",
        ]

    def get_religions(self) -> list[str]:
        """Returns a list of all religions.

        Returns:
            list[str]: A list of religions.
        """
        return self.religions
