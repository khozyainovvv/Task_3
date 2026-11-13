import time
import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_order_modal_opens(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_feed()
        order_feed_page.wait_for_feed_loaded()
        order_feed_page.click_first_order()

        assert order_feed_page.is_order_modal_visible() is True

    @allure.title("Созданный заказ отображается в «Ленте заказов»")
    def test_user_orders_in_feed(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_ingredient_by_drag_and_drop()
        main_page.click_place_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        time.sleep(1)

        assert order_number != "" and order_number != "9999"

        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_feed_loaded()

        assert order_feed_page.is_feed_not_empty() is True

    @allure.title("Счётчик «Выполнено за всё время» увеличивается при создании заказа")
    def test_total_orders_counter_increases(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_feed_loaded()

        counter_before = order_feed_page.get_total_orders_counter()

        main_page.click_constructor()
        time.sleep(1)
        main_page.add_ingredient_by_drag_and_drop()
        main_page.click_place_order()
        main_page.close_order_modal()
        time.sleep(1)

        main_page.click_order_feed()
        order_feed_page.wait_for_feed_loaded()
        counter_after = order_feed_page.get_total_orders_counter()

        assert counter_after > counter_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается при создании заказа")
    def test_today_orders_counter_increases(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_feed_loaded()

        counter_before = order_feed_page.get_today_orders_counter()

        main_page.click_constructor()
        time.sleep(1)
        main_page.add_ingredient_by_drag_and_drop()
        main_page.click_place_order()
        main_page.close_order_modal()
        time.sleep(1)

        main_page.click_order_feed()
        order_feed_page.wait_for_feed_loaded()
        counter_after = order_feed_page.get_today_orders_counter()

        assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, registered_user):
        login_page = LoginPage(driver)
        login_page.click_personal_account()
        login_page.login(registered_user["email"], registered_user["password"])
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_ingredient_by_drag_and_drop()
        main_page.click_place_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()
        time.sleep(1)

        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_for_feed_loaded()

        assert order_feed_page.is_order_in_progress(order_number) is True