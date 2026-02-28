import logging
import os
import yaml


def load_config():
    with open("configs/config.yaml") as f:
        return yaml.safe_load(f)


config = load_config()

LOG_FILE = config["logging"]["file"]

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log(message):
    print(message)
    logging.info(message)
