# coding=utf-8
from src.Calculator import Calculator
import pytest


class TestCalculator:

    @pytest.fixture(scope="session")
    def setup_calculator(self):
        print("Calculator initialize")
        return Calculator()

    def test_addition(self, setup_calculator):
        # self.calculator = Calculator()
        assert Calculator.addition(2, 1) == 3

    def test_subtraction(self, setup_calculator):
        assert Calculator.subtraction(2, 3) == -1

    def test_multiplication(self, setup_calculator):
        assert Calculator.multiplication(1.5, 1.5) == 2.25

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_divide(self, setup_calculator):
        assert Calculator.divide(0.3, 0.1) == 3.0

    def test_sum(self, setup_calculator):
        assert Calculator.sum(1, 2, 3) == 6

    @staticmethod
    def tear_down(self):
        print("tear down")

    @staticmethod
    def teardown_class(self):
        print("teardown class")