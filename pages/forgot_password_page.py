from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def fill_email(self, email):
        self.find_element(ForgotPasswordPageLocators.EMAIL_INPUT).send_keys(email)

    def click_restore(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def click_show_password(self):
        self.click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_input_active(self):
        element = self.find_element(ForgotPasswordPageLocators.PASSWORD_INPUT)
        return element.get_attribute("type") == "text"
    