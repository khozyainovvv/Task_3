import allure
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        main_page.click_constructor()

        assert "/" in driver.current_url
        assert "order-feed" not in driver.current_url

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()

        assert "/feed" in driver.current_url

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible() is True

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_visible() is False

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        counter_before = main_page.get_ingredient_counter()
        main_page.add_ingredient_by_drag_and_drop()
        time.sleep(2)
        counter_after = main_page.get_ingredient_counter()

        assert counter_after > counter_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])

        main_page = MainPage(driver)
        main_page.add_ingredient_by_drag_and_drop()
        main_page.click_place_order()

        order_number = main_page.get_order_number_from_modal()

        assert order_number != ""
        