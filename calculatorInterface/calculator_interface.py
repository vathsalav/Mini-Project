from abc import ABC, abstractmethod

class CalculatorInterface(ABC):

    @abstractmethod
    def addition(self, number1, number2):
        pass

    @abstractmethod
    def subtraction(self, number1, number2):
        pass

    @abstractmethod
    def multiplication(self, number1, number2):
        pass

    @abstractmethod
    def division(self, number1, number2):
        pass

    @abstractmethod
    def round(self, number):
        pass