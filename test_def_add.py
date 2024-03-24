import pytest


# Пример функции, которую мы будем тестировать
def add(a, b):
    return a + b


# Тестирование функции с использованием PyTest
def test_add_positive_positive():
    assert add(3, 5) == 8


def test_add_negative_positive():
    assert add(-3, 5) == 2


def test_add_negative_negative():
    assert add(-3, -5) == -8


def test_add_positive_zero():
    assert add(5, 0) == 5


def test_add_negative_zero():
    assert add(-5, 0) == -5


def test_add_zero_zero():
    assert add(0, 0) == 0


def test_add_int_string():
    with pytest.raises(TypeError):
        add(5, "string")


def test_addition_with_one_argument():
    with pytest.raises(TypeError):
        add(5)


def test_addition_with_3_argument():
    with pytest.raises(TypeError):
        add(5, 6, 3)
