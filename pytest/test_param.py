import pytest


@pytest.mark.parametrize('num1, num2, result',[(2,8,10),(5,10,15),(8,8,16)])

def test_add(num1,num2,result):
    assert num1+num2==result