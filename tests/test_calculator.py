import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator()

    def test_adding_success(self):
        assert self.calculator.adding(1, 1) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(2, 1) == 1

    def test_division_success(self):
        assert self.calculator.division(4, 2) == 2

    def test_multiply_success(self):
        assert self.calculator.multiply(2, 2) == 4

    def teardown(self):
        print('Выполнение метода Teardown')

