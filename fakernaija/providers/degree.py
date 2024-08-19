"""This module provides a DegreeProvider class for accessing information about degrees awarded in Nigerian schools from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json


class DegreeProvider:
    """A class to provide information about Degrees in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the DegreeProvider.

        Sets the path to the directory containing Degrees data.
        """
        self.data_path = Path(__file__).parent.parent / "data" / "degrees.json"
        self.degrees_data = load_json(
            self.data_path,
            [
                "name",
                "degree_type",
                "abbr",
            ],
        )

    def get_degrees(self, degree_type: str | None = None) -> list[dict]:
        """Get a list of degrees filtered by degree type if specified.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                                                Defaults to None (any degree type).

        Returns:
            list[dict]: A list of degree dictionaries.
        """
        if degree_type:
            return [
                degree
                for degree in self.degrees_data
                if degree["degree_type"] == degree_type
            ]
        return self.degrees_data

    def get_degree_names(self, degree_type: str | None = None) -> list[str]:
        """Get a list of degree names filtered by degree type if specified.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                                                Defaults to None (any degree type).

        Returns:
            list[str]: A list of degree names.
        """
        return [degree["name"] for degree in self.get_degrees(degree_type)]

    def get_degree_abbrs(self, degree_type: str | None = None) -> list[str]:
        """Get a list of degree abbreviations filtered by degree type if specified.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                                                Defaults to None (any degree type).

        Returns:
            list[str]: A list of degree abbreviations.
        """
        return [degree["abbr"] for degree in self.get_degrees(degree_type)]
