"""Unit tests for the EmailProvider class.

This module contains unit tests for the EmailProvider class, which provides methods
for generating random email address with Nigerian names. The tests ensure that the
methods return the expected names based on tribes and given domains.
"""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers.emails import EmailProvider
from fakernaija.providers.names import NameProvider


class TestEmailProvider(unittest.TestCase):
    """Unit tests for the EmailProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()
        self.mock_name_provider = MagicMock(spec=NameProvider)
        self.email_provider.name_provider = self.mock_name_provider

    def test_get_first_names_with_filters(self) -> None:
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

    def test_get_first_names_no_filters(self) -> None:
        """Test get_first_names method with no filters."""
        mock_first_names = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.mock_name_provider.get_first_names.return_value = mock_first_names

        result = self.email_provider.get_first_names()
        self.mock_name_provider.get_first_names.assert_called_once_with(
            None,
            None,
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

    def test_get_first_names_with_tribe_and_gender_filter(self) -> None:
        """Test get_first_names with both tribe and gender filters applied."""
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


class TestGenerateEmailMethod(unittest.TestCase):
    """Unit tests for the generate_email method of the EmailProvider class."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.email_provider = EmailProvider()

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_valid(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating a valid email address."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = (["Ade"], ["Ogunleye"])

        email = self.email_provider.generate_email("yoruba", "male", "example.com")
        self.assertIsNotNone(email)
        if email is not None:
            self.assertIn("@example.com", email)

    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    def test_generate_email_invalid_domain(
        self,
        mock_validate_domain: MagicMock,
    ) -> None:
        """Test generating an email with an invalid domain."""
        mock_validate_domain.return_value = False

        email = self.email_provider.generate_email(domain="invalid_domain")
        self.assertIsNone(email)

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_with_missing_names(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email when no names are available."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = ([], [])

        email = self.email_provider.generate_email("yoruba", "male", "example.com")
        self.assertIsNone(email)

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_random_domain(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email with a random domain."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = (["Ade"], ["Ogunleye"])

        email = self.email_provider.generate_email("yoruba", "male")
        self.assertIsNotNone(email)
        if email is not None:
            self.assertTrue(
                any(
                    email.endswith(f"@{domain}")
                    for domain in self.email_provider.default_domains
                ),
            )

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_random_tribe(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email with a random tribe."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.side_effect = lambda tribe, _: (
            ["Ade"] if tribe == "yoruba" else ["Ugochi"],
            ["Ogunleye"] if tribe == "yoruba" else ["Okafor"],
        )

        email = self.email_provider.generate_email()
        self.assertIsNotNone(email)

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_with_suffix(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email with a random number suffix."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = (["Ade"], ["Ogunleye"])

        # Patch random.random to return a value less than 0.5 to ensure suffix is added
        with patch("random.random", return_value=0.4):
            email = self.email_provider.generate_email("yoruba", "male", "example.com")
            self.assertIsNotNone(email)
            if email is not None:
                self.assertRegex(email, r"[a-zA-Z]+[.]?[a-zA-Z]*[0-9]+@example\.com")

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_without_suffix(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email without a random number suffix."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = (["Ade"], ["Ogunleye"])

        # Patch random.random to return a value greater than 0.5 to ensure no suffix is added
        with patch("random.random", return_value=0.6):
            email = self.email_provider.generate_email("yoruba", "male", "example.com")
            self.assertIsNotNone(email)
            if email is not None:
                self.assertNotRegex(email, r"[0-9]+@example\.com")

    @patch("fakernaija.providers.emails.EmailProvider.get_names_by_tribe")
    @patch("fakernaija.providers.emails.EmailProvider.validate_domain")
    @patch("fakernaija.providers.emails.EmailProvider.validate_email")
    def test_generate_email_invalid_email(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_names_by_tribe: MagicMock,
    ) -> None:
        """Test generating an email when the email validation fails."""
        mock_validate_email.return_value = False
        mock_validate_domain.return_value = True
        mock_get_names_by_tribe.return_value = (["Ade"], ["Ogunleye"])

        email = self.email_provider.generate_email("yoruba", "male", "example.com")
        self.assertIsNone(email)
