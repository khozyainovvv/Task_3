import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.click_forgot_password()

        assert "/forgot-password" in driver.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_submit_email_for_recovery(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.click_forgot_password()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.fill_email(registered_user["email"])
        forgot_page.click_restore()

        WebDriverWait(driver, 10).until(EC.url_contains("/reset-password"))
        assert "/reset-password" in driver.current_url

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_activates_input(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.click_forgot_password()

        forgot_page = ForgotPasswordPage(driver)
        forgot_page.fill_email(registered_user["email"])
        forgot_page.click_restore()

        WebDriverWait(driver, 10).until(EC.url_contains("/reset-password"))

        forgot_page.click_show_password()

        assert forgot_page.is_password_input_active() is True