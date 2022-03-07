# https://docs.pytest.org/en/7.0.x/

#pytest

def func(x):
    return x*x

def test_func():
    assert func(3)==6
