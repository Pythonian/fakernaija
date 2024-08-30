"""Unit tests for the MaritalStatus mixin methods.

This module contains unit tests for the MaritalStatus class, which provides methods
to interact with the MaritalStatusProvider class for returning marital status data.
"""

import unittest

from fakernaija.mixins import MaritalStatus


class TestMaritalStatus(unittest.TestCase):
    """Test suite for the MaritalStatus class."""

    def setUp(self) -> None:
        """Set up the MaritalStatus instance for testing."""
        self.marital_status = MaritalStatus()

    def test_marital_status(self) -> None:
        """Test that marital_status returns a string."""
        marital_status = self.marital_status.marital_status()
        self.assertIsInstance(marital_status, str)
