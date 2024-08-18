"""Course mixin to group related methods for the CourseProvider."""

import random

from fakernaija.providers import CourseProvider
from fakernaija.utils import get_unique_value


class Course:
    """A mixin providing methods to generate course-related data.

    This mixin utilizes the `CourseProvider` class and provides the
    functionality for fetching and returning course-related data.
    """

    def __init__(self) -> None:
        """Initializes the Course mixin and its provider."""
        self.course_provider = CourseProvider()
        self._used_course_names: set[str] = set()
        self._used_course_codes: set[str] = set()

    def course(self) -> dict[str, str]:
        """Get a random course object.

        Returns:
            dict[str, str]: A dictionary with course name and code.

        Example:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> course = naija.course()
                >>> print(f"Random course: {course}")
                Random course: {'name': 'Introduction to Computer Science', 'code': 'COS101'}
        """
        return random.choice(self.course_provider.get_courses())

    def course_name(self) -> str:
        """Get a random course name.

        Returns:
            str: A random course name.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> course_name = naija.course_name()
                >>> print(f"Random course name: {course_name}")
                Random course name: Introduction to Computer Science

                >>> for _ in range(3):
                ...     print(naija.course_name())
                ...
                Solar Energy II
                Chemical Process Technology III
                Analytical Mechanics
        """
        course_names = self.course_provider.get_courses_name()
        course_name = get_unique_value(course_names, self._used_course_names)
        self._used_course_names.add(course_name)
        return course_name

    def course_code(self) -> str:
        """Get a random course code.

        Returns:
            str: A random course code.

        Examples:
            .. code-block:: python

                >>> from fakernaija import Faker
                >>> naija = Faker()

                >>> course = naija.course_code()
                >>> print(f"Random course: {course}")
                Random course: COS101

                >>> for _ in range(3):
                ...     print(naija.course_code())
                ...
                STA212
                COS452
                MTH421
        """
        course_codes = self.course_provider.get_courses_code()
        course_code = get_unique_value(course_codes, self._used_course_codes)
        self._used_course_codes.add(course_code)
        return course_code
