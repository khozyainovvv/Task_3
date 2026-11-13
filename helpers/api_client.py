import requests

BASE_URL = "https://qa-stellarburgers.education-services.ru/api"

class StellarBurgersApi:

    @staticmethod
    def register_user(email: str, password: str, name: str) -> requests.Response:
        return requests.post(
            f"{BASE_URL}/auth/register",
            json={"email": email, "password": password, "name": name}
        )

    @staticmethod
    def login_user(email: str, password: str) -> requests.Response:
        return requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password}
        )

    @staticmethod
    def delete_user(access_token: str) -> requests.Response:
        return requests.delete(
            f"{BASE_URL}/auth/user",
            headers={"Authorization": access_token}
        )