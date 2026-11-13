import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_ingredient(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)

    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL))

    def close_order_modal(self):
        close_button = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL_CLOSE)
        )
        for _ in range(5):
            try:
                close_button.click()
                break
            except Exception:
                time.sleep(1)
        self.wait.until(
            EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)
        )

    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    def add_ingredient_by_drag_and_drop(self):
        source = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.FIRST_INGREDIENT)
        )
        target = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
        )
        self.driver.execute_script("""
            function createEvent(type) {
                let event = document.createEvent('CustomEvent');
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) { this.data[type] = val; },
                    getData: function(type) { return this.data[type]; }
                };
                return event;
            }
            arguments[0].dispatchEvent(createEvent('dragstart'));
            arguments[1].dispatchEvent(createEvent('dragenter'));
            arguments[1].dispatchEvent(createEvent('dragover'));
            arguments[1].dispatchEvent(createEvent('drop'));
        """, source, target)
        time.sleep(2)

    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number_from_modal(self):
        def number_is_real(driver):
            try:
                element = driver.find_element(*MainPageLocators.ORDER_NUMBER_MODAL)
                text = element.text.strip()
                if text and text != "9999":
                    return text
            except Exception:
                pass
            return False

        return self.wait.until(number_is_real)
    