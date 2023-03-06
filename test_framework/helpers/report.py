import functools
from typing import Any, Callable, cast

import allure


def _decode_possible_body(response) -> Any:
    """Метод для парсинга payload который отправляется rest в запросах"""
    try:
        # По умолчанию байтовая строка
        return response.request.body.decode("utf-8")  # type: ignore
    except AttributeError:
        return response.request.body  # В случае GET запроса вернется None
    except UnicodeDecodeError:
        return "Content cannot be displayed because of UnicodeDecodeError"


def allure_attachment_new(entity: Any) -> None:
    """Результат идет в allure"""
    endpoint = entity.url
    request_body = _decode_possible_body(entity)
    status_code = str(entity.status_code)
    response = entity.text
    string = response.replace("<", "&lt;")
    response = string.replace(">", "&gt;")
    attachment = (
        """
                        <p><strong>Endpoint:</strong> {}</p>
                        <p><strong>Payload:</strong> {}</p>
                        <p><strong>Status_code:</strong>&nbsp;{}</p>
                        <p><strong>Response:</strong> {}</p>
                  """
    ).format(endpoint, request_body, status_code, response)
    allure.attach(attachment, "entity_response", allure.attachment_type.HTML)


def allure_attach_response(method: Callable) -> Callable:
    """Decorator to attach returning response from any function/method to allure."""

    @functools.wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        response = cast(Any, method(self, *args, **kwargs))
        allure_attachment_new(response)
        return response

    return wrapper
