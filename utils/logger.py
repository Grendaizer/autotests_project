import logging
import os
from config import BASE_DIR


def get_logger(name: str = "main") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_dir = os.path.join(BASE_DIR, "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Динамічний файл по типу логера
    log_path = os.path.join(log_dir, f"{name}.log")

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(name)s — %(message)s")

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger
