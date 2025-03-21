import os
import shutil
import subprocess
import zipfile
import pytest
import requests
from config import BASE_DIR, HEADLESS, BOT_TOKEN, ALLURE_RESULTS_DIR, ALLURE_CLI, CHAT_IDS
from selenium import webdriver



def pytest_sessionstart(session):
    print("Очищаємо логи та результати перед запуском...")
    folders = [
        os.path.join(BASE_DIR, "logs"),
        os.path.join(BASE_DIR, "allure-results"),
        os.path.join(BASE_DIR, "allure-report")
    ]

    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)  # Видаляє папку зі всім вмістом
                os.makedirs(folder)  # Заново створюємо чисту папку
            except Exception as e:
                print(f"Не вдалося видалити {folder}: {e}")

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_sessionfinish(session, exitstatus):
    report_dir = os.path.join(os.path.dirname(__file__), 'allure-report')
    zip_path = os.path.join(os.path.dirname(__file__), 'allure-report.zip')

    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

    subprocess.run([ALLURE_CLI, 'generate', ALLURE_RESULTS_DIR, '-o', report_dir, '--clean'], check=True)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(report_dir):
            for file in files:
                path = os.path.join(root, file)
                rel = os.path.relpath(path, report_dir)
                zipf.write(path, rel)

    for chat_id in CHAT_IDS:
        with open(zip_path, 'rb') as f:  # Відкриваємо файл окремо для кожного запиту
            r = requests.post(
                f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument',
                data={'chat_id': chat_id},
                files={'document': f}
            )
            if r.status_code == 200:
                print(f"Звіт надіслано користувачу {chat_id}")
            else:
                print(f"Помилка для {chat_id}: {r.status_code} {r.text}")
