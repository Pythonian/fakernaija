"""Unit tests for the Email mixin methods."""

import unittest
from unittest.mock import patch

from fakernaija.mixins import Email


class TestEmail(unittest.TestCase):
    """Unit tests for the Naija method from the EmailProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.naija = Email()
        self.email_provider_mock = patch.object(
            self.naija,
            "email_provider",
            autospec=True,
        ).start()
        self.addCleanup(patch.stopall)

    def test_email_no_filters(self) -> None:
        """Test generating an email with no tribe, gender, domain, or name filters."""
        self.email_provider_mock.generate_email.return_value = "pythonian@gmail.com"
        result = self.naija.email()
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            None,
            None,
        )
        self.assertEqual(result, "pythonian@gmail.com")

    def test_email_with_tribe_filter(self) -> None:
        """Test generating an email with a tribe filter."""
        self.email_provider_mock.generate_email.return_value = (
            "tribe_pythonian@gmail.com"
        )
        result = self.naija.email(tribe="yoruba")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            None,
            None,
            None,
        )
        self.assertEqual(result, "tribe_pythonian@gmail.com")

    def test_email_with_gender_filter(self) -> None:
        """Test generating an email with a gender filter."""
        self.email_provider_mock.generate_email.return_value = (
            "gender_pythonian@gmail.com"
        )
        result = self.naija.email(gender="male")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "male",
            None,
            None,
        )
        self.assertEqual(result, "gender_pythonian@gmail.com")

    def test_email_with_tribe_and_gender_filters(self) -> None:
        """Test generating an email with both tribe and gender filters."""
        self.email_provider_mock.generate_email.return_value = (
            "tribe_gender_pythonian@gmail.com"
        )
        result = self.naija.email(tribe="yoruba", gender="male")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            "male",
            None,
            None,
        )
        self.assertEqual(result, "tribe_gender_pythonian@gmail.com")

    def test_email_with_domain(self) -> None:
        """Test generating an email with a domain filter."""
        self.email_provider_mock.generate_email.return_value = "test@unn.edu.ng"

        result = self.naija.email(domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            "unn.edu.ng",
            None,
        )
        self.assertEqual(result, "test@unn.edu.ng")

    def test_email_with_tribe_and_domain(self) -> None:
        """Test generating an email with tribe and domain filters."""
        self.email_provider_mock.generate_email.return_value = "tribe_test@unn.edu.ng"

        result = self.naija.email(tribe="yoruba", domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            None,
            "unn.edu.ng",
            None,
        )
        self.assertEqual(result, "tribe_test@unn.edu.ng")

    def test_email_with_gender_and_domain(self) -> None:
        """Test generating an email with gender and domain filters."""
        self.email_provider_mock.generate_email.return_value = "gender_test@unn.edu.ng"

        result = self.naija.email(gender="male", domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "male",
            "unn.edu.ng",
            None,
        )
        self.assertEqual(result, "gender_test@unn.edu.ng")

    def test_email_with_all_filters(self) -> None:
        """Test generating an email with tribe, gender, domain, and name filters."""
        self.email_provider_mock.generate_email.return_value = (
            "tribe_gender_test@unn.edu.ng"
        )

        result = self.naija.email(
            tribe="yoruba",
            gender="male",
            domain="unn.edu.ng",
        )
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            "male",
            "unn.edu.ng",
            None,
        )
        self.assertEqual(result, "tribe_gender_test@unn.edu.ng")

    def test_email_with_invalid_tribe(self) -> None:
        """Test generating an email with an invalid tribe."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.naija.email(tribe="invalid_tribe")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "invalid_tribe",
            None,
            None,
            None,
        )
        self.assertIsNone(result)

    def test_email_with_invalid_gender(self) -> None:
        """Test generating an email with an invalid gender."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.naija.email(gender="invalid_gender")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "invalid_gender",
            None,
            None,
        )
        self.assertIsNone(result)

    def test_email_with_invalid_domain(self) -> None:
        """Test generating an email with an invalid domain."""
        self.email_provider_mock.generate_email.return_value = None

        result = self.naija.email(domain="invalid_domain")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            "invalid_domain",
            None,
        )
        self.assertIsNone(result)

    def test_email_with_invalid_tribe_and_gender(self) -> None:
        """Test generating an email with invalid tribe and gender."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.naija.email(tribe="invalid_tribe", gender="invalid_gender")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "invalid_tribe",
            "invalid_gender",
            None,
            None,
        )
        self.assertIsNone(result)

    def test_email_with_name(self) -> None:
        """Test generating an email with a name filter."""
        self.email_provider_mock.generate_email.return_value = "seyi01@gmail.com"

        result = self.naija.email(name="Seyi")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            None,
            "Seyi",
        )
        self.assertEqual(result, "seyi01@gmail.com")

    def test_email_with_fullname_and_domain(self) -> None:
        """Test generating an email with a full name and domain filter."""
        self.email_provider_mock.generate_email.return_value = "pythonian.seyi23@edu.ng"

        result = self.naija.email(name="Seyi Pythonian", domain="edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            "edu.ng",
            "Seyi Pythonian",
        )
        self.assertEqual(result, "pythonian.seyi23@edu.ng")

    def test_email_with_name_and_all_filters(self) -> None:
        """Test generating an email with tribe, gender, domain, and name filters."""
        self.email_provider_mock.generate_email.return_value = (
            "pythonian.seyi@unn.edu.ng"
        )

        result = self.naija.email(
            tribe="yoruba",
            gender="male",
            domain="unn.edu.ng",
            name="Seyi Pythonian",
        )
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            "male",
            "unn.edu.ng",
            "Seyi Pythonian",
        )
        self.assertEqual(result, "pythonian.seyi@unn.edu.ng")
