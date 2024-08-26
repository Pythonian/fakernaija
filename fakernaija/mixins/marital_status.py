"""MaritalStatus mixin module."""

from fakernaija.providers import MaritalStatusProvider
from fakernaija.utils import get_unique_value


class MaritalStatus:
    """A mixin providing methods to fetch and return marital status data."""

    def __init__(self) -> None:
        """Initializes the MaritalStatus mixin and sets up its provider."""
        self.marital_status_provider = MaritalStatusProvider()
        self._used_marital_statuses: set[str] = set()

    def marital_status(self) -> str:
        """Returns a random marital_status.

        Returns:
            str: A random marital_status.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> marital_status = naija.marital_status()
                >>> print(f"Random marital status: {marital_status}")
                Random marital_status: Separated

                >>> for _ in range(3):
                ...     print(naija.marital_status())
                ...
                Married
                Divorced
                Engaged
        """
        marital_statuses = self.marital_status_provider.get_marital_statuses()
        marital_status = get_unique_value(marital_statuses, self._used_marital_statuses)
        self._used_marital_statuses.add(marital_status)
        return marital_status
