import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers.api_client import StellarBurgersApi

BASE_URL = "https://qa-stellarburgers.education-services.ru"

class WebdriverFactory:

    @staticmethod
    def get_webdriver(browser_name: str):
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")



def generate_random_email() -> str:
    return f"test_{random.randint(100000, 999999)}@yandex.ru"


def generate_random_password() -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))



def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
    )


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = WebdriverFactory.get_webdriver(browser_name)
    browser.maximize_window()
    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    return {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "name": "Test User"
    }


@pytest.fixture
def registered_user(user_data):
    response = StellarBurgersApi.register_user(
        user_data["email"], user_data["password"], user_data["name"]
    )
    response.raise_for_status()
    data = response.json()

    yield {
        **user_data,
        "accessToken": data["accessToken"],
        "refreshToken": data["refreshToken"]
    }

    StellarBurgersApi.delete_user(data["accessToken"])
    