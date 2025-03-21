import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger("ui")

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    @allure.step("Логінимось з юзером: {username}")
    def login(self, username, password):
        self._enter_username(username)
        self._enter_password(password)
        self._click_login()

    @allure.step("Вводимо логін: {username}")
    def _enter_username(self, username):
        logger.info(f"Вводимо логін: {username}")
        self.type(self.USERNAME_INPUT, username)

    @allure.step("Вводимо пароль: ***")
    def _enter_password(self, password):
        logger.info(f"Вводимо пароль: ***")
        self.type(self.PASSWORD_INPUT, password)

    @allure.step("Натискаємо кнопку 'Login'")
    def _click_login(self):
        logger.info(f"Натискаємо кнопку 'Login'")
        self.click(self.LOGIN_BUTTON)
