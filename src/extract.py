import sys
import json

import requests

from utils import setup_logger
from config import Config

logger = setup_logger(__name__)


def fetch_data():
    url = Config.URL

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        data = res.json()

        return data['users']
    except requests.exceptions.RequestException as e:
        logger.error(f'Request error occurred: {e}')
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f'JSON decode error occurred: {e}')
        sys.exit(1)


def main():
    logger.info(f'Fetching data from {Config.URL}')
    data = fetch_data()
    with open(file=Config.JSON_FILE, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    logger.info(f'Data saved to {Config.JSON_FILE}')


if __name__ == "__main__":
    main()
