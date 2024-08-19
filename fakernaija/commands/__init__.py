from .course import course, course_code, course_name
from .currency import currency, currency_code, currency_name, currency_symbol
from .degree import degree, degree_abbr, degree_name
from .email import email
from .faculty import department_by_faculty, department_name, faculty, faculty_name
from .name import firstname, fullname, lastname, prefix
from .phonenumber import phonenumber
from .school import school, school_name
from .state import (
    state,
    state_capital,
    state_lga,
    state_name,
    state_postal_code,
)

__all__ = [
    "course",
    "course_code",
    "course_name",
    "currency",
    "currency_code",
    "currency_name",
    "currency_symbol",
    "degree",
    "degree_abbr",
    "degree_name",
    "email",
    "faculty",
    "faculty_name",
    "department_name",
    "department_by_faculty",
    "firstname",
    "fullname",
    "prefix",
    "lastname",
    "phonenumber",
    "school",
    "school_name",
    "lga",
    "postal_code",
    "region",
    "region_abbr",
    "region_name",
    "state",
    "state_capital",
    "state_code",
    "state_lga",
    "state_name",
    "state_postal_code",
    "state_region",
    "state_slogan",
]
