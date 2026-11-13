from selenium.webdriver.common.by import By


class MainPageLocators:

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    CONSTRUCTOR_AREA = (By.XPATH, "//span[contains(@class, 'BurgerConstructor_basket__listContainer')]")
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    ORDER_MODAL_CLOSE = (
        By.XPATH,
        "//section[.//h2[contains(@class, 'text_type_digits-large')]]//button[contains(@class, 'Modal_modal__close')]"
    )
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")