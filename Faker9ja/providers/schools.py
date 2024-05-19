import json
import os


class SchoolProvider:
    """
    A class to provide information about Educational institutions in Nigeria.
    """

    def __init__(self):
        """Initializes the SchoolProvider instance."""

        # The path to the JSON file containing schools data
        self.data_path = os.path.join(os.path.dirname(__file__), "data", "schools.json")
        # Loads the json data for reuse
        self.schools_data = self.load_json(self.data_path)

    def load_json(self, file_path):
        """
        Load JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The loaded JSON data.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_schools(self):
        """
        Get a list of all the Schools.

        Returns:
            list: A list of school names.
        """
        return [school["name"] for school in self.schools_data["schools"]]

    def get_school_by_name(self, name):
        """
        Get information about a school by its name.

        Args:
            name (str): The name of the school.

        Returns:
            dict: Information about the school.
        """
        for school in self.get_schools():
            if school["name"] == name:
                return school
        return None

    def get_school_acronyms(self):
        """
        Get a list of all school acronyms.

        Returns:
            list: A list of school acronyms.
        """
        return [school["acronym"] for school in self.schools_data["schools"]]

    def get_schools_by_location(self, location):
        """
        Get a list of schools located at the specified location.

        Args:
            location (str): The location to filter schools by.

        Returns:
            list: A list of schools at the specified location.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["location"] == location
        ]

    def get_federal_schools(self):
        """
        Get a list of all federal schools.

        Returns:
            list: A list of dictionaries containing federal schools.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["ownership"] == "Federal"
        ]

    def get_state_schools(self):
        """
        Get a list of all state schools.

        Returns:
            list: A list of dictionaries containing state schools.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["ownership"] == "State"
        ]

    def get_private_schools(self):
        """
        Get a list of all private schools.

        Returns:
            list: A list of dictionaries containing private schools.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["ownership"] == "Private"
        ]

    def get_universities(self):
        """
        Get a list of all universities.

        Returns:
            list: A list of university names and information.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "University"
        ]

    def get_universities_by_location(self, location):
        """
        Get a list of universities at a specific location.

        Args:
            location (str): The location to filter universities.

        Returns:
            list: A list of universities at the specified location.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["location"] == location and school["type"] == "University"
        ]

    def get_polytechnics(self):
        """
        Get a list of all the polytechnics.

        Returns:
            list: A list of polytechnic names.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "Polytechnic"
        ]

    def get_polytechnics_by_location(self, location):
        """
        Get a list of polytechnics in a specific location.

        Args:
            location (str): The location to filter polytechnics.

        Returns:
            list: A list of polytechnics at the specified location.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["location"] == location and school["type"] == "Polytechnic"
        ]

    def get_colleges_of_education(self):
        """
        Get a list of all colleges of education.

        Returns:
            list: A list of dictionaries containing information about colleges of education.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "College of Education"
        ]

    def get_colleges_of_education_by_location(self, location):
        """
        Get a list of colleges of education at a specific location.

        Args:
            location (str): The location to filter colleges of education.

        Returns:
            list: A list of dictionaries containing colleges of education at the specified location.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["location"] == location
            and school["type"] == "College of Education"
        ]

    def get_federal_universities(self):
        """
        Get a list of all federal universities.

        Returns:
            list: A list of federal universities.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "University" and school["ownership"] == "Federal"
        ]

    def get_federal_polytechnics(self):
        """
        Get a list of all federal polytechnics.

        Returns:
            list: A list of federal polytechnics.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "Polytechnic" and school["ownership"] == "Federal"
        ]

    def get_federal_colleges_of_education(self):
        """
        Get a list of all federal colleges of education.

        Returns:
            list: A list of dictionaries of federal colleges of education.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "College of Education"
            and school["ownership"] == "Federal"
        ]

    def get_state_universities(self):
        """
        Get a list of all state universities.

        Returns:
            list: A list of state universities.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "University" and school["ownership"] == "State"
        ]

    def get_state_polytechnics(self):
        """
        Get a list of all state polytechnics.

        Returns:
            list: A list of state polytechnics.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "Polytechnic" and school["ownership"] == "State"
        ]

    def get_state_colleges_of_education(self):
        """
        Get a list of all state colleges of education.

        Returns:
            list: A list of dictionaries of state colleges of education.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "College of Education"
            and school["ownership"] == "State"
        ]

    def get_private_universities(self):
        """
        Get a list of all private universities.

        Returns:
            list: A list of private universities.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "University" and school["ownership"] == "Private"
        ]

    def get_private_polytechnics(self):
        """
        Get a list of all private polytechnics.

        Returns:
            list: A list of private polytechnics.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "Polytechnic" and school["ownership"] == "Private"
        ]

    def get_private_colleges_of_education(self):
        """
        Get a list of all private colleges of education.

        Returns:
            list: A list of dictionaries of private colleges of education.
        """
        return [
            school
            for school in self.schools_data["schools"]
            if school["type"] == "College of Education"
            and school["ownership"] == "Private"
        ]
