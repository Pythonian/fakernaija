"""This module provides a DegreeProvider class for accessing information about degrees awarded in Nigerian schools from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json, normalize_input


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
        self.valid_degree_types = ["undergraduate", "masters", "doctorate"]

    def validate_degree_type(self, degree_type: str | None) -> str | None:
        """Normalize and validate degree type.

        Args:
            degree_type (str): The type of degree to validate.

        Returns:
            str: The validated and lowercased degree type.

        Raises:
            ValueError: If the degree type is not valid.
        """
        degree_type = normalize_input(degree_type)
        if degree_type and degree_type not in self.valid_degree_types:
            msg = f"Invalid degree_type. Must be one of {self.valid_degree_types}."
            raise ValueError(msg)
        return degree_type

    def get_degrees(self, degree_type: str | None = None) -> list[dict]:
        """Get a list of degrees filtered by degree type if specified.

        Args:
            degree_type (str | None, optional): The type of degree to filter by.
                                                Defaults to None (any degree type).

        Returns:
            list[dict]: A list of degree dictionaries.
        """
        degree_type = self.validate_degree_type(degree_type)
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
