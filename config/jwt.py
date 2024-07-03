import os
import requests
from typing import Dict, Any
from config import ash


def login(user: str, password: str, logger) -> Dict[str, Any]:
    data = {"user[email]": user, "user[password]": password}
    logger.info("Attempting to login")
    try:
        response = requests.post("http://enlighten.enphaseenergy.com/login/login.json?", data=data)
        response.raise_for_status()
        logger.info("Login successful")
    except requests.RequestException as e:
        logger.error(f"API request failed during login: {e}")
        raise RuntimeError(f"API request failed: {e}")
    return response.json()


def fetch_token(response_data: Dict[str, Any], envoy_serial: str, user: str, logger) -> str:
    data = {
        "session_id": response_data["session_id"],
        "serial_num": envoy_serial,
        "username": user,
    }
    logger.info("Fetching token")
    try:
        response = requests.post("http://entrez.enphaseenergy.com/tokens", json=data)
        response.raise_for_status()
        logger.info("Token fetched successfully")
    except requests.RequestException as e:
        logger.error(f"API request failed during token fetch: {e}")
        raise RuntimeError(f"API request failed: {e}")
    return response.text


def configure_logger(log_path: str):
    logger_configurator = ash.LoggerConfigurator(log_path)
    return logger_configurator.logger


def load_settings(logger) -> Dict[str, str]:
    environment_loader = ash.EnvironmentLoader(logger)
    return environment_loader.load_environment_settings()


def save_token(token: str):
    print(token)
    print("Save token to .env file manually to use it without connecting to the internet for up to one year.")
    return token


def run():
    logdir = os.path.join("..", "log")
    logger = configure_logger(logdir)

    try:
        settings = load_settings(logger)
        response_data = login(settings["evun"], settings["evpw"], logger)
        token_raw = fetch_token(response_data, settings["evserial"], settings["evun"], logger)
        save_token(token_raw)
        return token_raw
    except KeyError as e:
        logger.error(f"Environment variable error: {e}")
        return 1
    except RuntimeError as e:
        logger.error(f"Runtime error: {e}")
        return 1
    except IOError as e:
        logger.error(f"Failed to write token to file: {e}")
        return 1


if __name__ == "__main__":
    run()
