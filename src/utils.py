import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def setup_logger(name: str) -> logging.Logger:
    lgr = logging.getLogger(name)
    return lgr
