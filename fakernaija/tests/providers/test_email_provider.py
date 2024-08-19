"""Unit tests for the EmailProvider class."""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.providers import EmailProvider
from fakernaija.providers.name_provider import NameProvider


class TestEmailProvider(unittest.TestCase):
    """Test suite for the EmailProvider class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.email_provider = EmailProvider()
        self.mock_name_provider = MagicMock(spec=NameProvider)
        self.email_provider.name_provider = self.mock_name_provider

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

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_valid(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating a valid email address."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = [{"name": "Ade"}]
        mock_get_last_names.return_value = [{"name": "Ogunleye"}]

        email = self.email_provider.generate_email("yoruba", "male", "example.com")
        self.assertIsNotNone(email)
        self.assertIn("@example.com", email)

    @patch("fakernaija.providers.EmailProvider.validate_domain")
    def test_generate_email_invalid_domain(
        self,
        mock_validate_domain: MagicMock,
    ) -> None:
        """Test generating an email with an invalid domain."""
        mock_validate_domain.return_value = False

        with self.assertRaises(ValueError):
            self.email_provider.generate_email(domain="invalid_domain")

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_with_missing_names(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email when no names are available."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = []
        mock_get_last_names.return_value = []

        with self.assertRaises(ValueError):
            self.email_provider.generate_email("yoruba", "male", "example.com")

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_random_domain(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email with a random domain."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = [{"name": "Ade"}]
        mock_get_last_names.return_value = [{"name": "Ogunleye"}]

        email = self.email_provider.generate_email("yoruba", "male")
        self.assertIsNotNone(email)
        self.assertTrue(
            any(
                email.endswith(f"@{domain}")
                for domain in self.email_provider.default_domains
            ),
        )

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_random_tribe(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email with a random tribe."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.side_effect = (
            lambda tribe, _: [{"name": "Ade"}]
            if tribe == "yoruba"
            else [{"name": "Ugochi"}]
        )
        mock_get_last_names.side_effect = (
            lambda tribe: [{"name": "Ogunleye"}]
            if tribe == "yoruba"
            else [{"name": "Okafor"}]
        )

        email = self.email_provider.generate_email()
        self.assertIsNotNone(email)

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_with_suffix(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email with a random number suffix."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = [{"name": "Ade"}]
        mock_get_last_names.return_value = [{"name": "Ogunleye"}]

        # Patch random.random to return a value less than 0.5 to ensure suffix is added
        with patch("random.random", return_value=0.4):
            email = self.email_provider.generate_email("yoruba", "male", "example.com")
            self.assertIsNotNone(email)
            self.assertRegex(email, r"[a-zA-Z]+[.]?[a-zA-Z]*[0-9]+@example\.com")

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_without_suffix(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email without a random number suffix."""
        mock_validate_email.return_value = True
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = [{"name": "Ade"}]
        mock_get_last_names.return_value = [{"name": "Ogunleye"}]

        # Patch random.random to return a value greater than 0.5 to ensure no suffix is added
        with patch("random.random", return_value=0.6):
            email = self.email_provider.generate_email("yoruba", "male", "example.com")
            self.assertIsNotNone(email)
            self.assertNotRegex(email, r"[0-9]+@example\.com")

    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_first_names",
    )
    @patch(
        "fakernaija.providers.name_provider.NameProvider.get_last_names",
    )
    @patch("fakernaija.providers.EmailProvider.validate_domain")
    @patch("fakernaija.providers.EmailProvider.validate_email")
    def test_generate_email_invalid_email(
        self,
        mock_validate_email: MagicMock,
        mock_validate_domain: MagicMock,
        mock_get_last_names: MagicMock,
        mock_get_first_names: MagicMock,
    ) -> None:
        """Test generating an email when the email validation fails."""
        mock_validate_email.return_value = False
        mock_validate_domain.return_value = True
        mock_get_first_names.return_value = [{"name": "Ade"}]
        mock_get_last_names.return_value = [{"name": "Ogunleye"}]

        with self.assertRaises(ValueError):
            self.email_provider.generate_email("yoruba", "male", "example.com")
