import unittest
from unittest.mock import patch
from app import add, subtract, multiply, divide, percentage, calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertIsNone(divide(5, 0))

    def test_percentage(self):
        self.assertEqual(percentage(50, 100), 50)
        self.assertEqual(percentage(25, 50), 50)
        self.assertEqual(percentage(0, 10), 0)
        self.assertEqual(percentage(10, 0), "Error! Division by zero.")

    @patch('builtins.input', side_effect=['1', '10', '5'])
    @patch('builtins.print')
    def test_calculator_add(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: 15.0")

    @patch('builtins.input', side_effect=['2', '10', '5'])
    @patch('builtins.print')
    def test_calculator_subtract(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: 5.0")

    @patch('builtins.input', side_effect=['3', '10', '5'])
    @patch('builtins.print')
    def test_calculator_multiply(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: 50.0")

    @patch('builtins.input', side_effect=['4', '10', '5'])
    @patch('builtins.print')
    def test_calculator_divide(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: 2.0")

    @patch('builtins.input', side_effect=['5', '50', '100'])
    @patch('builtins.print')
    def test_calculator_percentage(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: 50.0%")

    @patch('builtins.input', side_effect=['4', '10', '0'])
    @patch('builtins.print')
    def test_calculator_divide_by_zero(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("The result is: None")

    @patch('builtins.input', side_effect=['6'])
    @patch('builtins.print')
    def test_calculator_invalid_choice(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("Invalid input. Please try again.")

    @patch('builtins.input', side_effect=['1', 'ten', '5'])
    @patch('builtins.print')
    def test_calculator_invalid_number(self, mock_print, mock_input):
        calculator()
        mock_print.assert_any_call("Invalid input! Please enter numeric values.")

if __name__ == '__main__':
    unittest.main()