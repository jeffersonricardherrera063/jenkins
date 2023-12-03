import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    #INICIO TEST SUMA
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # INICIO TEST DIVISION
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    #INICIO TEST METODO MULTIPLICACION
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "a", 2)
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 5, "m")

    # INICIO TEST RESTA
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(0, self.calc.substract(-1, -1))
        self.assertEqual(1, self.calc.substract(-1, -2))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "A", 10)
        self.assertRaises(TypeError, self.calc.substract, 10, "AS")

    # INICIO TEST POTENCIA
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(125, self.calc.power(5, 3))
        self.assertEqual(3600, self.calc.power(60, 2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, 0, 0)
        self.assertRaises(TypeError, self.calc.power, 0, -2)
        self.assertRaises(TypeError, self.calc.power, 10, "e")
        self.assertRaises(TypeError, self.calc.power, "c", 3)

    # INICIO TEST POTENCIA
    def test_logaritmo_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logaritmo(10))
        self.assertEqual(1.7781512503836436, self.calc.logaritmo(60))

    def test_logaritmo_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logaritmo, 0)
        self.assertRaises(TypeError, self.calc.logaritmo, -1)
        self.assertRaises(TypeError, self.calc.logaritmo, "e")

    # INICIO TEST RAIZ CUADRADA
    def test_raiz_cuadrada_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.raiz_cuadrada(9))
        self.assertEqual(1, self.calc.raiz_cuadrada(1))

    def test_raiz_cuadrada_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.raiz_cuadrada, -1)
        self.assertRaises(TypeError, self.calc.logaritmo, "e")

    # INICIO TEST FACTORIAL
    def test_factorial_method_returns_correct_result(self):
        self.assertEqual(120, self.calc.factorial(5))
        self.assertEqual(362880, self.calc.factorial(9))
        self.assertEqual(1, self.calc.factorial(1))

    def test_factorial_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.factorial, -1)
        self.assertRaises(TypeError, self.calc.factorial, 0)
        self.assertRaises(TypeError, self.calc.factorial, "e")

    # INICIO TEST SENO
    def test_seno_method_returns_correct_result(self):
        self.assertEqual(0.08715574274765817, self.calc.seno(5))
        self.assertEqual(0.03489949670250097, self.calc.seno(2))
        self.assertEqual(0.3420201433256687, self.calc.seno(20))

    def test_seno_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.seno, "e")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
