"""
Створіть простий декоратор логування log_func,
який буде прінтити будь яке повідомлення перед визовом декорованої функції, та після.
"""


def log_func(func):
    def wrapper(*args, **kwargs):
        print("I`m going to greet you!")
        result = func(*args, **kwargs)
        print("Told you!")
        return result
    return wrapper()


@log_func
def hello(name="Anton"):
    print(f"Hello,{name} !")

