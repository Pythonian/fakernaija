"""CourseMixin to group related methods for the CourseProvider."""

import random

from fakernaija.providers.courses import CourseProvider


class Course:
    """Methods for the CourseProvider."""

    def __init__(self) -> None:
        """Initializes the Course mixin and its provider."""
        self.course_provider = CourseProvider()

    def course(self) -> str:
        """Generates a random course.

        Returns:
            str: A random course.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> course = naija.course()
                >>> print(f"Random course: {course}")
                'Random course: Modern Art History'
        """
        courses = self.course_provider.get_courses()
        return random.choice(courses)
