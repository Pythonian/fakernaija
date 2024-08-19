"""Unittests for functions in the utils module."""

import unittest
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from fakernaija.providers import (
    CourseProvider,
    DegreeProvider,
    FacultyProvider,
    NameProvider,
    SchoolProvider,
    StateProvider,
)
from fakernaija.utils import load_json, validate_json_structure


class NameProviderLoadJSONFirstNames(unittest.TestCase):
    """Unit tests for loading the JSON data of the NameProvider."""

    @patch("fakernaija.providers.name.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Ade", "extra": "value"},
            {"tribe": "igbo", "gender": "female", "name": "Ugochi"},
        ]
        self.required_keys: list[str] = ["tribe", "gender", "name"]
        self.name_provider = NameProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.name_provider.data_path / "first_names.json",
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.name_provider.data_path / 'first_names.json'}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class NameProviderLoadJSONLastNames(unittest.TestCase):
    """Unit tests for loading the JSON data of the NameProvider."""

    @patch("fakernaija.providers.name.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"tribe": "yoruba", "name": "Tinubu"},
            {"tribe": "igbo", "name": "Maduike"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"tribe": "yoruba"},
            {"name": "Maduike"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {"tribe": "yoruba", "gender": "male", "name": "Tinubu"},
            {"tribe": "igbo", "gender": "female", "name": "Maduike"},
        ]
        self.required_keys: list[str] = ["tribe", "name"]
        self.name_provider = NameProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.name_provider.data_path / "last_names.json",
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.name_provider.data_path / 'last_names.json'}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class CourseProviderLoadJSON(unittest.TestCase):
    """Unit tests for loading the JSON data of the CourseProvider."""

    @patch("fakernaija.providers.course.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"name": "Computer Science", "code": "CSC101"},
            {"name": "Mathematics", "code": "MTH101"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"name": "Computer Science"},
            {"name": "Mathematics", "code": "MTH101"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {"name": "Computer Science", "code": "CSC101", "extra": "value"},
            {"name": "Mathematics", "code": "MTH101"},
        ]
        self.required_keys: list[str] = ["name", "code"]
        self.course_provider = CourseProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.course_provider.data_path,
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.course_provider.data_path}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class DegreeProviderLoadJSON(unittest.TestCase):
    """Unit tests for loading the JSON data of the DegreeProvider."""

    @patch("fakernaija.providers.degree.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, str]] = [
            {"name": "Bachelor of Science", "degree_type": "B.Sc", "abbr": "B.Sc"},
            {"name": "Master of Science", "degree_type": "M.Sc", "abbr": "M.Sc"},
        ]
        self.invalid_data_missing_keys: list[dict[str, str]] = [
            {"name": "Bachelor of Science", "abbr": "B.Sc"},
            {"degree_type": "M.Sc", "abbr": "M.Sc"},
        ]
        self.invalid_data_extra_keys: list[dict[str, str]] = [
            {
                "name": "Bachelor of Science",
                "degree_type": "B.Sc",
                "abbr": "B.Sc",
                "extra": "value",
            },
            {"name": "Master of Science", "degree_type": "M.Sc", "abbr": "M.Sc"},
        ]
        self.required_keys: list[str] = ["name", "degree_type", "abbr"]
        self.degree_provider = DegreeProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.degree_provider.data_path,
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.degree_provider.data_path}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class FacultyProviderLoadJSON(unittest.TestCase):
    """Unit tests for loading the JSON data of the FacultyProvider."""

    @patch("fakernaija.providers.faculty.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, Any]] = [
            {"name": "Faculty of Science", "departments": ["Physics", "Chemistry"]},
            {"name": "Faculty of Arts", "departments": ["History", "Philosophy"]},
        ]
        self.invalid_data_missing_keys: list[dict[str, Any]] = [
            {"name": "Faculty of Science"},
            {"name": "Faculty of Arts", "departments": ["History", "Philosophy"]},
        ]
        self.invalid_data_extra_keys: list[dict[str, Any]] = [
            {
                "name": "Faculty of Science",
                "departments": ["Physics", "Chemistry"],
                "extra": "value",
            },
            {"name": "Faculty of Arts", "departments": ["History", "Philosophy"]},
        ]
        self.required_keys: list[str] = ["name", "departments"]
        self.faculty_provider = FacultyProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.faculty_provider.data_path,
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.faculty_provider.data_path}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class SchoolProviderLoadJSON(unittest.TestCase):
    """Unit tests for loading the JSON data of the SchoolProvider."""

    @patch("fakernaija.providers.school.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, Any]] = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "state": "Lagos",
                "type": "University",
                "ownership": "Federal",
            },
            {
                "name": "Covenant University",
                "acronym": "CU",
                "state": "Ogun",
                "type": "University",
                "ownership": "Private",
            },
        ]
        self.invalid_data_missing_keys: list[dict[str, Any]] = [
            {"name": "University of Lagos", "acronym": "UNILAG"},
            {
                "name": "Covenant University",
                "acronym": "CU",
                "state": "Ogun",
                "type": "University",
                "ownership": "Private",
            },
        ]
        self.invalid_data_extra_keys: list[dict[str, Any]] = [
            {
                "name": "University of Lagos",
                "acronym": "UNILAG",
                "state": "Lagos",
                "type": "University",
                "ownership": "Federal",
                "extra": "value",
            },
            {
                "name": "Covenant University",
                "acronym": "CU",
                "state": "Ogun",
                "type": "University",
                "ownership": "Private",
            },
        ]
        self.required_keys: list[str] = [
            "name",
            "acronym",
            "state",
            "type",
            "ownership",
        ]
        self.school_provider = SchoolProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.school_provider.data_path,
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.school_provider.data_path}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))


