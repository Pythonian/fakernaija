"""This module provides a DegreeProvider class for accessing information about degrees awarded in Nigerian schools from a JSON file."""

from pathlib import Path

from fakernaija.utils import load_json


class DegreeProvider:
    """A class to provide information about Degrees awarded in Nigerian schools."""

    def __init__(self) -> None:
        """Initializes the DegreeProvider.

        Sets the path to the directory containing degrees data.
        """
        self.data_path = Path(__file__).parent.parent / "data" / "degrees.json"
        self.degrees_data = load_json(
            self.data_path,
            [
                "name",
                "degree_type",
                "initials",
            ],
        )

    def get_degrees(
        self,
        degree_type: str | None = None,
        initials: bool = False,
    ) -> list[str]:
        """Get a list of degrees optionally filtered by type and whether to get initials.

        Args:
            degree_type (str | None, optional): The type of degree to filter by. Defaults to None (returns all degrees).
            initials (bool, optional): Whether to get initials instead of full degree names. Defaults to False.

        Returns:
            list[str]: A list of degrees or degree initials based on the filters.
        """
        degrees = self.degrees_data
        if degree_type:
            degrees = [
                degree for degree in degrees if degree["degree_type"] == degree_type
            ]
        return [
            degree["initials"] if initials else degree["name"] for degree in degrees
        ]

    def get_degree_initials(self, degree_type: str | None = None) -> list[str]:
        """Get a list of degree initials optionally filtered by degree type.

        Args:
            degree_type (str | None, optional): The type of degree to filter by. Defaults to None.

        Returns:
            list[str]: A list of degree initials.
        """
        return self.get_degrees(degree_type, initials=True)
