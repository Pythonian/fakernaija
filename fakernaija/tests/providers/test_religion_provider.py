"""Unit tests for the ReligionProvider class."""

import unittest

from fakernaija.providers import ReligionProvider


class TestReligionProvider(unittest.TestCase):
    """Test suite for the ReligionProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment by initializing a ReligionProvider instance."""
        self.religion_provider = ReligionProvider()

    def test_get_religions(self) -> None:
        """Test getting all religions."""
        expected_religions = [
            "Christian",
            "Muslim",
            "Traditionalist",
            "Atheist",
            "Secularist",
            "Humanist",
            "Judaist",
        ]
        religions = self.religion_provider.get_religions()
        self.assertEqual(religions, expected_religions)
