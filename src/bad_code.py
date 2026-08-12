def add(a, b):
    return a + b


def unused_function():
    x = 123
    y = 456
    return x * y


print(add(1, 2))


def bad():
    x = 1
    return x / 0


def bad1():
    return 1 / 0
