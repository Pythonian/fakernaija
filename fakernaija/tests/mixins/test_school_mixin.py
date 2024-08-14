"""Unit tests for the School mixin methods."""

import unittest
from unittest.mock import patch

from fakernaija.mixins import School
from fakernaija.providers.school_provider import SchoolProvider


class TestSchool(unittest.TestCase):
    """Test suite for the School mixin class."""

    def setUp(self) -> None:
        """Set up the School mixin for testing."""
        self.school_mixin = School()
        self.school_provider_mock = patch.object(
            SchoolProvider,
            "get_schools",
        ).start()
        self.school_name_provider_mock = patch.object(
            SchoolProvider,
            "get_school_names",
        ).start()

    def tearDown(self) -> None:
        """Stop all patches."""
        patch.stopall()

    def test_school_no_filters(self) -> None:
        """Test that a random school is returned with no applied filters."""
        self.school_provider_mock.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "state": "Lagos",
                "type": "university",
                "ownership": "Federal",
            },
            {
                "name": "Ahmadu Bello University",
                "acronym": "ABU",
                "state": "Kaduna",
                "type": "university",
                "ownership": "Federal",
            },
        ]

        school = self.school_mixin.school()
        self.assertIn(school, self.school_provider_mock.return_value)

    def test_school_with_filters(self) -> None:
        """Test that a school is correctly filtered by ownership, state, and school type."""
        self.school_provider_mock.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "state": "Lagos",
                "type": "university",
                "ownership": "Federal",
            },
        ]

        school = self.school_mixin.school(
            ownership="Federal",
            state="Lagos",
            school_type="university",
        )
        self.assertEqual(school, self.school_provider_mock.return_value[0])

    def test_school_returns_none_if_no_match(self) -> None:
        """Test that None is returned if no schools match the filters."""
        self.school_provider_mock.return_value = []
        school = self.school_mixin.school(ownership="Private")
        self.assertIsNone(school)

    def test_school_name_no_filters(self) -> None:
        """Test that a random school name is returned when no filters are applied."""
        self.school_name_provider_mock.return_value = [
            "University of Lagos",
            "Ahmadu Bello University",
        ]

        school_name = self.school_mixin.school_name()
        self.assertIn(school_name, self.school_name_provider_mock.return_value)

    def test_school_name_with_acronym(self) -> None:
        """Test that a school acronym is returned when acronym=True."""
        self.school_name_provider_mock.return_value = ["UNILAG", "ABU"]

        school_acronym = self.school_mixin.school_name(acronym=True)
        self.assertIn(school_acronym, self.school_name_provider_mock.return_value)

    def test_school_name_with_filters(self) -> None:
        """Test that a school name is correctly filtered by ownership, state, and school type."""
        self.school_name_provider_mock.return_value = ["University of Lagos"]

        school_name = self.school_mixin.school_name(
            ownership="Federal",
            state="Lagos",
            school_type="university",
        )
        self.assertEqual(school_name, self.school_name_provider_mock.return_value[0])

    def test_school_name_returns_none_if_no_match(self) -> None:
        """Test that None is returned if no school names match the filters."""
        self.school_name_provider_mock.return_value = []
        school_name = self.school_mixin.school_name(ownership="Private")
        self.assertIsNone(school_name)

    def test_school_name_unique_in_session(self) -> None:
        """Test that repeated calls to school_name return unique values in a session."""
        self.school_name_provider_mock.return_value = [
            "University of Lagos",
            "Ahmadu Bello University",
        ]

        first_name = self.school_mixin.school_name()
        second_name = self.school_mixin.school_name()

        # Ensure the second name is different if there are multiple options
        if len(self.school_name_provider_mock.return_value) > 1:
            self.assertNotEqual(first_name, second_name)

    def test_school_name_repeats_after_exhaustion(self) -> None:
        """Test that school_name starts repeating after all unique values have been used."""
        self.school_name_provider_mock.return_value = [
            "University of Lagos",
            "Ahmadu Bello University",
        ]

        used_names = set()
        for _ in range(3):  # More iterations than there are unique names
            name = self.school_mixin.school_name()
            used_names.add(name)

        self.assertEqual(len(used_names), 2)  # Should contain all unique names
