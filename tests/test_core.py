from hello_app.core import add


def test_BasicAddition() -> None:
    assert add(2, 3) == 5


def test_NegativeAddition() -> None:
    assert add(-4, -1) == -5
