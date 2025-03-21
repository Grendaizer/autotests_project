import pytest
import allure
from pages.login_page import LoginPage
import config
from utils.debug import save_debug_info_to_allure
from utils.logger import get_logger
from selenium.common.exceptions import TimeoutException

logger = get_logger((__name__))


@allure.feature("Login")
@allure.title("Успішний логін")
def test_login_success(driver):
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    logger.info("Відкрили сторінку логіну")

    try:
        login.login(config.USERNAME, config.PASSWORD)
        logger.info("Логін відправлений")

        assert "inventory" in driver.current_url, "Не потрапили на сторінку інвентарю"
        logger.info("Перевірка урла пройдена")
    except Exception as e:
        logger.error(f"Тест впав: {e}")
        save_debug_info_to_allure(driver, name="test_login_success")
        raise


@allure.feature("Login")
@allure.title("Невдалий логін з неправильними даними")
def test_login_fail(driver):
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    logger.info("Відкрили сторінку логіну")

    try:
        login.login("wrong_user", "wrong_pass")
        logger.info("Виконали логін з неправильними даними")

        error_text = login.get_text(LoginPage.ERROR_MSG)
        logger.info(f"Отримали повідомлення про помилку: {error_text}")

        assert "Epic sadface" in error_text, "Очікуване повідомлення не знайдено"
    except TimeoutException:
        logger.error("Не зʼявилось повідомлення про помилку логіну")
        save_debug_info_to_allure(driver, name="test_login_fail_timeout")
        pytest.fail("Повідомлення про помилку не зʼявилось!")
    except Exception as e:
        logger.error(f"Невідомий помилка під час логіну: {e}")
        save_debug_info_to_allure(driver, name="test_login_fail")
        raise
