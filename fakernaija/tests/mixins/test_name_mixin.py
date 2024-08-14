"""Unit tests for the Name mixin methods.

This module contains unit tests for the Name class, which provides methods
to interact with the NameProvider class for generating different Name combinations.
"""

import unittest

from fakernaija.mixins import Name


class TestName(unittest.TestCase):
    """Test suite for the Name mixin class."""

    def setUp(self) -> None:
        """Set up the Name instance for testing."""
        self.name_mixin = Name()

    def test_full_name(self) -> None:
        """Test that full_name returns a string."""
        name = self.name_mixin.full_name()
        self.assertIsInstance(name, str)

    def test_full_name_with_middle_name(self) -> None:
        """Test that full_name with middle_name returns a string and that first and middle names are not the same."""
        name = self.name_mixin.full_name(middle_name=True)
        self.assertIsInstance(name, str)
        parts = name.split()
        self.assertNotEqual(parts[0], parts[1])

    def test_male_full_name(self) -> None:
        """Test that male_full_name returns a string."""
        name = self.name_mixin.male_full_name()
        self.assertIsInstance(name, str)

    def test_female_full_name(self) -> None:
        """Test that female_full_name returns a string."""
        name = self.name_mixin.female_full_name()
        self.assertIsInstance(name, str)

    def test_full_name_tribe(self) -> None:
        """Test that full_name_tribe returns a string."""
        name = self.name_mixin.full_name_tribe("yoruba")
        self.assertIsInstance(name, str)

    def test_first_name(self) -> None:
        """Test that first_name returns a string."""
        name = self.name_mixin.first_name()
        self.assertIsInstance(name, str)

    def test_first_name_tribe(self) -> None:
        """Test that first_name_tribe returns a string."""
        name = self.name_mixin.first_name_tribe("hausa")
        self.assertIsInstance(name, str)

    def test_male_first_name(self) -> None:
        """Test that male_first_name returns a string."""
        name = self.name_mixin.male_first_name()
        self.assertIsInstance(name, str)

    def test_female_first_name(self) -> None:
        """Test that female_first_name returns a string."""
        name = self.name_mixin.female_first_name()
        self.assertIsInstance(name, str)

    def test_male_first_name_tribe(self) -> None:
        """Test that male_first_name_tribe returns a string."""
        name = self.name_mixin.male_first_name_tribe("igbo")
        self.assertIsInstance(name, str)

    def test_female_first_name_tribe(self) -> None:
        """Test that female_first_name_tribe returns a string."""
        name = self.name_mixin.female_first_name_tribe("ijaw")
        self.assertIsInstance(name, str)

    def test_last_name(self) -> None:
        """Test that last_name returns a string."""
        name = self.name_mixin.last_name()
        self.assertIsInstance(name, str)

    def test_last_name_tribe(self) -> None:
        """Test that last_name_tribe returns a string."""
        name = self.name_mixin.last_name_tribe("edo")
        self.assertIsInstance(name, str)

    def test_prefix(self) -> None:
        """Test that prefix returns a string."""
        prefix = self.name_mixin.prefix()
        self.assertIsInstance(prefix, str)

    def test_male_prefix(self) -> None:
        """Test that male_prefix returns a string."""
        prefix = self.name_mixin.male_prefix()
        self.assertIsInstance(prefix, str)

    def test_female_prefix(self) -> None:
        """Test that female_prefix returns a string."""
        prefix = self.name_mixin.female_prefix()
        self.assertIsInstance(prefix, str)

    def test_traditional_male_title(self) -> None:
        """Test that traditional_male_title returns a string."""
        title = self.name_mixin.traditional_male_title()
        self.assertIsInstance(title, str)

    def test_traditional_female_title(self) -> None:
        """Test that traditional_female_title returns a string."""
        title = self.name_mixin.traditional_female_title()
        self.assertIsInstance(title, str)

    def test_professional_title(self) -> None:
        """Test that professional_title returns a string."""
        title = self.name_mixin.professional_title()
        self.assertIsInstance(title, str)
