from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    FIRST_ORDER = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem')])[1]//a")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")