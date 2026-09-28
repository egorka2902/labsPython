import pytest
from toolkit.convert import change
from toolkit.convert import convErr as err

def test1():
    assert change('m', 'cm', 12.1) == 1210