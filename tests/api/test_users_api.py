import requests
import allure
from utils.logger import get_logger

logger = get_logger(__name__)


@allure.feature("API")
@allure.title("Отримання користувачів")
def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    logger.info(f"GET {url}")

    with allure.step(f"Відправляємо GET {url}"):
        r = requests.get(url)

    allure.attach(str(r.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
    allure.attach(r.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

    logger.info(f"Status: {r.status_code}")
    logger.info(f"Response: {r.text}")

    assert r.status_code == 200
    assert r.json()["page"] == 2


@allure.feature("API")
@allure.title("Створення користувача")
def test_create_user():
    url = "https://reqres.in/api/users"
    data = {"name": "morpheus", "job": "leader"}

    logger.info(f"POST {url} | payload: {data}")

    with allure.step(f"Відправляємо POST {url}"):
        r = requests.post(url, json=data)

    allure.attach(str(r.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
    allure.attach(r.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

    logger.info(f"Status: {r.status_code}")
    logger.info(f"Response: {r.text}")

    assert r.status_code == 201
    assert r.json()["name"] == "morpheus"
