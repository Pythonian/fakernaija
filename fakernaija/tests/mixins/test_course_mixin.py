"""Unit tests for the Course mixin methods.

This module contains unit tests for the Course class, which provides methods
to interact with the CourseProvider class for generating course information.
"""

import unittest

from fakernaija.mixins.course_mixin import Course


class TestCourse(unittest.TestCase):
    """Test suite for the Course class."""

    def setUp(self) -> None:
        """Set up the Course instance for testing."""
        self.course = Course()

    def test_course(self) -> None:
        """Test that course returns a dictionary."""
        course = self.course.course()
        self.assertIsInstance(course, dict)

    def test_course_name(self) -> None:
        """Test that course_name returns a string."""
        course = self.course.course_name()
        self.assertIsInstance(course, str)

    def test_course_code(self) -> None:
        """Test that course_code returns a string."""
        course = self.course.course_code()
        self.assertIsInstance(course, str)
