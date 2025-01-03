import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    URL = 'https://dummyjson.com/users'
    JSON_FILE = 'user_data.json'
