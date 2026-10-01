import pytest
from toolkit.convert import change
from toolkit.convert import convErr as err

def test1():
    assert change('m', 'cm', 12.1) == 1210
def test2():
    assert change('k', 'c', 115) == -158.15
def test3():
    assert change('g', 'kg', 115500) == 115.5
def test4():
    assert change('k', 'f', 12) == -438.07
def test5():
    assert change('m', 'km', 1478) == 1.48 #с округлением,а так 1.478
def test6():
    assert change('mm', 'km', 1231215) == 1.23 # с округлением тоже
def test7():
    assert change('kg', 'g', 0.356) == 356

def test_1():
    with pytest.raises(err):
        change('k','c', -1) #ниже нуля
def test_2():
    with pytest.raises(err):
        change('c','k', -273.15) #ниже нуля
def test_3():
    with pytest.raises(err):
        change('f','c', -460) 
def test_4():
    with pytest.raises(err):
        change('km', 'm', -5.5)
def test_5():
    with pytest.raises(err):
        change('g', 'kg', -1300)
