import sys
import json
import pandas as pd

from config import Config
from utils import setup_logger

logger = setup_logger(__name__)


def load_data(file_name: str):
    try:
        with open(file=file_name, mode='r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        logger.error(f'Eroor loading file {file_name}')
        sys.exit(1)


def transform_data(data):
    try:
        df = pd.DataFrame(data)

        df = df[['id', 'firstName', 'lastName', 'age', 'gender', 'email',
                 'phone', 'username', 'password', 'birthDate', 'image', 'bloodGroup',
                 'height', 'weight', 'eyeColor', 'hair', 'ip', 'macAddress',
                 'ein', 'ssn', 'role']]
        df.dropna()
        return df
    except Exception as e:
        logger.error(f"An error occurred during data transformation: {e}")
        sys.exit(1)


def main():
    data = load_data(file_name=Config.JSON_FILE)
    transformed_df = transform_data(data=data)
    transformed_df.to_csv(Config.CSV_FILE, index=False)
    logger.info(f'Data saved to {Config.CSV_FILE}')


if __name__ == "__main__":
    main()
