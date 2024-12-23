# API-клиенты — для отправки запросов.
import requests
from playwright.async_api import Page
from requests.auth import HTTPBasicAuth
from typing import Dict


class ApiClient:
    def __init__(self, page: Page, base_url: str, auth_credentials: tuple):
        self.page = page
        self.base_url = base_url
        self.auth_credentials = auth_credentials

    def _send_request(
        self,
        method: str,
        endpoint: str,
        email: str = None,
        data: Dict = None,
        params: Dict = None,
    ):
        # Формирование URL с учетом email, если он передан
        url = f"{self.base_url}{endpoint}"
        if email:
            url = f"{url}{email}/"  # Добавление email в конец URL для всех запросов, кроме POST

        headers = {"Content-Type": "application/json"}
        response = None

        # Выбор метода запроса и отправка
        if method == "POST":
            response = requests.post(
                url,
                json=data,
                auth=HTTPBasicAuth(*self.auth_credentials),
                headers=headers,
            )
        elif method == "GET":
            response = requests.get(
                url,
                params=params,
                auth=HTTPBasicAuth(*self.auth_credentials),
                headers=headers,
            )
        elif method == "PUT":
            response = requests.put(
                url,
                json=data,
                auth=HTTPBasicAuth(*self.auth_credentials),
                headers=headers,
            )
        elif method == "DELETE":
            response = requests.delete(
                url, auth=HTTPBasicAuth(*self.auth_credentials), headers=headers
            )

        # Проверка успешности запроса
        if response.status_code in [200, 201, 204]:
            return response.json() if response.status_code != 204 else None
        else:
            raise Exception(f"Request failed: {response.status_code} - {response.text}")

    def post(self, endpoint: str, data: Dict):
        """POST-запрос."""
        return self._send_request("POST", endpoint, data=data)

    def get(self, endpoint: str, email: str, params: Dict = None):
        """GET-запрос."""
        return self._send_request("GET", endpoint, email=email, params=params)

    def put(self, endpoint: str, email: str, data: Dict):
        """PUT-запрос."""
        return self._send_request("PUT", endpoint, email=email, data=data)

    def delete(self, endpoint: str, email: str):
        """DELETE-запрос."""
        return self._send_request("DELETE", endpoint, email=email)
