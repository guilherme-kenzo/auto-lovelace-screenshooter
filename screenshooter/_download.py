import os
import requests
import tarfile
from loguru import logger
from .config import GECK_URL, BASE_DIR


def download_driver_if_not_exists() -> bool:
    """Downloads the geckodriver if it doesn't exist.

    Returns:
        bool: True if either the driver already existed or if it was successfully downloaded. False otherwise.
    """
    if os.path.isfile(os.path.join(BASE_DIR, "geckodriver")):
        return True
    try:
        file_path = _download_driver()
        _extract_driver(file_path)
    except Exception as e:  # TK - specify exceptions
        logger.error(e)
        return False
    return True


def _download_driver() -> str:
    r = requests.get(GECK_URL, stream=True)
    f_path = os.path.join(BASE_DIR, "geckodriver.tar.gz")
    with open(f_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return f_path


def _extract_driver(file_path: str) -> None:
    file = tarfile.open(file_path, "r:gz")
    file.extractall(BASE_DIR)
    file.close()
