__author__ = 'krzysztofduda'


class TaxCalculator():
    def __init__(self):
        self.keys = [0.0, 0.05, 0.1]
        self.values = [1000, 5000, 10000]
        self.brackets = {0.0: (0, 1000), 0.05: (1001, 5000), 0.1: (5001, 10000)}

    def calculateTax(self, salary=None):
        self.salary = salary
        tax = [(self.salary * x) for x in self.keys if (self.salary <= self.brackets.get(x)[1]and self.salary >=self.brackets.get(x)[0])]
        return tax