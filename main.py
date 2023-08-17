"""
Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його.
Для отримання часу роботи скористуйтесь модулем time і функцією time.time()
"""
import time


def timeit(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання програми: {end-start}")
        return result
    return timer()


@timeit
def hello(name="Anton"):
    time.sleep(1)
    print(f"Hello,{name} !")

