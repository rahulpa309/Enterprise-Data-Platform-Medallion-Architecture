"""
Configuration Loader

Loads all YAML configuration files used by the Banking Data Generator.
"""

from pathlib import Path
import yaml


class ConfigLoader:
    """
    Loads configuration files from the config folder.
    """

    def __init__(self):

        self.config_path = (
            Path(__file__).resolve().parent.parent / "config"
        )

        self.config = {}
        self.generation_rules = {}
        self.dq_rules = {}

    def _load_yaml(self, file_name: str) -> dict:
        """
        Load a YAML file.
        """

        file_path = self.config_path / file_name

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def load(self):
        """
        Load all configuration files.
        """

        self.config = self._load_yaml("config.yaml")

        self.generation_rules = self._load_yaml(
            "generation_rules.yaml"
        )

        self.dq_rules = self._load_yaml(
            "dq_rules.yaml"
        )

    def get_config(self):
        return self.config

    def get_generation_rules(self):
        return self.generation_rules

    def get_dq_rules(self):
        return self.dq_rules