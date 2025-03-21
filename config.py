import os
import shutil
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "allure-results")
ALLURE_CLI = shutil.which("allure")

BOT_TOKEN = os.getenv("BOT_TOKEN", "default_token")  # Безпечний дефолт
CHAT_IDS = [chat_id.strip() for chat_id in os.getenv("CHAT_IDS", "").split(",")] # Парсимо в список
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


