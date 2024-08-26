"""MaritalStatusProvider module."""


class MaritalStatusProvider:
    """A provider class to access marital status data."""

    def __init__(self) -> None:
        """Initializes the MaritalStatusProvider."""
        self.statuses = [
            "Annulled",
            "Divorced",
            "Engaged",
            "Married",
            "Separated",
            "Single",
            "Widowed",
        ]

    def get_marital_statuses(self) -> list[str]:
        """Returns a list of all marital statuses.

        Returns:
            list[str]: A list of marital statuses.
        """
        return self.statuses
