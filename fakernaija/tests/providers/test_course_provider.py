"""Unit tests for the CourseProvider class."""

import unittest

from fakernaija.providers.course_provider import CourseProvider


class TestCourseProvider(unittest.TestCase):
    """Test suite for the CourseProvider class."""

    def setUp(self) -> None:
        """Set up the CourseProvider instance for testing."""
        self.course_provider = CourseProvider()

    def test_get_courses(self) -> None:
        """Test getting a list of all course names."""
        courses = self.course_provider.get_courses()
        self.assertIn("Introduction to Computer Science", courses)

    def test_get_course_codes(self) -> None:
        """Test getting a list of all course codes."""
        courses = self.course_provider.get_courses_code()
        self.assertIn("COS101", courses)

    def test_get_course_data(self) -> None:
        """Test getting a list of all courses with their names and codes."""
        courses = self.course_provider.get_course_data()
        self.assertIn(
            {"name": "Introduction to Computer Science", "code": "COS101"},
            courses,
        )
