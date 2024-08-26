"""Religion mixin module."""

from fakernaija.providers import ReligionProvider
from fakernaija.utils import get_unique_value


class Religion:
    """A mixin providing methods to fetch and return religion data."""

    def __init__(self) -> None:
        """Initializes the Religion mixin and sets up its provider."""
        self.religion_provider = ReligionProvider()
        self._used_religions: set[str] = set()

    def religion(self) -> str:
        """Returns a random religion.

        Returns:
            str: A random religion.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> religion = naija.religion()
                >>> print(f"Random religion: {religion}")
                Random religion: Atheist

                >>> for _ in range(3):
                ...     print(naija.religion())
                ...
                Humanist
                Christian
                Muslim
        """
        religions = self.religion_provider.get_religions()
        religion = get_unique_value(religions, self._used_religions)
        self._used_religions.add(religion)
        return religion
