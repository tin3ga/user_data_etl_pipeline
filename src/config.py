import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for the ETL pipeline.

    Attributes:
        URL (str): The URL to fetch user data from.
        JSON_FILE (str): The filename to save the raw user data in JSON format.
        CSV_FILE (str): The filename to save the transformed
        user data in CSV format.
        DATABASE_URL (str): The database connection URL,
        fetched from environment variables.
    """
    URL = 'https://dummyjson.com/users'
    JSON_FILE = 'user_data.json'
    CSV_FILE = 'transformed_user_data.csv'
    DATABASE_URL = os.getenv('DATABASE_URL')
