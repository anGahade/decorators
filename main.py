"""
Створіть декоратор retry який приймає першим аргументом число - кількість разів,
яку потрібно буде повторити виконання функції у разі викидання нею помилки.
"""
import time


def retry(n):
    def decorator(func):
        def once_more(*args, **kwargs):
            retries = 0
            while n != retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error: {e}. Retrying......")
                    time.sleep(1)
                    retries += 1
        return once_more
    return decorator


@retry(2)
def error_func():
    print(1/0)


error_func()
