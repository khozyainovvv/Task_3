from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def fill_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def click_register(self):
        self.click(LoginPageLocators.REGISTER_LINK)
        