"""This module provides a `Faker` class that generates random Nigerian data."""

from fakernaija.mixins import (
    Course,
    Currency,
    Degree,
    Email,
    Faculty,
    Name,
    PhoneNumber,
    School,
    State,
)


class Faker(
    Course,
    Currency,
    Degree,
    Email,
    Faculty,
    Name,
    PhoneNumber,
    School,
    State,
):
    """This is the primary interface for generating various types of data.

    This class aggregates various mixins, each providing methods
    to generate specific types of data.
    """

    def __init__(self) -> None:
        """Initializes the Faker class and its inherited mixins."""
        Course.__init__(self)
        Currency.__init__(self)
        Degree.__init__(self)
        Email.__init__(self)
        Faculty.__init__(self)
        Name.__init__(self)
        PhoneNumber.__init__(self)
        School.__init__(self)
        State.__init__(self)
