from math_func import add, mul


def test_add():
    assert add(7, 3) == 10
    assert add(8) == 10
    assert add(4) == 6
    # print("In addition test method")


def test_mul():
    assert mul(7, 4) == 28
    assert mul(7) == 21
    # print("In multiplication test method")
