import sys
import pandas as pd
from sqlalchemy import create_engine

from config import Config
from utils import setup_logger

logger = setup_logger(__name__)

_engine = None


def create_db_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(Config.DATABASE_URL)
    return _engine


def read_csv_data(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        logger.error("Error: Transformed data file not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logger.error("Error: Transformed data file is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        logger.error("Error: Parsing error while reading the transformed data file.")
        sys.exit(1)
    except pd.errors.DtypeWarning:
        logger.warning("Warning: Columns have mixed types.")
        df = pd.read_csv(file_name, dtype=str)
        return df


def load_to_postgres(engine, df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    logger.info(f"Data loaded into the table {table_name} successfully!")


def main():
    # Load the transformed data from the CSV file
    df = read_csv_data(Config.CSV_FILE)

    engine = create_db_engine()
    # Load the data into PostgreSQL
    load_to_postgres(engine, df, table_name='user_data')


if __name__ == "__main__":
    main()
