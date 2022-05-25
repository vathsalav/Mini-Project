
from calculatorInterface.calculator_interface import CalculatorInterface


class CalculatorImplementation(CalculatorInterface):
    def addition(self, number1, number2):
        if isinstance(number1, int) and isinstance(number2, int):  # this line is checking the input types
            if number1 > 0 and number2 > 0:  # this line checks that we are working with positive numbers
                return number1 + number2
            else:
                return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
        else:
            return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types

    def subtraction(self, number1, number2):
        if isinstance(number1, int) and isinstance(number2, int):  # this line is checking the input types
            if number1 > 0 and number2 > 0:  # this line checks that we are working with positive numbers
                return number1 - number2
            else:
                return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
        else:
            return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types

    def multiplication(self, number1, number2):
        if isinstance(number1, int) and isinstance(number2, int):  # this line is checking the input types
            if number1 > 0 and number2 > 0:  # this line checks that we are working with positive numbers
                return number1 * number2
            else:
                return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
        else:
            return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types

    def division(self, number1, number2):
        try:
            if isinstance(number1, int) and isinstance(number2, int):  # this line is checking the input types

                if number1 >= 0 and number2 >= 0:  # this line checks that we are working with positive numbers
                    return number1 / number2
                else:
                    return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
            else:
                return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types
        except ZeroDivisionError:
            return "You can't divide by zero"

    def round(self, number):
        if isinstance(number, float):  # this line is checking the input types
            if number > 0:  # this line checks that we are working with positive numbers
                return round(number)
            else:
                return "bad input: please only enter mixed positive numbers"
        else:
            return "bad input: please only enter mixed positive numbers"
