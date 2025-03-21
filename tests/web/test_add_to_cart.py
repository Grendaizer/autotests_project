import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import config
from utils.debug import save_debug_info_to_allure
from utils.logger import get_logger

logger = get_logger((__name__))


@allure.feature("Cart")
@allure.title("Додавання товару до кошика")
def test_add_item_to_cart(driver):
    login = LoginPage(driver)

    try:
        login.open(config.BASE_URL)
        logger.info("Відкрили сторінку логіну")

        login.login(config.USERNAME, config.PASSWORD)
        logger.info("Успішно залогінились")

        inventory = InventoryPage(driver)

        inventory.add_item_to_cart()
        logger.info("Додали товар до кошика")

        inventory.go_to_cart()
        logger.info("Перейшли до кошика")

        assert "cart" in driver.current_url, "Не потрапили на сторінку кошика"
        logger.info("Перевірка урла пройдена")

    except Exception as e:
        logger.error(f"Тест на додавання до кошика впав: {e}")
        save_debug_info_to_allure(driver, name="test_add_item_to_cart")
        raise
