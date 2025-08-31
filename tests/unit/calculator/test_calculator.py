import pytest

from src.math.calculator import Calculator as C


class TestCalculator:
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (-1, -1, -2),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-1.5, 1.5, 0.0),
        ],
    )
    def test_add(self, a, b, expected):
        assert C.add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 1, 1),
            (-1, -1, 0),
            (0, 0, 0),
            (2.5, 1.5, 1.0),
            (-1.5, 1.5, -3.0),
        ],
    )
    def test_subtract(self, a, b, expected):
        assert C.subtract(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 6),
            (-1, -1, 1),
            (0, 10, 0),
            (2.5, 2.0, 5.0),
            (-1.5, 2.0, -3.0),
        ],
    )
    def test_multiply(self, a, b, expected):
        assert C.multiply(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (6, 3, 2.0),
            (-4, -2, 2.0),
            (5.0, 2.0, 2.5),
            (-4.5, -1.5, 3.0),
        ],
    )
    def test_divide(self, a, b, expected):
        assert C.divide(a, b) == expected

    @pytest.mark.parametrize(
        "a, b",
        [
            (1, 0),
            (-1, 0),
            (0, 0),
        ],
    )
    def test_divide_by_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            C.divide(a, b)
