"""This module provides a `Faker` class that generates random Nigerian data."""

from fakernaija.mixins import Course
from fakernaija.mixins.currency_mixin import Currency
from fakernaija.mixins.degree_mixin import Degree
from fakernaija.mixins.email_mixin import Email
from fakernaija.mixins.faculty_mixin import Faculty
from fakernaija.mixins.name_mixin import Name
from fakernaija.mixins.phonenumber_mixin import PhoneNumber
from fakernaija.mixins.school_mixin import School
from fakernaija.mixins.state_mixin import State


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
        """Initializes the Faker class and its mixins."""
        Course.__init__(self)
        Currency.__init__(self)
        Degree.__init__(self)
        Email.__init__(self)
        Faculty.__init__(self)
        Name.__init__(self)
        PhoneNumber.__init__(self)
        School.__init__(self)
        State.__init__(self)
