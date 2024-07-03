import os
from pathlib import Path
from typing import Dict, Any
import logging


class LoggerConfigurator:
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        self._configure_logs_directory()
        self._configure_logging()

    def _configure_logs_directory(self):
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)

    def _configure_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[logging.FileHandler(f"{self.log_dir}/app.log"), logging.StreamHandler()],
        )
        self.logger = logging.getLogger(__name__)


class EnvironmentLoader:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def load_environment_settings(self) -> Dict[str, Any]:
        env_vars = ["EVUN", "EVPW", "EVSERIAL", "IQ_GATEWAY"]
        settings = {}

        for var in env_vars:
            value = os.getenv(var)
            if value is None:
                error_message = f"Environment variable {var} not found"
                self.logger.error(error_message)
                raise KeyError(error_message)
            settings[var.lower()] = value

        self.logger.info("Environment variables successfully retrieved")
        return settings
