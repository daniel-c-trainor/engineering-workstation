from src.bad_code import add, bad, bad1


def test_add():
    assert add(2, 3) == 5


def test_bad():
    try:
        bad()
    except ZeroDivisionError:
        pass


def test_bad1():
    try:
        bad1()
    except ZeroDivisionError:
        pass
