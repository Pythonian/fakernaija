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
        self.provider = DegreeProvider()
        self.all_degrees = self.provider.get_degrees()
        self.all_initials = self.provider.get_degree_initials()

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
        """Test that undergraduate degree returns a full name string."""
        name = self.faker.degree(degree_type="undergraduate")
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_undergraduate_degree_initial(self) -> None:
        """Test that undergraduate degree with initial=True returns an initial string."""
        initial = self.faker.degree(degree_type="undergraduate", initial=True)
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)

    def test_masters_degree(self) -> None:
        """Test that masters degree returns a full name string."""
        name = self.faker.degree(degree_type="masters")
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_masters_degree_initial(self) -> None:
        """Test that masters degree with initial=True returns an initial string."""
        initial = self.faker.degree(initial=True, degree_type="masters")
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)

    def test_doctorate_degree(self) -> None:
        """Test that doctorate degree returns a full name string."""
        name = self.faker.degree(degree_type="doctorate")
        self.assertIsInstance(name, str)
        self.assertIn(name, self.all_degrees)

    def test_doctorate_degree_initial(self) -> None:
        """Test that doctorate degree with initial=True returns an initial string."""
        initial = self.faker.degree(initial=True, degree_type="doctorate")
        self.assertIsInstance(initial, str)
        self.assertIn(initial, self.all_initials)
