import functools
import time
from typing import Any, Type

from test_framework.helpers.log import my_log
from test_framework.helpers.main_checkers import WaitException

logger = my_log()


def step_waiter(timeout: int = 0, wait_interval: int = 0, wait_exceptions: Type[BaseException] = WaitException) -> Any:
    def _wait(step: Any) -> Any:

        step_name = step.__name__.split(".")[-1]

        @functools.wraps(step)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            wait_until = int(time.time()) + timeout

            while wait_until > time.time():
                try:
                    return step(*args, **kwargs)
                except wait_exceptions:
                    logger.info(f"Waiting for {step_name}")
                    time.sleep(wait_interval)
            return step(*args, **kwargs)

        return wrapper

    return _wait
