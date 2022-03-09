import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_2_mas_2(self):
        calc = Calculadora()
        self.assertEqual(4, calc.sumar(2, 2))

    def test_3_mas_2(self):
        calc = Calculadora()
        self.assertEqual(5, calc.sumar(3, 2))

    def test_3_menos_2(self):
        calc = Calculadora()
        self.assertEqual(1, calc.restar(3, 2))


if __name__ == '__main__':
    unittest.main()
