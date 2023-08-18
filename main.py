"""
Реалізувати декоратор кешування memorize, який кешує результати декорованої функції
для покращення продуктивності при повторних викликах з тими самими аргументами.
Тобто він повинен запамʼятовувати аргументи з якими функція визивалась і результат роботи функції з цими аргументами.
І у випадку, якщо ми вже маємо результат для цих аргументів,
просто повернути закешований результат, замість виклику функції.
"""


def memorize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Returning cached result:")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating...")
            return result

    return wrapper


@memorize
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(5, 7))
print(sum_of_numbers(5, 7))


