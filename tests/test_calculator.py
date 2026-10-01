import pytest
from toolkit.calculator import calc
from toolkit.calculator import CalcErr as err


# хорошие тесты


def test_addition():
    assert calc("2 + 3") == 5


def test_subtraction():
    assert calc("10 - 4") == 6


def test_multiplication():
    assert calc("3 * 7") == 21


def test_division():
    assert calc("15 / 3") == 5


def test_priority():
    assert calc("2 + 3 * 4") == 14
    assert calc("10 - 6 / 2") == 7


def test_unary_minus():
    assert calc("-5 + 5") == 0
    assert calc("3 + -2") == 1
    assert calc("-3 * -4") == 12


def test_unary_plus():
    assert calc("+5") == 5
    assert calc("+3 + +2") == 5


def test_floats():
    assert calc("1.5 + 2.5") == 4.0
    assert calc("3.0 * 2.5") == 7.5


def test_spaces_ignored():
    assert calc("  2+3  ") == 5
    assert calc("10   -   4") == 6


def test_complex_expression():
    assert calc("2 + 3 * 4 - 6 / 2") == 11


# плохие тесты

def test_empty():
    with pytest.raises(err):
        calc("")


def test_spaces():
    with pytest.raises(err):
        calc("   ")


def test_character():
    with pytest.raises(err):
        calc("2 + a")


def test_missing():
    with pytest.raises(err):
        calc("2 +")


def test_two():
    with pytest.raises(err):
        calc("2 + * 3")


def test_zero():
    with pytest.raises(err):
        calc("5 / 0")


def test_start():
    with pytest.raises((err, IndexError)):
        calc("* 5")