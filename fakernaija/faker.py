"""This module provides a `Faker` class that generates random Nigerian data."""

from fakernaija.mixins.course_mixin import Course
from fakernaija.mixins.degree_mixin import Degree
from fakernaija.mixins.email_mixin import Email
from fakernaija.mixins.faculty_mixin import Faculty
from fakernaija.mixins.name_mixin import Name
from fakernaija.mixins.phonenumber_mixin import PhoneNumber
from fakernaija.mixins.school_mixin import School
from fakernaija.mixins.state_mixin import State


class Faker(
    Course,
    Degree,
    Email,
    Faculty,
    Name,
    PhoneNumber,
    School,
    State,
):
    """A class for generating fake data exposed by different Providers."""

    def __init__(self) -> None:
        """Initializes the Faker class and its mixins."""
        Course.__init__(self)
        Degree.__init__(self)
        Email.__init__(self)
        Faculty.__init__(self)
        Name.__init__(self)
        PhoneNumber.__init__(self)
        School.__init__(self)
        State.__init__(self)
