"""Unit tests for the MaritalStatusProvider class."""

import unittest

from fakernaija.providers import MaritalStatusProvider


class TestMaritalStatusProvider(unittest.TestCase):
    """Test suite for the MaritalStatusProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment by initializing a MaritalStatusProvider instance."""
        self.marital_status_provider = MaritalStatusProvider()

    def test_get_marital_statuses(self) -> None:
        """Test getting all marital statuses."""
        expected_statuses = [
            "Annulled",
            "Divorced",
            "Engaged",
            "Married",
            "Separated",
            "Single",
            "Widowed",
        ]
        statuses = self.marital_status_provider.get_marital_statuses()
        self.assertEqual(statuses, expected_statuses)
