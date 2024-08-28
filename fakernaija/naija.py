"""This module provides a `Naija` class that generates random Nigerian data."""

from fakernaija.mixins import (
    Course,
    Degree,
    Email,
    Faculty,
    MaritalStatus,
    Name,
    PhoneNumber,
    Religion,
    School,
    State,
)


class Naija(
    Course,
    Degree,
    Email,
    Faculty,
    MaritalStatus,
    Name,
    PhoneNumber,
    Religion,
    School,
    State,
):
    """This is the primary interface for generating various types of data.

    This class aggregates various mixins, each providing methods
    to generate specific types of data.
    """

    def __init__(self) -> None:
        """Initializes the Naija class and its inherited mixins."""
        Course.__init__(self)
        Degree.__init__(self)
        Email.__init__(self)
        Faculty.__init__(self)
        MaritalStatus.__init__(self)
        Name.__init__(self)
        PhoneNumber.__init__(self)
        Religion.__init__(self)
        School.__init__(self)
        State.__init__(self)
