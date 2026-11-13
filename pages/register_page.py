from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage

class RegisterPage(BasePage):

    def fill_name(self, name):
        self.find_element(RegisterPageLocators.NAME_INPUT).send_keys(name)

    def fill_email(self, email):
        self.find_element(RegisterPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.find_element(RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_register(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    def click_login_link(self):
        self.click(RegisterPageLocators.LOGIN_LINK)
        