import os
import shutil

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

BOT_TOKEN = '7184559035:AAFrvmZ8kEZwPDkp2WtpqZnyKGkzn9aFtvY'
CHAT_IDS = ['452864527', '462107859']  # Список Telegram ID

HEADLESS = True
DEBUG = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "allure-results")
ALLURE_CLI = shutil.which("allure")


