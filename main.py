"""
Створіть декоратор retry який приймає першим аргументом число - кількість разів,
яку потрібно буде повторити виконання функції у разі викидання нею помилки.
"""
import time


def timeit(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання програми: {end-start}")
        return result
    return timer


@timeit
def hello(name="Anton"):
    time.sleep(1)
    print(f"Hello,{name} !")


hello()
