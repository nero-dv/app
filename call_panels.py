import logging
import os
from typing import Dict, List, Literal
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv("./.env")

# Import internal modules using relative paths
import config.jwt as jwt
from config import ash

# Disable SSL warnings
urllib3.disable_warnings()


def read_token() -> str | Literal[1]:
    """
    Reads the token from environment variables. Generates a new one if not found.

    Returns:
        str: The token.
    """
    token = os.getenv("ENPHASE_JWT")
    if token is None:
        token = jwt.run()
    return token


class DataFetcher:
    """
    A class to fetch data from given URLs and process the responses.
    """

    def __init__(self, logger: logging.Logger):
        """
        Initializes the DataFetcher with a logger.

        Args:
            logger (logging.Logger): The logger instance.
        """
        self.logger = logger

    def fetch_data(self, urls: List[str], headers: Dict[str, str], timeout: int = 60) -> List[requests.Response]:
        """
        Fetches data from the given URLs with the provided headers.

        Args:
            urls (List[str]): List of URLs to fetch data from.
            headers (Dict[str, str]): Headers to include in the request.
            timeout (int): Timeout for the request. Defaults to 60 seconds.

        Returns:
            List[requests.Response]: Responses from the URLs.
        """
        responses = []
        for url in urls:
            try:
                response = requests.get(url, headers=headers, verify=False, timeout=timeout)
                responses.append(response)
            except requests.RequestException as e:
                self.logger.error(f"Request failed for {url}: {str(e)}")
                responses.append(None)
        return responses

    def save_response_to_file(self, response: requests.Response, filename: str) -> None:
        """
        Saves the response content to a file.

        Args:
            response (requests.Response): The response to save.
            filename (str): Path to the file where the response will be saved.
        """
        try:
            with open(filename, "w") as file:
                file.write(response.text)
            self.logger.info(f"Saved: {filename}")
        except IOError as e:
            self.logger.error(f"Failed to save {filename}: {str(e)}")

    def process_responses(
        self, response_list: List[requests.Response], urls: List[str], timestamp: int, logdir: str
    ) -> None:
        """
        Processes the list of responses, saving successful responses to files and logging errors.

        Args:
            response_list (List[requests.Response]): List of responses to process.
            urls (List[str]): List of URLs that were requested.
            timestamp (int): Current timestamp.
            logdir (str): Directory where logs will be saved.
        """
        for i, response in enumerate(response_list):
            if response is not None and response.status_code == 200:
                name = urls[i].split("/")[-1]
                filename = os.path.join(logdir, f"{timestamp}_{name}.json")
                self.save_response_to_file(response, filename)
            else:
                status_code = response.status_code if response else "No Response"
                self.logger.error(f"Failed to get data from {urls[i]}. Status Code: {status_code}")


def initialize_logger(log_directory: str) -> logging.Logger:
    """
    Initializes and returns a logger.

    Args:
        log_directory (str): Directory where logs will be saved.

    Returns:
        logging.Logger: Configured logger.
    """
    logger_configurator = ash.LoggerConfigurator(log_directory)
    return logger_configurator.logger


def load_environment_settings(logger: logging.Logger) -> dict:
    """
    Loads and returns environment settings.

    Args:
        logger (logging.Logger): The logger instance.

    Returns:
        dict: Environment settings.
    """
    environment_loader = ash.EnvironmentLoader(logger)
    return environment_loader.load_environment_settings()


def generate_urls(host: str) -> List[str]:
    """
    Generates and returns the list of URLs to fetch data from.

    Args:
        host (str): The host part of the URL.

    Returns:
        List[str]: List of URLs.
    """
    return [
        f"{host}/ivp/meters",
        f"{host}/ivp/meters/readings",
        f"{host}/api/v1/production",
        # f"{host}/ivp/pdm/energy",
        f"{host}/api/v1/production/inverters",
        f"{host}/ivp/livedata/status",
        f"{host}/ivp/meters/reports/consumption",
    ]
