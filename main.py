"""
Створіть декоратор **`rate_limit`**, який обмежує кількість викликів
декорованої функції протягом певного періоду часу.
Декоратор повинен приймати два параметри `max_calls` та `period`.
Перший парметр - максимальна кількість допустимих викликів функції.
Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls` викликів.
"""
import time


def rate_limit(max_calls=1, period=10):
    last_called = None
    calls = 0

    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            nonlocal last_called, calls

            current_time = time.time()

            if last_called is None or current_time - last_called >= period:
                calls = 0
                last_called = current_time

            if calls < max_calls:
                result = func(*args, **kwargs)
                calls += 1
                return result
            else:
                return "Rate limit exceeded. Please wait."

        return inner_wrapper

    return wrapper


@rate_limit(max_calls=2, period=10)
def limited_function():
    return "Function executed."


for _ in range(5):
    print(limited_function())
    time.sleep(0.5)

