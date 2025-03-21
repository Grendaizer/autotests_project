import allure
from config import DEBUG


def save_debug_info_to_allure(driver, name="debug"):
    if DEBUG:
        try:
            allure.attach(driver.get_screenshot_as_png(),
                          name=f"{name}_screenshot",
                          attachment_type=allure.attachment_type.PNG)

            allure.attach(driver.page_source,
                          name=f"{name}_html",
                          attachment_type=allure.attachment_type.HTML)
        except Exception as e:
            print(f"[DEBUG ATTACH ERROR] {e}")
