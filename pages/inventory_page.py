import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger("ui")

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Додаємо товар 'Sauce Labs Backpack' до кошика")
    def add_item_to_cart(self):
        logger.info("Додаємо товар 'Sauce Labs Backpack' до кошика")
        self.click(self.ADD_TO_CART_BTN)

    @allure.step("Переходимо до кошика")
    def go_to_cart(self):
        logger.info("Переходимо до кошика")
        self.click(self.CART_LINK)
