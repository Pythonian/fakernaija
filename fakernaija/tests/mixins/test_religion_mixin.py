"""Unit tests for the Religion mixin methods.

This module contains unit tests for the Religion class, which provides methods
to interact with the ReligionProvider class for returning religion data.
"""

import unittest

from fakernaija.mixins import Religion


class TestReligion(unittest.TestCase):
    """Test suite for the Religion class."""

    def setUp(self) -> None:
        """Set up the Religion instance for testing."""
        self.religion = Religion()

    def test_religion(self) -> None:
        """Test that religion returns a string."""
        religion = self.religion.religion()
        self.assertIsInstance(religion, str)
