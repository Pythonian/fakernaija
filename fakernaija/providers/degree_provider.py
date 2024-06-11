"""This module provides a DegreeProvider class for accessing information about degrees awarded in Nigerian schools from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json


class DegreeProvider:
    """A class to provide information about Degrees awarded in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the DegreeProvider.

        Sets the path to the directory containing degrees data.
        """
        self.data_path = Path(__file__).parent / "data" / "degrees.json"
        self.degrees_data = load_json(
            self.data_path,
            [
                "name",
                "degree_type",
                "initials",
            ],
        )

    def get_degrees(self) -> list[str]:
        """Get a list of all the degrees.

        Returns:
            list[str]: A list of degrees.
        """
        return [degree["name"] for degree in self.degrees_data]

    def get_degree_initials(self) -> list[str]:
        """Get a list of all the degree initials.

        Returns:
            list[str]: A list of degree initials.
        """
        return [degree["initials"] for degree in self.degrees_data]

    def _get_degrees_by_type(self, degree_type: str, initials: bool) -> list[str]:
        """Filter degrees based on degree type and whether to get initials.

        Args:
            degree_type (str): The degree type value to filter by.
            initials (bool): Whether to get initials instead of full degree names.

        Returns:
            list[str]: A list of filtered degrees.
        """
        key = "initials" if initials else "name"
        return [
            degree[key]
            for degree in self.degrees_data
            if degree["degree_type"] == degree_type
        ]

    def get_undergraduate_degrees(self, initials: bool = False) -> list[str]:
        """Get a list of all undergraduate degrees.

        Args:
            initials (bool): Whether to get initials instead of full degree names.

        Returns:
            list[str]: A list of undergraduate degrees.
        """
        return self._get_degrees_by_type("undergraduate", initials)

    def get_masters_degrees(self, initials: bool = False) -> list[str]:
        """Get a list of all masters degrees.

        Args:
            initials (bool): Whether to get initials instead of full degree names.

        Returns:
            list[str]: A list of masters degrees.
        """
        return self._get_degrees_by_type("masters", initials)

    def get_doctorate_degrees(self, initials: bool = False) -> list[str]:
        """Get a list of all doctorate degrees.

        Args:
            initials (bool): Whether to get initials instead of full degree names.

        Returns:
            list[str]: A list of doctorate degrees.
        """
        return self._get_degrees_by_type("doctorate", initials)
