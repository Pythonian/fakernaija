"""Course mixin to group related methods for the CourseProvider."""

import random

from fakernaija.providers.course_provider import CourseProvider


class Course:
    """Methods for the CourseProvider."""

    def __init__(self) -> None:
        """Initializes the Course mixin and its provider."""
        self.course_provider = CourseProvider()
        self._used_courses: set[str] = set()

    def course(self, code: bool = False) -> str:
        """Get a random course.

        Args:
            code (bool): If True, returns the course code instead of the name. Defaults to False.

        Returns:
            str: A random course or course code.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> course = naija.course()
                >>> print(f"Random course: {course}")
                'Random course: Introduction to Computer Science'

                >>> course_code = naija.course(code=True)
                >>> print(f"Random course code: {course_code}")
                'Random course code: STA131'
        """
        courses = (
            self.course_provider.get_courses_code()
            if code
            else self.course_provider.get_courses()
        )
        course = self._get_unique_value(courses, self._used_courses)
        self._used_courses.add(course)
        return course

    def _get_unique_value(self, values: list[str], used_values: set[str]) -> str:
        """Helper method to get a unique value from a list of values.

        Args:
            values (list[str]): The list of possible values.
            used_values (set[str]): The set of values that have already been used.

        Returns:
            str: A unique value from the list.
        """
        available_values = set(values) - used_values
        if not available_values:
            # If all values have been used, reset the used values set
            used_values.clear()
            available_values = set(values)
        return random.choice(list(available_values))
