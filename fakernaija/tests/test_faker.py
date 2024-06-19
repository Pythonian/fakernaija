"""Unit tests for the Faker class.

This module contains unit tests for the Faker class, which provides methods
for generating random Nigerian data. The tests ensure that the
methods return the expected types and handle various inputs correctly.
"""

import unittest
from unittest.mock import MagicMock, patch

from fakernaija.faker import Faker


class TestFakerStateProvider(unittest.TestCase):
    """Unit tests for the Faker method from the StateProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()

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
        self.faker.state_provider.states_data = [
            {"region_initial": "SW"},
            {"region_initial": "SE"},
        ]
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


class TestFakerSchoolProvider(unittest.TestCase):
    """Unit tests for the Faker method from the SchoolProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()

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

        # Test when acronym=False
        mock_choice.return_value = "University of Lagos"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.school(location="Lagos")
            self.assertEqual(result, "University of Lagos")

        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[{"name": "University of Lagos", "acronym": "UNILAG"}],
        ):
            result = self.faker.school(acronym=True, location="Lagos")
            self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools")
    @patch("random.choice")
    def test_school_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools: MagicMock,
    ) -> None:
        """Test school method without location parameter."""
        mock_get_schools.return_value = [
            {"name": "Covenant University", "acronym": "CU"},
            {"name": "Babcock University", "acronym": "BU"},
        ]

        # Test when acronym=False
        mock_choice.return_value = "Covenant University"
        with patch.object(
            self.faker.school_provider,
            "get_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.school()
            self.assertEqual(result, "Covenant University")

        # Test when acronym=True
        mock_choice.return_value = "CU"
        with patch.object(
            self.faker.school_provider,
            "get_schools",
            return_value=[{"name": "Covenant University", "acronym": "CU"}],
        ):
            result = self.faker.school(acronym=True)
            self.assertEqual(result, "CU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    def test_school_with_location_no_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test school method with location but no schools available."""
        mock_get_schools_by_location.return_value = []

        result = self.faker.school(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools")
    def test_school_no_schools_available(self, mock_get_schools: MagicMock) -> None:
        """Test school method with no schools available."""
        mock_get_schools.return_value = []

        result = self.faker.school()
        self.assertIsNone(result)

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
            "get_schools_by_location",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_school(location="Lagos")
            self.assertEqual(result, "University of Lagos")

        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "ownership": "Federal",
                },
            ],
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
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "ownership": "Federal",
            },
            {
                "name": "Ahmadu Bello University",
                "acronym": "ABU",
                "ownership": "Federal",
            },
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
    def test_federal_school_with_location_no_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test federal_school method with location but no schools available."""
        mock_get_schools_by_location.return_value = []

        result = self.faker.federal_school(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    def test_federal_school_with_location_no_federal_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test federal_school method with location but no federal schools available."""
        mock_get_schools_by_location.return_value = [
            {"name": "Lagos State University", "acronym": "LASU", "ownership": "State"},
        ]

        result = self.faker.federal_school(location="Lagos")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_schools")
    def test_federal_school_no_schools_available(
        self,
        mock_get_federal_schools: MagicMock,
    ) -> None:
        """Test federal_school method with no schools available."""
        mock_get_federal_schools.return_value = []

        result = self.faker.federal_school()
        self.assertIsNone(result)

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
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_school(location="Lagos")
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "ownership": "State",
                },
            ],
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
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "ownership": "State",
            },
            {
                "name": "Ekiti State University",
                "acronym": "EKSU",
                "ownership": "State",
            },
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
    def test_state_school_with_location_no_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test state_school method with location but no schools available."""
        mock_get_schools_by_location.return_value = []

        result = self.faker.state_school(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    def test_state_school_with_location_no_state_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test state_school method with location but no state schools available."""
        mock_get_schools_by_location.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "ownership": "Federal",
            },
        ]

        result = self.faker.state_school(location="Lagos")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_schools")
    def test_state_school_no_schools_available(
        self,
        mock_get_state_schools: MagicMock,
    ) -> None:
        """Test state_school method with no schools available."""
        mock_get_state_schools.return_value = []

        result = self.faker.state_school()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    @patch("random.choice")
    def test_private_school_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test private_school method with location parameter."""
        mock_get_schools_by_location.return_value = [
            {
                "name": "Covenant University",
                "acronym": "CU",
                "ownership": "Private",
            },
            {
                "name": "Babcock University",
                "acronym": "BU",
                "ownership": "Private",
            },
        ]

        # Test when acronym=False
        mock_choice.return_value = "Covenant University"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[
                {
                    "name": "Covenant University",
                    "acronym": "CU",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_school(location="Ogun")
            self.assertEqual(result, "Covenant University")

        # Test when acronym=True
        mock_choice.return_value = "CU"
        with patch.object(
            self.faker.school_provider,
            "get_schools_by_location",
            return_value=[
                {
                    "name": "Covenant University",
                    "acronym": "CU",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_school(acronym=True, location="Ogun")
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
            {
                "name": "Covenant University",
                "acronym": "CU",
                "ownership": "Private",
            },
            {
                "name": "Babcock University",
                "acronym": "BU",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Covenant University"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[
                {
                    "name": "Covenant University",
                    "acronym": "CU",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_school()
            self.assertEqual(result, "Covenant University")
        # Test when acronym=True
        mock_choice.return_value = "CU"
        with patch.object(
            self.faker.school_provider,
            "get_private_schools",
            return_value=[
                {
                    "name": "Covenant University",
                    "acronym": "CU",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_school(acronym=True)
            self.assertEqual(result, "CU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    def test_private_school_with_location_no_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test private_school method with location but no schools available."""
        mock_get_schools_by_location.return_value = []

        result = self.faker.private_school(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_schools_by_location")
    def test_private_school_with_location_no_private_schools(
        self,
        mock_get_schools_by_location: MagicMock,
    ) -> None:
        """Test private_school method with location but no private schools available."""
        mock_get_schools_by_location.return_value = [
            {"name": "Federal University", "acronym": "FU", "ownership": "Federal"},
        ]

        result = self.faker.private_school(location="Lagos")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_private_schools")
    def test_private_school_no_schools_available(
        self,
        mock_get_private_schools: MagicMock,
    ) -> None:
        """Test private_school method with no schools available."""
        mock_get_private_schools.return_value = []

        result = self.faker.private_school()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    @patch("random.choice")
    def test_university_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_universities_by_location: MagicMock,
    ) -> None:
        """Test university method with location parameter."""
        mock_get_universities_by_location.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "type": "University",
            },
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "type": "University",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                },
            ],
        ):
            result = self.faker.university(location="Lagos")
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                },
            ],
        ):
            result = self.faker.university(acronym=True, location="Lagos")
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities")
    @patch("random.choice")
    def test_university_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test university method without location parameter."""
        mock_get_universities.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "type": "University",
            },
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "type": "University",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_universities",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                },
            ],
        ):
            result = self.faker.university()
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_universities",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                },
            ],
        ):
            result = self.faker.university(acronym=True)
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    def test_university_with_location_no_universities(
        self,
        mock_get_universities_by_location: MagicMock,
    ) -> None:
        """Test university method with location but no universities available."""
        mock_get_universities_by_location.return_value = []

        result = self.faker.university(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities")
    def test_university_no_universities_available(
        self,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test university method with no universities available."""
        mock_get_universities.return_value = []

        result = self.faker.university()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    @patch("random.choice")
    def test_polytechnic_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test polytechnic method with location parameter."""
        mock_get_polytechnics_by_location.return_value = [
            {
                "name": "Lagos State Polytechnic",
                "acronym": "LASPOTECH",
                "type": "Polytechnic",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Lagos State Polytechnic",
                    "acronym": "LASPOTECH",
                    "type": "Polytechnic",
                },
            ],
        ):
            result = self.faker.polytechnic(location="Lagos")
            self.assertEqual(result, "Lagos State Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "LASPOTECH"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Lagos State Polytechnic",
                    "acronym": "LASPOTECH",
                    "type": "Polytechnic",
                },
            ],
        ):
            result = self.faker.polytechnic(acronym=True, location="Lagos")
            self.assertEqual(result, "LASPOTECH")

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics")
    @patch("random.choice")
    def test_polytechnic_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_polytechnics: MagicMock,
    ) -> None:
        """Test polytechnic method without location parameter."""
        mock_get_polytechnics.return_value = [
            {
                "name": "Lagos State Polytechnic",
                "acronym": "LASPOTECH",
                "type": "Polytechnic",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics",
            return_value=[
                {
                    "name": "Lagos State Polytechnic",
                    "acronym": "LASPOTECH",
                    "type": "Polytechnic",
                },
            ],
        ):
            result = self.faker.polytechnic()
            self.assertEqual(result, "Lagos State Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "LASPOTECH"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics",
            return_value=[
                {
                    "name": "Lagos State Polytechnic",
                    "acronym": "LASPOTECH",
                    "type": "Polytechnic",
                },
            ],
        ):
            result = self.faker.polytechnic(acronym=True)
            self.assertEqual(result, "LASPOTECH")

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    def test_polytechnic_with_location_no_polytechnics(
        self,
        mock_get_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test polytechnic method with location but no polytechnics available."""
        mock_get_polytechnics_by_location.return_value = []

        result = self.faker.polytechnic(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics")
    def test_polytechnic_no_polytechnics_available(
        self,
        mock_get_polytechnics: MagicMock,
    ) -> None:
        """Test polytechnic method with no polytechnics available."""
        mock_get_polytechnics.return_value = []

        result = self.faker.polytechnic()
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    @patch("random.choice")
    def test_college_of_education_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test college_of_education method with location parameter."""
        mock_get_colleges_of_education_by_location.return_value = [
            {
                "name": "Corona College of Education",
                "acronym": "CCED",
                "type": "College of Education",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Corona College of Education"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Corona College of Education",
                    "acronym": "CCED",
                    "type": "College of Education",
                },
            ],
        ):
            result = self.faker.college_of_education(location="Lagos")
            self.assertEqual(result, "Corona College of Education")
        # Test when acronym=True
        mock_choice.return_value = "CCED"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Corona College of Education",
                    "acronym": "CCED",
                    "type": "College of Education",
                },
            ],
        ):
            result = self.faker.college_of_education(acronym=True, location="Lagos")
            self.assertEqual(result, "CCED")

    @patch("fakernaija.providers.schools.SchoolProvider.get_colleges_of_education")
    @patch("random.choice")
    def test_college_of_education_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_colleges_of_education: MagicMock,
    ) -> None:
        """Test college_of_education method without location parameter."""
        mock_get_colleges_of_education.return_value = [
            {
                "name": "Corona College of Education",
                "acronym": "CCED",
                "type": "College of Education",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Corona College of Education"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education",
            return_value=[
                {
                    "name": "Corona College of Education",
                    "acronym": "CCED",
                    "type": "College of Education",
                },
            ],
        ):
            result = self.faker.college_of_education()
            self.assertEqual(result, "Corona College of Education")
        # Test when acronym=True
        mock_choice.return_value = "CCED"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education",
            return_value=[
                {
                    "name": "Corona College of Education",
                    "acronym": "CCED",
                    "type": "College of Education",
                },
            ],
        ):
            result = self.faker.college_of_education(acronym=True)
            self.assertEqual(result, "CCED")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    def test_college_of_education_with_location_no_colleges_of_education(
        self,
        mock_get_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test college_of_education method with location but no colleges of education available."""
        mock_get_colleges_of_education_by_location.return_value = []

        result = self.faker.college_of_education(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_colleges_of_education")
    def test_college_of_education_no_colleges_of_education_available(
        self,
        mock_get_colleges_of_education: MagicMock,
    ) -> None:
        """Test college_of_education method with no colleges of education available."""
        mock_get_colleges_of_education.return_value = []

        result = self.faker.college_of_education()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    @patch("random.choice")
    def test_federal_university_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_universities_by_location: MagicMock,
    ) -> None:
        """Test federal_university method with location parameter."""
        mock_get_federal_universities_by_location.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "type": "University",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "University of Lagos"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "type": "University",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_university(location="Lagos")
            self.assertEqual(result, "University of Lagos")
        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "type": "University",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_university(acronym=True, location="Lagos")
            self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_universities")
    @patch("random.choice")
    def test_federal_university_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test federal_university method without location parameter."""
        mock_get_universities.return_value = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "type": "University",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "University of Lagos"
        with patch.object(
            self.faker.school_provider,
            "get_federal_universities",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "type": "University",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_university()
            self.assertEqual(result, "University of Lagos")
        # Test when acronym=True
        mock_choice.return_value = "UNILAG"
        with patch.object(
            self.faker.school_provider,
            "get_federal_universities",
            return_value=[
                {
                    "name": "University of Lagos",
                    "acronym": "UNILAG",
                    "type": "University",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_university(acronym=True)
            self.assertEqual(result, "UNILAG")

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    def test_federal_university_with_location_no_universities(
        self,
        mock_get_federal_universities_by_location: MagicMock,
    ) -> None:
        """Test federal_university method with location but no universities available."""
        mock_get_federal_universities_by_location.return_value = []

        result = self.faker.federal_university(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_universities")
    def test_federal_university_no_universities_available(
        self,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test federal_university method with no universities available."""
        mock_get_universities.return_value = []

        result = self.faker.federal_university()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    @patch("random.choice")
    def test_federal_polytechnic_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test federal_polytechnic method with location parameter."""
        mock_get_federal_polytechnics_by_location.return_value = [
            {
                "name": "Federal Polytechnic Ado Ekiti",
                "acronym": "FEDPOLYADO",
                "type": "Polytechnic",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Federal Polytechnic Ado Ekiti"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Federal Polytechnic Ado Ekiti",
                    "acronym": "FEDPOLYADO",
                    "type": "Polytechnic",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_polytechnic(location="Ekiti")
            self.assertEqual(result, "Federal Polytechnic Ado Ekiti")
        # Test when acronym=True
        mock_choice.return_value = "FEDPOLYADO"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Federal Polytechnic Ado Ekiti",
                    "acronym": "FEDPOLYADO",
                    "type": "Polytechnic",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_polytechnic(acronym=True, location="Ekiti")
            self.assertEqual(result, "FEDPOLYADO")

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_polytechnics")
    @patch("random.choice")
    def test_federal_polytechnic_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_polytechnics: MagicMock,
    ) -> None:
        """Test federal_polytechnic method without location parameter."""
        mock_get_federal_polytechnics.return_value = [
            {
                "name": "Federal Polytechnic Ado Ekiti",
                "acronym": "FEDPOLYADO",
                "type": "Polytechnic",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Federal Polytechnic Ado Ekiti"
        with patch.object(
            self.faker.school_provider,
            "get_federal_polytechnics",
            return_value=[
                {
                    "name": "Federal Polytechnic Ado Ekiti",
                    "acronym": "FEDPOLYADO",
                    "type": "Polytechnic",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_polytechnic()
            self.assertEqual(result, "Federal Polytechnic Ado Ekiti")
        # Test when acronym=True
        mock_choice.return_value = "FEDPOLYADO"
        with patch.object(
            self.faker.school_provider,
            "get_federal_polytechnics",
            return_value=[
                {
                    "name": "Federal Polytechnic Ado Ekiti",
                    "acronym": "FEDPOLYADO",
                    "type": "Polytechnic",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_polytechnic(acronym=True)
            self.assertEqual(result, "FEDPOLYADO")

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    def test_federal_polytechnic_with_location_no_polytechnics(
        self,
        mock_get_federal_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test federal_polytechnic method with location but no polytechnics available."""
        mock_get_federal_polytechnics_by_location.return_value = []

        result = self.faker.federal_polytechnic(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_federal_polytechnics")
    def test_federal_polytechnic_no_polytechnics_available(
        self,
        mock_get_federal_polytechnics: MagicMock,
    ) -> None:
        """Test federal_polytechnic method with no polytechnics available."""
        mock_get_federal_polytechnics.return_value = []

        result = self.faker.federal_polytechnic()
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    @patch("random.choice")
    def test_federal_college_of_education_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test federal_college_of_education method with location parameter."""
        mock_get_federal_colleges_of_education_by_location.return_value = [
            {
                "name": "Federal College of Education, Zaria",
                "acronym": "FCEZARIA",
                "type": "College of Education",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Federal College of Education, Zaria"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Federal College of Education, Zaria",
                    "acronym": "FCEZARIA",
                    "type": "College of Education",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_college_of_education(location="Kaduna")
            self.assertEqual(result, "Federal College of Education, Zaria")
        # Test when acronym=True
        mock_choice.return_value = "FCEZARIA"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Federal College of Education, Zaria",
                    "acronym": "FCEZARIA",
                    "type": "College of Education",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_college_of_education(
                acronym=True,
                location="Kaduna",
            )
            self.assertEqual(result, "FCEZARIA")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_federal_colleges_of_education",
    )
    @patch("random.choice")
    def test_federal_college_of_education_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_federal_colleges_of_education: MagicMock,
    ) -> None:
        """Test federal_college_of_education method without location parameter."""
        mock_get_federal_colleges_of_education.return_value = [
            {
                "name": "Federal College of Education, Zaria",
                "acronym": "FCEZARIA",
                "type": "College of Education",
                "ownership": "Federal",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Federal College of Education, Zaria"
        with patch.object(
            self.faker.school_provider,
            "get_federal_colleges_of_education",
            return_value=[
                {
                    "name": "Federal College of Education, Zaria",
                    "acronym": "FCEZARIA",
                    "type": "College of Education",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_college_of_education()
            self.assertEqual(result, "Federal College of Education, Zaria")
        # Test when acronym=True
        mock_choice.return_value = "FCEZARIA"
        with patch.object(
            self.faker.school_provider,
            "get_federal_colleges_of_education",
            return_value=[
                {
                    "name": "Federal College of Education, Zaria",
                    "acronym": "FCEZARIA",
                    "type": "College of Education",
                    "ownership": "Federal",
                },
            ],
        ):
            result = self.faker.federal_college_of_education(acronym=True)
            self.assertEqual(result, "FCEZARIA")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    def test_federal_college_of_education_with_location_no_colleges(
        self,
        mock_get_federal_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test federal_college_of_education method with location but no colleges available."""
        mock_get_federal_colleges_of_education_by_location.return_value = []

        result = self.faker.federal_college_of_education(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_federal_colleges_of_education",
    )
    def test_federal_college_of_education_no_colleges_available(
        self,
        mock_get_federal_colleges_of_education: MagicMock,
    ) -> None:
        """Test federal_college_of_education method with no colleges available."""
        mock_get_federal_colleges_of_education.return_value = []

        result = self.faker.federal_college_of_education()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    @patch("random.choice")
    def test_state_university_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_universities_by_location: MagicMock,
    ) -> None:
        """Test state_university method with location parameter."""
        mock_get_state_universities_by_location.return_value = [
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "type": "University",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_university(location="Lagos")
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_university(acronym=True, location="Lagos")
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_universities")
    @patch("random.choice")
    def test_state_university_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_universities: MagicMock,
    ) -> None:
        """Test state_university method without location parameter."""
        mock_get_state_universities.return_value = [
            {
                "name": "Lagos State University",
                "acronym": "LASU",
                "type": "University",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Lagos State University"
        with patch.object(
            self.faker.school_provider,
            "get_state_universities",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_university()
            self.assertEqual(result, "Lagos State University")
        # Test when acronym=True
        mock_choice.return_value = "LASU"
        with patch.object(
            self.faker.school_provider,
            "get_state_universities",
            return_value=[
                {
                    "name": "Lagos State University",
                    "acronym": "LASU",
                    "type": "University",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_university(acronym=True)
            self.assertEqual(result, "LASU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    def test_state_university_with_location_no_universities(
        self,
        mock_get_state_universities_by_location: MagicMock,
    ) -> None:
        """Test state_university method with location but no universities available."""
        mock_get_state_universities_by_location.return_value = []

        result = self.faker.state_university(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_universities")
    def test_state_university_no_universities_available(
        self,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test state_university method with no universities available."""
        mock_get_universities.return_value = []

        result = self.faker.state_university()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    @patch("random.choice")
    def test_state_polytechnic_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test state_polytechnic method with location parameter."""
        mock_get_state_polytechnics_by_location.return_value = [
            {
                "name": "Akwa Ibom State Polytechnic",
                "acronym": "AKWAPOLY",
                "type": "Polytechnic",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Akwa Ibom State Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Akwa Ibom State Polytechnic",
                    "acronym": "AKWAPOLY",
                    "type": "Polytechnic",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_polytechnic(location="Akwa Ibom")
            self.assertEqual(result, "Akwa Ibom State Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "AKWAPOLY"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Akwa Ibom State Polytechnic",
                    "acronym": "AKWAPOLY",
                    "type": "Polytechnic",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_polytechnic(acronym=True, location="Akwa Ibom")
            self.assertEqual(result, "AKWAPOLY")

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_polytechnics")
    @patch("random.choice")
    def test_state_polytechnic_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_polytechnics: MagicMock,
    ) -> None:
        """Test state_polytechnic method without location parameter."""
        mock_get_state_polytechnics.return_value = [
            {
                "name": "Akwa Ibom State Polytechnic",
                "acronym": "AKWAPOLY",
                "type": "Polytechnic",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Akwa Ibom State Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_state_polytechnics",
            return_value=[
                {
                    "name": "Akwa Ibom State Polytechnic",
                    "acronym": "AKWAPOLY",
                    "type": "Polytechnic",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_polytechnic()
            self.assertEqual(result, "Akwa Ibom State Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "AKWAPOLY"
        with patch.object(
            self.faker.school_provider,
            "get_state_polytechnics",
            return_value=[
                {
                    "name": "Akwa Ibom State Polytechnic",
                    "acronym": "AKWAPOLY",
                    "type": "Polytechnic",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_polytechnic(acronym=True)
            self.assertEqual(result, "AKWAPOLY")

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    def test_state_polytechnic_with_location_no_polytechnics(
        self,
        mock_get_state_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test state_polytechnic method with location but no polytechnics available."""
        mock_get_state_polytechnics_by_location.return_value = []

        result = self.faker.state_polytechnic(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_polytechnics")
    def test_state_polytechnic_no_polytechnics_available(
        self,
        mock_get_state_polytechnics: MagicMock,
    ) -> None:
        """Test state_polytechnic method with no polytechnics available."""
        mock_get_state_polytechnics.return_value = []

        result = self.faker.state_polytechnic()
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    @patch("random.choice")
    def test_state_college_of_education_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test state_college_of_education method with location parameter."""
        mock_get_state_colleges_of_education_by_location.return_value = [
            {
                "name": "College of Education, Ikere-Ekiti",
                "acronym": "COEIKERE",
                "type": "College of Education",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "College of Education, Ikere-Ekiti"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "College of Education, Ikere-Ekiti",
                    "acronym": "COEIKERE",
                    "type": "College of Education",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_college_of_education(location="Ekiti")
            self.assertEqual(result, "College of Education, Ikere-Ekiti")
        # Test when acronym=True
        mock_choice.return_value = "COEIKERE"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "College of Education, Ikere-Ekiti",
                    "acronym": "COEIKERE",
                    "type": "College of Education",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_college_of_education(
                acronym=True,
                location="Ekiti",
            )
            self.assertEqual(result, "COEIKERE")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_state_colleges_of_education",
    )
    @patch("random.choice")
    def test_state_college_of_education_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_state_colleges_of_education: MagicMock,
    ) -> None:
        """Test state_college_of_education method without location parameter."""
        mock_get_state_colleges_of_education.return_value = [
            {
                "name": "College of Education, Ikere-Ekiti",
                "acronym": "COEIKERE",
                "type": "College of Education",
                "ownership": "State",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "College of Education, Ikere-Ekiti"
        with patch.object(
            self.faker.school_provider,
            "get_state_colleges_of_education",
            return_value=[
                {
                    "name": "College of Education, Ikere-Ekiti",
                    "acronym": "COEIKERE",
                    "type": "College of Education",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_college_of_education()
            self.assertEqual(result, "College of Education, Ikere-Ekiti")
        # Test when acronym=True
        mock_choice.return_value = "COEIKERE"
        with patch.object(
            self.faker.school_provider,
            "get_state_colleges_of_education",
            return_value=[
                {
                    "name": "College of Education, Ikere-Ekiti",
                    "acronym": "COEIKERE",
                    "type": "College of Education",
                    "ownership": "State",
                },
            ],
        ):
            result = self.faker.state_college_of_education(acronym=True)
            self.assertEqual(result, "COEIKERE")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    def test_state_college_of_education_with_location_no_colleges(
        self,
        mock_get_state_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test state_college_of_education method with location but no colleges available."""
        mock_get_state_colleges_of_education_by_location.return_value = []

        result = self.faker.state_college_of_education(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_state_colleges_of_education",
    )
    def test_state_college_of_education_no_colleges_available(
        self,
        mock_get_state_colleges_of_education: MagicMock,
    ) -> None:
        """Test state_college_of_education method with no colleges available."""
        mock_get_state_colleges_of_education.return_value = []

        result = self.faker.state_college_of_education()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    @patch("random.choice")
    def test_private_university_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_universities_by_location: MagicMock,
    ) -> None:
        """Test private_university method with location parameter."""
        mock_get_private_universities_by_location.return_value = [
            {
                "name": "Pan-Atlantic University",
                "acronym": "PAU",
                "type": "University",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Pan-Atlantic University"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Pan-Atlantic University",
                    "acronym": "PAU",
                    "type": "University",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_university(location="Lagos")
            self.assertEqual(result, "Pan-Atlantic University")
        # Test when acronym=True
        mock_choice.return_value = "PAU"
        with patch.object(
            self.faker.school_provider,
            "get_universities_by_location",
            return_value=[
                {
                    "name": "Pan-Atlantic University",
                    "acronym": "PAU",
                    "type": "University",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_university(acronym=True, location="Lagos")
            self.assertEqual(result, "PAU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_state_universities")
    @patch("random.choice")
    def test_private_university_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_universities: MagicMock,
    ) -> None:
        """Test private_university method without location parameter."""
        mock_get_private_universities.return_value = [
            {
                "name": "Pan-Atlantic University",
                "acronym": "PAU",
                "type": "University",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Pan-Atlantic University"
        with patch.object(
            self.faker.school_provider,
            "get_private_universities",
            return_value=[
                {
                    "name": "Pan-Atlantic University",
                    "acronym": "PAU",
                    "type": "University",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_university()
            self.assertEqual(result, "Pan-Atlantic University")
        # Test when acronym=True
        mock_choice.return_value = "PAU"
        with patch.object(
            self.faker.school_provider,
            "get_private_universities",
            return_value=[
                {
                    "name": "Pan-Atlantic University",
                    "acronym": "PAU",
                    "type": "University",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_university(acronym=True)
            self.assertEqual(result, "PAU")

    @patch("fakernaija.providers.schools.SchoolProvider.get_universities_by_location")
    def test_private_university_with_location_no_universities(
        self,
        mock_get_private_universities_by_location: MagicMock,
    ) -> None:
        """Test private_university method with location but no universities available."""
        mock_get_private_universities_by_location.return_value = []

        result = self.faker.private_university(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_private_universities")
    def test_private_university_no_universities_available(
        self,
        mock_get_universities: MagicMock,
    ) -> None:
        """Test private_university method with no universities available."""
        mock_get_universities.return_value = []

        result = self.faker.private_university()
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    @patch("random.choice")
    def test_private_polytechnic_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test private_polytechnic method with location parameter."""
        mock_get_private_polytechnics_by_location.return_value = [
            {
                "name": "Crown Polytechnic",
                "acronym": "CROWNPOLY",
                "type": "Polytechnic",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Crown Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Crown Polytechnic",
                    "acronym": "CROWNPOLY",
                    "type": "Polytechnic",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_polytechnic(location="Ekiti")
            self.assertEqual(result, "Crown Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "CROWNPOLY"
        with patch.object(
            self.faker.school_provider,
            "get_polytechnics_by_location",
            return_value=[
                {
                    "name": "Crown Polytechnic",
                    "acronym": "CROWNPOLY",
                    "type": "Polytechnic",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_polytechnic(acronym=True, location="Ekiti")
            self.assertEqual(result, "CROWNPOLY")

    @patch("fakernaija.providers.schools.SchoolProvider.get_private_polytechnics")
    @patch("random.choice")
    def test_private_polytechnic_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_polytechnics: MagicMock,
    ) -> None:
        """Test private_polytechnic method without location parameter."""
        mock_get_private_polytechnics.return_value = [
            {
                "name": "Crown Polytechnic",
                "acronym": "CROWNPOLY",
                "type": "Polytechnic",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Crown Polytechnic"
        with patch.object(
            self.faker.school_provider,
            "get_private_polytechnics",
            return_value=[
                {
                    "name": "Crown Polytechnic",
                    "acronym": "CROWNPOLY",
                    "type": "Polytechnic",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_polytechnic()
            self.assertEqual(result, "Crown Polytechnic")
        # Test when acronym=True
        mock_choice.return_value = "CROWNPOLY"
        with patch.object(
            self.faker.school_provider,
            "get_private_polytechnics",
            return_value=[
                {
                    "name": "Crown Polytechnic",
                    "acronym": "CROWNPOLY",
                    "type": "Polytechnic",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_polytechnic(acronym=True)
            self.assertEqual(result, "CROWNPOLY")

    @patch("fakernaija.providers.schools.SchoolProvider.get_polytechnics_by_location")
    def test_private_polytechnic_with_location_no_polytechnics(
        self,
        mock_get_private_polytechnics_by_location: MagicMock,
    ) -> None:
        """Test private_polytechnic method with location but no polytechnics available."""
        mock_get_private_polytechnics_by_location.return_value = []

        result = self.faker.private_polytechnic(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch("fakernaija.providers.schools.SchoolProvider.get_private_polytechnics")
    def test_private_polytechnic_no_polytechnics_available(
        self,
        mock_get_private_polytechnics: MagicMock,
    ) -> None:
        """Test private_polytechnic method with no polytechnics available."""
        mock_get_private_polytechnics.return_value = []

        result = self.faker.private_polytechnic()
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    @patch("random.choice")
    def test_private_college_of_education_with_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test private_college_of_education method with location parameter."""
        mock_get_private_colleges_of_education_by_location.return_value = [
            {
                "name": "Best Legacy College of Education",
                "acronym": "BESTLEGACY",
                "type": "College of Education",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Best Legacy College of Education"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Best Legacy College of Education",
                    "acronym": "BESTLEGACY",
                    "type": "College of Education",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_college_of_education(location="Oyo")
            self.assertEqual(result, "Best Legacy College of Education")
        # Test when acronym=True
        mock_choice.return_value = "BESTLEGACY"
        with patch.object(
            self.faker.school_provider,
            "get_colleges_of_education_by_location",
            return_value=[
                {
                    "name": "Best Legacy College of Education",
                    "acronym": "BESTLEGACY",
                    "type": "College of Education",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_college_of_education(
                acronym=True,
                location="Oyo",
            )
            self.assertEqual(result, "BESTLEGACY")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_private_colleges_of_education",
    )
    @patch("random.choice")
    def test_private_college_of_education_without_location(
        self,
        mock_choice: MagicMock,
        mock_get_private_colleges_of_education: MagicMock,
    ) -> None:
        """Test private_college_of_education method without location parameter."""
        mock_get_private_colleges_of_education.return_value = [
            {
                "name": "Best Legacy College of Education",
                "acronym": "BESTLEGACY",
                "type": "College of Education",
                "ownership": "Private",
            },
        ]
        # Test when acronym=False
        mock_choice.return_value = "Best Legacy College of Education"
        with patch.object(
            self.faker.school_provider,
            "get_private_colleges_of_education",
            return_value=[
                {
                    "name": "Best Legacy College of Education",
                    "acronym": "BESTLEGACY",
                    "type": "College of Education",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_college_of_education()
            self.assertEqual(result, "Best Legacy College of Education")
        # Test when acronym=True
        mock_choice.return_value = "BESTLEGACY"
        with patch.object(
            self.faker.school_provider,
            "get_private_colleges_of_education",
            return_value=[
                {
                    "name": "Best Legacy College of Education",
                    "acronym": "BESTLEGACY",
                    "type": "College of Education",
                    "ownership": "Private",
                },
            ],
        ):
            result = self.faker.private_college_of_education(acronym=True)
            self.assertEqual(result, "BESTLEGACY")

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_colleges_of_education_by_location",
    )
    def test_private_college_of_education_with_location_no_colleges(
        self,
        mock_get_private_colleges_of_education_by_location: MagicMock,
    ) -> None:
        """Test private_college_of_education method with location but no colleges available."""
        mock_get_private_colleges_of_education_by_location.return_value = []

        result = self.faker.private_college_of_education(location="NonExistentLocation")
        self.assertIsNone(result)

    @patch(
        "fakernaija.providers.schools.SchoolProvider.get_private_colleges_of_education",
    )
    def test_private_college_of_education_no_colleges_available(
        self,
        mock_get_private_colleges_of_education: MagicMock,
    ) -> None:
        """Test private_college_of_education method with no colleges available."""
        mock_get_private_colleges_of_education.return_value = []

        result = self.faker.private_college_of_education()
        self.assertIsNone(result)


class TestFakerNameProvider(unittest.TestCase):
    """Unit tests for the Faker method from the NameProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()

    def test_full_name(self) -> None:
        """Test that full_name returns a string."""
        name = self.faker.full_name()
        self.assertIsInstance(name, str)

    def test_first_name(self) -> None:
        """Test that first_name returns a string."""
        name = self.faker.first_name()
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

    def test_traditional_male_title(self) -> None:
        """Test that traditional_male_title returns a string."""
        prefix = self.faker.traditional_male_title()
        self.assertIsInstance(prefix, str)

    def test_traditional_female_title(self) -> None:
        """Test that traditional_female_title returns a string."""
        prefix = self.faker.traditional_female_title()
        self.assertIsInstance(prefix, str)

    def test_professional_title(self) -> None:
        """Test that professional_title returns a string."""
        prefix = self.faker.professional_title()
        self.assertIsInstance(prefix, str)


class TestFakerEmailProvider(unittest.TestCase):
    """Unit tests for the Faker method from the EmailProvider."""

    def setUp(self) -> None:
        """Set up the test case environment."""
        self.faker = Faker()
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
