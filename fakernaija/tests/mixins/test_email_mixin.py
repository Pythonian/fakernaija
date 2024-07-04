"""Unit tests for the Email mixin methods."""

import unittest
from unittest.mock import patch

from fakernaija.mixins.email_mixin import Email


class TestEmail(unittest.TestCase):
    """Unit tests for the Faker method from the EmailProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Email()
        self.email_provider_mock = patch.object(
            self.faker,
            "email_provider",
            autospec=True,
        ).start()
        self.addCleanup(patch.stopall)

    def test_email_no_filters(self) -> None:
        """Test generating an email with no tribe or gender or domain filters."""
        self.email_provider_mock.generate_email.return_value = "pythonian@gmail.com"
        result = self.faker.email()
        self.email_provider_mock.generate_email.assert_called_once_with(
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
        result = self.faker.email(tribe="yoruba")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            None,
            None,
        )
        self.assertEqual(result, "tribe_pythonian@gmail.com")

    def test_email_with_gender_filter(self) -> None:
        """Test generating an email with a gender filter."""
        self.email_provider_mock.generate_email.return_value = (
            "gender_pythonian@gmail.com"
        )
        result = self.faker.email(gender="male")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "male",
            None,
        )
        self.assertEqual(result, "gender_pythonian@gmail.com")

    def test_email_with_tribe_and_gender_filters(self) -> None:
        """Test generating an email with both tribe and gender filters."""
        self.email_provider_mock.generate_email.return_value = (
            "tribe_gender_pythonian@gmail.com"
        )
        result = self.faker.email(tribe="yoruba", gender="male")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            "male",
            None,
        )
        self.assertEqual(result, "tribe_gender_pythonian@gmail.com")

    def test_email_with_invalid_tribe(self) -> None:
        """Test generating an email with an invalid tribe."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.faker.email(tribe="invalid_tribe")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "invalid_tribe",
            None,
            None,
        )
        self.assertIsNone(result)

    def test_email_with_invalid_gender(self) -> None:
        """Test generating an email with an invalid gender."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.faker.email(gender="invalid_gender")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "invalid_gender",
            None,
        )
        self.assertIsNone(result)

    def test_email_with_invalid_tribe_and_gender(self) -> None:
        """Test generating an email with invalid tribe and gender."""
        self.email_provider_mock.generate_email.return_value = None
        result = self.faker.email(tribe="invalid_tribe", gender="invalid_gender")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "invalid_tribe",
            "invalid_gender",
            None,
        )
        self.assertIsNone(result)

    def test_email_with_domain(self) -> None:
        """Test generating an email with a domain filter."""
        self.email_provider_mock.generate_email.return_value = "test@unn.edu.ng"

        result = self.faker.email(domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            "unn.edu.ng",
        )
        self.assertEqual(result, "test@unn.edu.ng")

    def test_email_with_tribe_and_domain(self) -> None:
        """Test generating an email with tribe and domain filters."""
        self.email_provider_mock.generate_email.return_value = "tribe_test@unn.edu.ng"

        result = self.faker.email(tribe="yoruba", domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            None,
            "unn.edu.ng",
        )
        self.assertEqual(result, "tribe_test@unn.edu.ng")

    def test_email_with_gender_and_domain(self) -> None:
        """Test generating an email with gender and domain filters."""
        self.email_provider_mock.generate_email.return_value = "gender_test@unn.edu.ng"

        result = self.faker.email(gender="male", domain="unn.edu.ng")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            "male",
            "unn.edu.ng",
        )
        self.assertEqual(result, "gender_test@unn.edu.ng")

    def test_email_with_all_filters(self) -> None:
        """Test generating an email with tribe, gender, and domain filters."""
        self.email_provider_mock.generate_email.return_value = (
            "tribe_gender_test@unn.edu.ng"
        )

        result = self.faker.email(
            tribe="yoruba",
            gender="male",
            domain="unn.edu.ng",
        )
        self.email_provider_mock.generate_email.assert_called_once_with(
            "yoruba",
            "male",
            "unn.edu.ng",
        )
        self.assertEqual(result, "tribe_gender_test@unn.edu.ng")

    def test_email_with_invalid_domain(self) -> None:
        """Test generating an email with an invalid domain."""
        self.email_provider_mock.generate_email.return_value = None

        result = self.faker.email(domain="invalid_domain")
        self.email_provider_mock.generate_email.assert_called_once_with(
            None,
            None,
            "invalid_domain",
        )
        self.assertIsNone(result)

    def test_email_by_tribe(self) -> None:
        """Test generating an email with tribe filter using email_by_tribe."""
        self.email_provider_mock.generate_email.return_value = "tribe_test@gmail.com"

        result = self.faker.email_by_tribe("yoruba")
        self.email_provider_mock.generate_email.assert_called_once_with(
            tribe="yoruba",
        )
        self.assertEqual(result, "tribe_test@gmail.com")

    def test_email_by_gender(self) -> None:
        """Test generating an email with gender filter using email_by_gender."""
        self.email_provider_mock.generate_email.return_value = "gender_test@gmail.com"

        result = self.faker.email_by_gender("female")
        self.email_provider_mock.generate_email.assert_called_once_with(
            gender="female",
        )
        self.assertEqual(result, "gender_test@gmail.com")

    def test_email_by_domain(self) -> None:
        """Test generating an email with domain filter using email_by_domain."""
        self.email_provider_mock.generate_email.return_value = "test@domain.com"

        result = self.faker.email_by_domain("domain.com")
        self.email_provider_mock.generate_email.assert_called_once_with(
            domain="domain.com",
        )
        self.assertEqual(result, "test@domain.com")
