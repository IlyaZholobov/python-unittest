from unittest import TestCase
import unittest
from calc import calc_sting


class CalcTest(TestCase):

    def test_plus(self):
        self.assertEqual(calc_sting('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calc_sting('2-2'), 0)

    def test_multiple(self):
        self.assertEqual(calc_sting('2*4'), 8)

    def test_divine(self):
        self.assertEqual(calc_sting('4/2'), 2)

    def test_no_empty_string(self):
        with self.assertRaises(ValueError) as e:
            calc_sting('')
        self.assertEqual(e.exception.args[0], 'Пустая строка')

    def test_only_int(self):
        with self.assertRaises(ValueError) as e:
            calc_sting('2+3.4')
        self.assertEqual(e.exception.args[0],
                         'два числа тип инт и один знак операции')

    def test_only_one_sign(self):
        with self.assertRaises(ValueError) as e:
            calc_sting('2++34')
        self.assertEqual(e.exception.args[0],
                         'два числа тип инт и один знак операции')


if __name__ == '__main__':
    unittest.main()