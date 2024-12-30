import yaml
import os


class ConfigReader:
    """YAML Class to read config file"""

    def __init__(self, file_path: str):
        """
        Init and read YAML file
        :param file_path: YAML file path
        """
        self.file_path = file_path
        self.data = self._load_yaml()

    def _load_yaml(self):
        """Inner func: load YAML file and return"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"YAML file not found at {self.file_path}")
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            raise RuntimeError(f"Error reading YAML file: {e}")

    def get_data(self):
        """Get All YAML data"""
        return self.data