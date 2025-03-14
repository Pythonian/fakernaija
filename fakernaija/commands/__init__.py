"""Aggregates and exposes subcommands from various command modules."""

from .course import course, course_code, course_name
from .degree import degree, degree_abbr, degree_name
from .email import email
from .faculty import (
    department_name,
    faculty,
    faculty_name,
)
from .license_plate import license_plate
from .marital_status import marital_status
from .name import first_name, full_name, last_name, prefix
from .phonenumber import phone_number
from .religion import religion
from .school import school, school_name
from .state import (
    state,
    state_capital,
    state_lga,
    state_name,
    state_postal_code,
)

__all__ = [
    # Course commands
    "course",
    "course_code",
    "course_name",
    # Degree commands
    "degree",
    "degree_abbr",
    "degree_name",
    "department_name",
    # Email command
    "email",
    # Faculty commands
    "faculty",
    "faculty_name",
    # Name commands
    "first_name",
    "full_name",
    "last_name",
    # License plate command
    "license_plate",
    # Marital status command
    "marital_status",
    # PhoneNumber command
    "phone_number",
    "prefix",
    # Religion command
    "religion",
    # School commands
    "school",
    "school_name",
    # State commands
    "state",
    "state_capital",
    "state_lga",
    "state_name",
    "state_postal_code",
]
