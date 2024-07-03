import os
import time
import sys
from typing import Any, Dict, Literal
from logging import Logger
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from requests.models import Response
import call_panels as ash


def fetch_and_process_data(settings: Dict[str, Any], logger: Logger) -> None:
    """
    Fetch data from URLs and process the responses.

    Args:
        settings (dict): Environment settings.
        logger (Logger): Logger for logging.
    """
    host: Any = settings["iq_gateway"]
    token_code: str | Literal[1] = ash.read_token()

    data_fetcher = ash.DataFetcher(logger)
    urls: ash.List[str] = ash.generate_urls(host)
    headers: Dict[str, str] = {"Accept": "application/json", "Authorization": f"Bearer {token_code}"}
    responses: ash.List[Response] = data_fetcher.fetch_data(urls, headers, timeout=60)
    timestamp = int(time.time())

    data_fetcher.process_responses(responses, urls, timestamp, os.path.join(os.pardir, "log", "grid"))


def main():
    """
    Main function to orchestrate the fetching and processing of data.
    """
    logdir: str = os.path.join(os.pardir, "log", "grid")
    logger: Logger = ash.initialize_logger(logdir)
    settings: dict = ash.load_environment_settings(logger)

    fetch_and_process_data(settings, logger)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        try:
            future.result(timeout=120)
        except TimeoutError:
            print("Process took longer than 120 seconds. Exiting.")
            sys.exit(1)
