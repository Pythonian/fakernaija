"""Course mixin to group related methods for the CourseProvider."""

import random

from fakernaija.providers.course_provider import CourseProvider


class Course:
    """Methods for the CourseProvider."""

    def __init__(self) -> None:
        """Initializes the Course mixin and its provider."""
        self.course_provider = CourseProvider()

    def course(self) -> dict[str, str]:
        """Get a random course with its code.

        Returns:
            dict[str, str]: A dictionary with course name and code.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> course = naija.course()
                >>> print(f"Random course: {course}")
                "Random course: {'name': 'Introduction to Computer Science', 'code': 'COS101'}"
        """
        return random.choice(self.course_provider.get_course_data())

    def course_name(self) -> str:
        """Get a random course name.

        Returns:
            str: A random course name.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> course = naija.course_name()
                >>> print(f"Random course: {course}")
                "Random course: Introduction to Computer Science"
        """
        return random.choice(self.course_provider.get_courses())

    def course_code(self) -> str:
        """Get a random course code.

        Returns:
            str: A random course code.

        Example:
            .. code-block:: python

                >>> from fakernaija.faker import Faker
                >>> naija = Faker()

                >>> course = naija.course_code()
                >>> print(f"Random course: {course}")
                "Random course: COS101"
        """
        return random.choice(self.course_provider.get_courses_code())
