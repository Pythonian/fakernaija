"""Unit tests for the EmailProvider class.

This module contains unit tests for the EmailProvider class, which provides methods
for generating random email address with Nigerian names. The tests ensure that the
methods return the expected names based on tribes and given domains.
"""

import unittest
from unittest.mock import MagicMock

from fakernaija.providers.emails import EmailProvider
from fakernaija.providers.names import NameProvider


class TestEmailProvider(unittest.TestCase):
    """Unit tests for the EmailProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()
        self.mock_name_provider = MagicMock(spec=NameProvider)
        self.email_provider.name_provider = self.mock_name_provider

    def test_get_first_names(self) -> None:
        """Test get_first_names method with various filters."""
        mock_first_names = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.mock_name_provider.get_first_names.return_value = mock_first_names

        result = self.email_provider.get_first_names(tribe="yoruba", gender="male")
        self.mock_name_provider.get_first_names.assert_called_once_with(
            "yoruba",
            "male",
        )
        self.assertEqual(result, mock_first_names)

    def test_get_last_names(self) -> None:
        """Test get_last_names method with tribe filter."""
        mock_last_names = [
            {"tribe": "yoruba", "name": "Ojo"},
            {"tribe": "igbo", "name": "Maduike"},
        ]
        self.mock_name_provider.get_last_names.return_value = mock_last_names

        result = self.email_provider.get_last_names(tribe="yoruba")
        self.mock_name_provider.get_last_names.assert_called_once_with("yoruba")
        self.assertEqual(result, mock_last_names)

    def test_get_names_by_tribe(self) -> None:
        """Test get_names_by_tribe method with tribe and gender filters."""
        mock_first_names = [{"name": "Ade"}]
        mock_last_names = [{"name": "Ojo"}]
        self.mock_name_provider.get_first_names.return_value = mock_first_names
        self.mock_name_provider.get_last_names.return_value = mock_last_names

        result = self.email_provider.get_names_by_tribe("yoruba", gender="male")
        self.mock_name_provider.get_first_names.assert_called_once_with(
            "yoruba",
            "male",
        )
        self.mock_name_provider.get_last_names.assert_called_once_with("yoruba")
        self.assertEqual(result, (["Ade"], ["Ojo"]))

    def test_validate_domain(self) -> None:
        """Test validate_domain method with valid and invalid domains."""
        valid_domains = [
            "gmail.com",
            "yahoo.com",
            "edu.ng",
            "gov.ng",
            "mail.com",
            "unn.edu.ng",
            "ekiti.lirs.gov.ng",
            "subdomain.example.com",
        ]
        invalid_domains = [
            "invalid@@.co.s",
            "no-tld",
            "two..dots",
            "-invalid.com",
            "invalid-.com",
            "invalid.com-",
            "invalid..com",
            ".invalid.com",
            "invalid.com.",
            "too.many.dots.in.domain",
        ]

        for domain in valid_domains:
            self.assertTrue(self.email_provider.validate_domain(domain))

        for domain in invalid_domains:
            self.assertFalse(self.email_provider.validate_domain(domain))

    def test_validate_email(self) -> None:
        """Test validate_email method with valid and invalid emails."""
        valid_emails = [
            "test@example.com",
            "first.last@example.co.uk",
            "name+tag@domain.org",
        ]
        invalid_emails = ["invalid-email", "missing@domain", "user@.com", "@domain.com"]

        for email in valid_emails:
            self.assertTrue(self.email_provider.validate_email(email))

        for email in invalid_emails:
            self.assertFalse(self.email_provider.validate_email(email))
