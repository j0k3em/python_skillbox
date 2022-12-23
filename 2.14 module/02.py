import time
from typing import Callable, Any

def freeze(func: Callable) -> Any:
    """
    Декоратор, замедляющий работу функции на 5 сек.
    """

    def wrapped_func():
        time.sleep(5)
        func()

    return wrapped_func

@freeze
def test():
    print('<Тут что-то происходит...>')


test()