class StateProviderLoadJSON(unittest.TestCase):
    """Unit tests for loading the JSON data of the StateProvider."""

    @patch("fakernaija.providers.state.load_json")
    def setUp(self, mock_load_json: MagicMock) -> None:  # noqa: ARG002
        """Set up the test case with mock data."""
        self.valid_data: list[dict[str, Any]] = [
            {
                "code": "FC",
                "name": "FCT",
                "capital": "Abuja",
                "slogan": "Centre of Unity",
                "region": "North Central",
                "postal_code": "900001",
                "lgas": ["Abuja", "Kwali"],
            },
        ]
        self.invalid_data_missing_keys: list[dict[str, Any]] = [
            {"code": "FC", "name": "FCT"},
        ]
        self.invalid_data_extra_keys: list[dict[str, Any]] = [
            {
                "code": "FC",
                "name": "FCT",
                "capital": "Abuja",
                "slogan": "Centre of Unity",
                "region": "North Central",
                "postal_code": "900001",
                "extra": "key",
                "lgas": ["Abuja", "Kwali"],
            },
        ]
        self.required_keys: list[str] = [
            "name",
            "code",
            "capital",
            "slogan",
            "lgas",
            "region",
            "postal_code",
        ]
        self.state_provider = StateProvider()

    @patch("os.path.exists", return_value=False)
    def test_load_json_file_not_found(
        self,
        mock_exists: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test loading a JSON file that does not exist."""
        file_path = "non_existent.json"
        with self.assertRaises(FileNotFoundError) as context:
            load_json(file_path, self.required_keys)
        self.assertIn(f"File not found: {file_path}", str(context.exception))

    @patch(
        "pathlib.Path.open",
        new_callable=mock_open,
        read_data="{invalid_json",
    )
    def test_load_json_invalid_json(
        self,
        mock_file: MagicMock,  # noqa: ARG002
    ) -> None:
        """Test handling of invalid JSON format."""
        with self.assertRaises(ValueError) as context:
            load_json(
                self.state_provider.data_path,
                self.required_keys,
            )
        self.assertIn(
            f"Error decoding JSON from file: {self.state_provider.data_path}",
            str(context.exception),
        )

    def test_validate_json_structure_valid(self) -> None:
        """Test validating a valid JSON structure."""
        try:
            validate_json_structure(self.valid_data, self.required_keys)
        except ValueError:
            self.fail("validate_json_structure raised ValueError unexpectedly!")

    def test_validate_json_structure_missing_keys(self) -> None:
        """Test validating a JSON structure with missing keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_missing_keys, self.required_keys)
        self.assertIn("Missing keys", str(context.exception))

    def test_validate_json_structure_extra_keys(self) -> None:
        """Test validating a JSON structure with extra keys."""
        with self.assertRaises(ValueError) as context:
            validate_json_structure(self.invalid_data_extra_keys, self.required_keys)
        self.assertIn("Invalid keys", str(context.exception))
