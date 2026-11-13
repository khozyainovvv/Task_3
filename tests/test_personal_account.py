import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.account_page import AccountPage
from pages.login_page import LoginPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])

        login_page.click_personal_account()

        assert "/account" in driver.current_url

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])

        login_page.click_personal_account()
        account_page = AccountPage(driver)
        account_page.click_order_history()

        assert "/account/order-history" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])

        login_page.click_personal_account()
        account_page = AccountPage(driver)
        account_page.click_logout()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url