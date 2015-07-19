import unittest
from src.tax_calculator import TaxCalculator

__author__ = 'krzysztofduda'


class TestTaxCalculator(unittest.TestCase):
    def test_calculateTax_first_grade(self):
        tax = TaxCalculator()
        self.assertEquals(tax.calculateTax(1000), [0.0])

    def test_calculateTax_second_grade(self):
        tax1 = TaxCalculator()
        self.assertEquals(tax1.calculateTax(3000), [150])

    def test_calculateTax_third_grade(self):
        tax1 = TaxCalculator()
        self.assertEquals(tax1.calculateTax(5001), [500.1])
