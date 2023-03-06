from typing import Any

import requests
from requests import Response

from test_framework.helpers.log import my_log
from test_framework.helpers.report import allure_attach_response


class BaseRequests:
    def __init__(self) -> None:
        self.headers: dict = {"Content-Type": "application/json"}
        self.logger = my_log()

    def get(self, url: str, headers: dict = None) -> Response:
        return self._api_call("GET", url=url, headers=headers)

    def patch(self, url: str, headers: dict = None, json: dict = None) -> Response:
        return self._api_call("PATCH", url=url, headers=headers, json=json)

    def post(self, url: str, headers: dict = None, json: dict = None) -> Response:
        return self._api_call("POST", url=url, headers=headers, json=json)

    def put(self, url: str, headers: dict = None, json: dict = None) -> Response:
        return self._api_call("PUT", url=url, headers=headers, json=json)

    def update_headers(self, headers: dict) -> None:
        if headers is not None:
            for key, item in headers.items():
                self.headers[key] = item

    def _api_call(self, method: Any, url: str, headers: Any, json: dict = None) -> Any:
        try:
            return self._request(method, url, headers=headers, json=json)
        except Exception as error:
            self.logger.error(f"***<ERROR>: {error}\n ***")
        return None

    @allure_attach_response
    def _request(self, method: Any, url: str, headers: Any, json: dict = None) -> Response:
        self.update_headers(headers)
        return requests.request(method, url, headers=self.headers, json=json)
