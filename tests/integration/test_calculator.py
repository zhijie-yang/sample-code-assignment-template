import pytest

from src.math.calculator import Calculator as C


class TestCalculatorIntegration:
    def test_complex_operations(self):
        result = C.add(5, 3)
        result = C.subtract(result, 2)
        result = C.multiply(result, 4)
        result = C.divide(result, 2)
        assert result == 12.0
