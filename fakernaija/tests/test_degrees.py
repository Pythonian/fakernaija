"""Unit tests for the Degree mixin methods from the DegreeProvider.

This module contains a set of unit tests to verify the behavior of the Degree mixin methods from the DegreeProvider.
The tests ensure that the methods return valid degree names and initials as expected.
"""

import unittest

from fakernaija.faker import Faker
from fakernaija.providers.degree_provider import DegreeProvider


class TestDegreeMixin(unittest.TestCase):
    """Unit tests for the Degree methods from the Degree mixins."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()
        self.degree_provider = DegreeProvider()
        self.all_degrees = self.degree_provider.get_degrees()
        self.all_initials = self.degree_provider.get_degree_initials()

    def test_degree(self) -> None:
        """Test that degree returns a full name string."""
        name = self.faker.degree()
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_degree_initial(self) -> None:
        """Test that degree with initial=True returns an initial string."""
        initial = self.faker.degree(initial=True)
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)

    def test_undergraduate_degree(self) -> None:
        """Test that undergraduate_degree returns a full name string."""
        name = self.faker.undergraduate_degree()
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_undergraduate_degree_initial(self) -> None:
        """Test that undergraduate_degree with initial=True returns an initial string."""
        initial = self.faker.undergraduate_degree(initial=True)
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)

    def test_masters_degree(self) -> None:
        """Test that masters_degree returns a full name string."""
        name = self.faker.masters_degree()
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_masters_degree_initial(self) -> None:
        """Test that masters_degree with initial=True returns an initial string."""
        initial = self.faker.masters_degree(initial=True)
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)

    def test_doctorate_degree(self) -> None:
        """Test that doctorate_degree returns a full name string."""
        name = self.faker.doctorate_degree()
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_doctorate_degree_initial(self) -> None:
        """Test that doctorate_degree with initial=True returns an initial string."""
        initial = self.faker.doctorate_degree(initial=True)
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)
