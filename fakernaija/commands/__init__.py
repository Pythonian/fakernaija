"""Aggregates and exposes subcommands from various command modules."""

from .course import course, course_code, course_name
from .currency import currency, currency_code, currency_name, currency_symbol
from .degree import degree, degree_abbr, degree_name
from .email import email
from .faculty import (
    department_name,
    faculty,
    faculty_name,
)
from .name import first_name, full_name, last_name, prefix
from .phonenumber import phone_number
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
    # Currency commands
    "currency",
    "currency_code",
    "currency_name",
    "currency_symbol",
    # Degree commands
    "degree",
    "degree_abbr",
    "degree_name",
    # Email command
    "email",
    # Faculty commands
    "faculty",
    "faculty_name",
    "department_name",
    # Name commands
    "first_name",
    "full_name",
    "last_name",
    "prefix",
    # PhoneNumber command
    "phone_number",
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
