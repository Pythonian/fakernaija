import json
import os
import random


class NameProvider:
    """
    Provides functionality for generating names based on ethnicity and gender.

    Attributes:
        data_path (str): The path to the directory containing name data files.
    """

    def __init__(self, data_path=None):
        """
        Initialize the NameProvider.

        Args:
            data_path (str, optional):
                The path to the directory containing name data files.
        """

        if data_path is None:
            self.data_path = os.path.join(os.path.dirname(__file__), "data")
        else:
            self.data_path = data_path

    def load_json(self, file_path):
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The data loaded from the JSON file.
        """

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_first_names(self, tribe=None, gender=None):
        """
        Get a list of first names optionally filtered by ethnic group and gender.

        Args:
            tribe (str, optional):
                The ethnic group to filter by. Defaults to None.
            gender (str, optional):
                The gender to filter by. Defaults to None.

        Returns:
            list: A list of first names matching the specified filters.
        """

        if tribe:
            file_path = os.path.join(
                self.data_path, "names", "tribes", tribe, "first_names"
            )
        else:
            file_path = os.path.join(self.data_path, "names", "tribes")
        first_names = []
        for _, _, files in os.walk(file_path):
            for file in files:
                if file.endswith(".json"):
                    file_data = self.load_json(os.path.join(file_path, file))
                    if gender:
                        file_data = [
                            name for name in file_data if name["gender"] == gender
                        ]
                    first_names.extend(file_data)
        return first_names

    def get_last_names(self, tribe=None):
        """
        Get a list of last names optionally filtered by ethnic group.
        Last names are not gender specific so we do not filter by gender here.

        Args:
            tribe (str, optional):
                The ethnic group to filter by. Defaults to None.

        Returns:
            list: A list of last names matching the specified filter.
        """

        if tribe:
            file_path = os.path.join(
                self.data_path, "names", "tribes", tribe, "last_names.json"
            )
        else:
            file_path = os.path.join(
                self.data_path, "names", "tribes", "last_names.json"
            )
        return self.load_json(file_path)

    def generate_first_name(self, tribe=None, gender=None):
        """
        Generate a random first name optionally from a specific ethnic group and gender.

        Args:
            tribe (str, optional):
                The ethnic group of the name. Defaults to None.
            gender (str, optional):
                The gender of the name. Defaults to None.

        Returns:
            str: A random first name.
        """

        first_names = self.get_first_names(tribe)
        if first_names:
            if gender:
                first_names = [
                    name for name in first_names if name.get("gender") == gender
                ]
            return random.choice(first_names)["name"]
        else:
            return None

    def generate_full_name(self, tribe=None, gender=None):
        """
        Generate a random full name optionally from a specific ethnic group and gender.

        Args:
            tribe (str, optional):
                The ethnic group of the name. Defaults to None.
            gender (str, optional):
                The gender of the name. Defaults to None.

        Returns:
            str: A random full name.
        """

        first_name = self.generate_first_name(tribe, gender)
        last_name = random.choice(self.get_last_names(tribe))["name"]
        if first_name:
            return f"{first_name} {last_name}"
        else:
            return None

    def generate_last_name(self, tribe=None):
        """
        Generate a random last name optionally from a specific ethnic group.

        Args:
            tribe (str, optional):
                The ethnic group of the name. Defaults to None.

        Returns:
            str: A random last name.
        """

        last_names = self.get_last_names(tribe)
        if last_names:
            return random.choice(last_names)["name"]
        else:
            return None
