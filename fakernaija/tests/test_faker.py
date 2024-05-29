"""Unit tests for the Faker class.

This module contains unit tests for the Faker class, which provides methods
for generating random Nigerian data. The tests ensure that the
methods return the expected types and handle various inputs correctly.
"""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.faker import Faker

PHONE_NUMBER_LENGTH = 11


class TestFaker(unittest.TestCase):
    """Test suite for the Faker class."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()

    def test_full_name(self) -> None:
        """Test that full_name returns a string."""
        name = self.faker.full_name()
        self.assertIsInstance(name, str)

    def test_male_full_name(self) -> None:
        """Test that male_full_name returns a string."""
        name = self.faker.male_full_name()
        self.assertIsInstance(name, str)

    def test_female_full_name(self) -> None:
        """Test that female_full_name returns a string."""
        name = self.faker.female_full_name()
        self.assertIsInstance(name, str)

    def test_first_name(self) -> None:
        """Test that first_name returns a string."""
        name = self.faker.first_name()
        self.assertIsInstance(name, str)

    def test_male_first_name(self) -> None:
        """Test that male_first_name returns a string."""
        name = self.faker.male_first_name()
        self.assertIsInstance(name, str)

    def test_female_first_name(self) -> None:
        """Test that female_first_name returns a string."""
        name = self.faker.female_first_name()
        self.assertIsInstance(name, str)

    def test_last_name(self) -> None:
        """Test that last_name returns a string."""
        name = self.faker.last_name()
        self.assertIsInstance(name, str)

    def test_prefix(self) -> None:
        """Test that prefix returns a string."""
        prefix = self.faker.prefix()
        self.assertIsInstance(prefix, str)

    def test_male_prefix(self) -> None:
        """Test that male_prefix returns a string."""
        prefix = self.faker.male_prefix()
        self.assertIsInstance(prefix, str)

    def test_female_prefix(self) -> None:
        """Test that female_prefix returns a string."""
        prefix = self.faker.female_prefix()
        self.assertIsInstance(prefix, str)

    def test_phone_number(self) -> None:
        """Test that phone_number returns a valid Nigerian phone number."""
        number = self.faker.phone_number()
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)

    def test_phone_number_with_network(self) -> None:
        """Test that phone_number returns a valid phone number for a given network."""
        number = self.faker.phone_number(network="mtn")
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)
        self.assertTrue(
            number.startswith(
                (
                    "0703",
                    "0706",
                    "0803",
                    "0806",
                    "0813",
                    "0816",
                    "0810",
                    "0814",
                    "0903",
                    "0906",
                    "0913",
                    "0916",
                ),
            ),
        )

    def test_phone_number_with_prefix(self) -> None:
        """Test that phone_number returns a valid phone number for a given prefix."""
        number = self.faker.phone_number(prefix="0803")
        self.assertIsInstance(number, str)
        self.assertEqual(len(number), PHONE_NUMBER_LENGTH)
        self.assertTrue(number.startswith("0803"))

    def test_phone_number_with_invalid_prefix(self) -> None:
        """Test that phone_number raises ValueError for an invalid prefix."""
        with self.assertRaises(ValueError):
            self.faker.phone_number(prefix="0999")

    def test_phone_number_with_invalid_network(self) -> None:
        """Test that phone_number raises ValueError for an invalid network."""
        with self.assertRaises(ValueError):
            self.faker.phone_number(network="invalid_network")

    @patch("fakernaija.providers.states.StateProvider.get_states_by_region")
    @patch("random.choice")
    def test_state_with_region_initial(
        self,
        mock_choice: MagicMock,
        mock_get_states_by_region: MagicMock,
    ) -> None:
        """Test state method with region_initial parameter."""
        mock_get_states_by_region.return_value = [
            {"name": "Lagos", "code": "LA"},
            {"name": "Ogun", "code": "OG"},
        ]
        mock_choice.return_value = {"name": "Lagos", "code": "LA"}

        result = self.faker.state(region_initial="SW")
        self.assertEqual(result, "Lagos")

        result = self.faker.state(shortcode=True, region_initial="SW")
        self.assertEqual(result, "LA")

    @patch("fakernaija.providers.states.StateProvider.get_shortcodes")
    @patch("random.choice")
    def test_state_with_shortcode(
        self,
        mock_choice: MagicMock,
        mock_get_shortcodes: MagicMock,
    ) -> None:
        """Test state method with shortcode parameter."""
        mock_get_shortcodes.return_value = ["LA", "OG"]
        mock_choice.return_value = "LA"

        result = self.faker.state(shortcode=True)
        self.assertEqual(result, "LA")

    @patch("fakernaija.providers.states.StateProvider.get_states")
    @patch("random.choice")
    def test_state_without_parameters(
        self,
        mock_choice: MagicMock,
        mock_get_states: MagicMock,
    ) -> None:
        """Test state method without parameters."""
        mock_get_states.return_value = ["Lagos", "Ogun"]
        mock_choice.return_value = "Lagos"

        result = self.faker.state()
        self.assertEqual(result, "Lagos")

    @patch("fakernaija.providers.states.StateProvider.get_state_capital")
    @patch("random.choice")
    def test_capital_with_state(
        self,
        mock_choice: MagicMock,  # noqa: ARG002
        mock_get_state_capital: MagicMock,
    ) -> None:
        """Test capital method with state parameter."""
        mock_get_state_capital.return_value = "Ikeja"

        result = self.faker.capital(state="Lagos")
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.states.StateProvider.get_capitals")
    @patch("random.choice")
    def test_capital_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_capitals: MagicMock,
    ) -> None:
        """Test capital method without state parameter."""
        mock_get_capitals.return_value = ["Ikeja", "Abeokuta"]
        mock_choice.return_value = "Ikeja"

        result = self.faker.capital()
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.states.StateProvider.get_state_lgas")
    @patch("random.choice")
    def test_lga_with_state(
        self,
        mock_choice: MagicMock,
        mock_get_state_lgas: MagicMock,
    ) -> None:
        """Test lga method with state parameter."""
        mock_get_state_lgas.return_value = ["Ikeja", "Epe"]
        mock_choice.return_value = "Ikeja"

        result = self.faker.lga(state="Lagos")
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.states.StateProvider.get_lgas")
    @patch("random.choice")
    def test_lga_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_lgas: MagicMock,
    ) -> None:
        """Test lga method without state parameter."""
        mock_get_lgas.return_value = ["Ikeja", "Epe", "Abeokuta"]
        mock_choice.return_value = "Ikeja"

        result = self.faker.lga()
        self.assertEqual(result, "Ikeja")

    @patch("fakernaija.providers.states.StateProvider.get_regions")
    @patch("random.choice")
    def test_region_with_initial(
        self,
        mock_choice: MagicMock,
        mock_get_regions: MagicMock,
    ) -> None:
        """Test region method with initial parameter."""
        mock_get_regions.return_value = ["South West", "South East"]
        self.faker.state_provider.states_data = {
            "states": [{"region_initial": "SW"}, {"region_initial": "SE"}],
        }
        mock_choice.return_value = "SW"

        result = self.faker.region(initial=True)
        self.assertEqual(result, "SW")

    @patch("fakernaija.providers.states.StateProvider.get_regions")
    @patch("random.choice")
    def test_region_without_initial(
        self,
        mock_choice: MagicMock,
        mock_get_regions: MagicMock,
    ) -> None:
        """Test region method without initial parameter."""
        mock_get_regions.return_value = ["South West", "South East"]
        mock_choice.return_value = "South West"

        result = self.faker.region()
        self.assertEqual(result, "South West")

    @patch("fakernaija.providers.states.StateProvider.get_postal_code_by_state")
    def test_postal_code_with_state(
        self,
        mock_get_postal_code_by_state: MagicMock,
    ) -> None:
        """Test postal code method with state parameter."""
        mock_get_postal_code_by_state.return_value = "100001"

        result = self.faker.postal_code(state="Lagos")
        self.assertEqual(result, "100001")

    @patch("fakernaija.providers.states.StateProvider.get_postal_codes")
    @patch("random.choice")
    def test_postal_code_without_state(
        self,
        mock_choice: MagicMock,
        mock_get_postal_codes: MagicMock,
    ) -> None:
        """Test postal code method without state parameter."""
        mock_get_postal_codes.return_value = ["100001", "110001"]
        mock_choice.return_value = "100001"

        result = self.faker.postal_code()
        self.assertEqual(result, "100001")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    @patch("random.choice")
    def test_school_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test school method with location parameter."""
        mock_get_schools_by_location.return_value = [
            {"name": "University of Lagos", "acronym": "UNILAG"},
            {"name": "Lagos State University", "acronym": "LASU"},
        ]
        mock_choice.return_value = "University of Lagos"

        result = self.faker.school(location="Lagos")
        self.assertEqual(result, "University of Lagos")

        mock_choice.return_value = "UNILAG"
        result = self.faker.school(acronym=True, location="Lagos")
        self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_school_acronyms")
    @patch("random.choice")
    def test_school_with_acronym(
        self,
        mock_choice: MagicMock,
        mock_get_school_acronyms: MagicMock,
    ) -> None:
        """Test school method with acronym parameter."""
        mock_get_school_acronyms.return_value = ["UNILAG", "LASU"]
        mock_choice.return_value = "UNILAG"

        result = self.faker.school(acronym=True)
        self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools")
    @patch("random.choice")
    def test_school_without_acronym_or_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools: MagicMock,
    ) -> None:
        """Test school method without acronym or location parameters."""
        mock_get_schools.return_value = [
            "University of Lagos",
            "Lagos State University",
        ]
        mock_choice.return_value = "University of Lagos"

        result = self.faker.school()
        self.assertEqual(result, "University of Lagos")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    @patch("random.choice")
    def test_federal_school_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test federal_school method with location parameter."""
        mock_get_schools_by_location.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "ownership": "Federal",
            },
            {"name": "Lagos State University", "acronym": "LASU", "ownership": "State"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "University of Lagos"
        with patch.object(
            self.faker.school_provider,
            "get_federal_schools",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.federal_school(location="Lagos")
            self.assertEqual(result, "University of Lagos")

        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_federal_schools",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.federal_school(acronym=True, location="Lagos")
            self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_schools")
    @patch("random.choice")
    def test_federal_school_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_schools: MagicMock,
    ) -> None:
        """Test federal_school method without location parameter."""
        mock_get_federal_schools.return_value = [
            {"name": "University of Lagos"},
            {"name": "University of Ibadan"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "University of Lagos"
        with patch.object(
            self.faker.school_provider,
            "get_federal_schools",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.federal_school()
            self.assertEqual(result, "University of Lagos")

        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_federal_schools",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.federal_school(acronym=True)
            self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    @patch("random.choice")
    def test_state_school_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test state_school method with location parameter."""
        mock_get_schools_by_location.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "ownership": "Federal",
            },
            {"name": "Lagos State University", "acronym": "LASU", "ownership": "State"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_state_schools",
            return_value=[{"name": "Lagos State University", "acronym": "LASU"}],
        ):
            result = self.faker.state_school(location="Lagos")
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_state_schools",
            return_value=[{"name": "Lagos State University", "acronym": "LASU"}],
        ):
            result = self.faker.state_school(acronym=True, location="Lagos")
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_schools")
    @patch("random.choice")
    def test_state_school_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_schools: MagicMock,
    ) -> None:
        """Test state_school method without location parameter."""
        mock_get_state_schools.return_value = [
            {"name": "Lagos State University"},
            {"name": "Osun State University"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_state_schools",
            return_value=[{"name": "Lagos State University", "acronym": "LASU"}],
        ):
            result = self.faker.state_school()
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_state_schools",
            return_value=[{"name": "Lagos State University", "acronym": "LASU"}],
        ):
            result = self.faker.state_school(acronym=True)
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    @patch("random.choice")
    def test_private_school_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test private_school method with location parameter."""
        mock_get_schools_by_location.return_value = [
            {"name": "Covenant University", "acronym": "CU", "ownership": "Private"},
            {"name": "Babcock University", "acronym": "BU", "ownership": "Private"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "Covenant University"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.private_school(location="Lagos")
            self.assertEqual(result, "Covenant University")

        # Test when acronym=True
        mock_choice.return_value = "CU"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.private_school(acronym=True, location="Lagos")
            self.assertEqual(result, "CU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_private_schools")
    @patch("random.choice")
    def test_private_school_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_schools: MagicMock,
    ) -> None:
        """Test private_school method without location parameter."""
        mock_get_private_schools.return_value = [
            {"name": "Covenant University", "acronym": "CU"},
            {"name": "Babcock University", "acronym": "BU"},
        ]
        # Test when acronym=False
        mock_choice.return_value = "Covenant University"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.private_school()
            self.assertEqual(result, "Covenant University")

        # Test when acronym=True
        mock_choice.return_value = "CU"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.private_school(acronym=True)
            self.assertEqual(result, "CU")


if __name__ == "__main__":
    unittest.main()
