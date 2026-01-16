from square import get_square


def test_sq():
    x = 3
    res = get_square(x)
    assert res == 9

def test_sq2():
    x = -5
    res = get_square(x)
    assert res == 25