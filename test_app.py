import pytest
import calculatrice

def test_addition():
    assert calculatrice.addition(2, 4) == 6
    assert calculatrice.addition(-1, 1) == 0
    assert calculatrice.addition(0, 0) == 0
    assert calculatrice.addition(-1, -1) == -2
    assert calculatrice.addition(1.5, 2.5) == 4.0

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 6),
    (-1, 1, 0),
    (0, 0, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4.0)
])
def test_addition_parametrized(a, b, expected):
    assert calculatrice.addition(a, b) == expected

if __name__ == "__main__":
    pytest.main()