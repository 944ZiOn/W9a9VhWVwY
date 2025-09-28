# 代码生成时间: 2025-09-29 00:02:47
import numpy as np

"""
A collection of mathematical calculation tools using the numpy library.
This module includes functions for basic arithmetic operations and
more complex mathematical computations.
"""

# Define a class to encapsulate the mathematical operations
class MathCalculator:
    """
    A class that provides methods for various mathematical calculations.
    """

    def add(self, x, y):
        """
        Adds two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.
        """
        try:
            return x + y
        except TypeError as e:
            raise ValueError("Both arguments must be numbers.") from e

    def subtract(self, x, y):
        """
        Subtracts one number from another.

        Args:
            x (float): The minuend.
            y (float): The subtrahend.

        Returns:
            float: The difference between x and y.
        """
        try:
            return x - y
        except TypeError as e:
            raise ValueError("Both arguments must be numbers.") from e

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.
        """
        try:
            return x * y
        except TypeError as e:
            raise ValueError("Both arguments must be numbers.") from e

    def divide(self, x, y):
        """
        Divides one number by another.

        Args:
            x (float): The dividend.
            y (float): The divisor.

        Returns:
            float: The quotient of x divided by y.
        """
        try:
            if y == 0:
                raise ValueError("Cannot divide by zero.")
            return x / y
        except TypeError as e:
            raise ValueError("Both arguments must be numbers.") from e

    def power(self, x, y):
        """
        Raises a number to the power of another.

        Args:
            x (float): The base number.
            y (float): The exponent.

        Returns:
            float: The result of x raised to the power of y.
        """
        try:
            return np.power(x, y)
        except TypeError as e:
            raise ValueError("Both arguments must be numbers.") from e

    def square_root(self, x):
        """
        Calculates the square root of a number.

        Args:
            x (float): The number to find the square root of.

        Returns:
            float: The square root of x.
        """
        try:
            if x < 0:
                raise ValueError("Cannot calculate the square root of a negative number.")
            return np.sqrt(x)
        except TypeError as e:
            raise ValueError("The argument must be a number.") from e

# Example usage:
if __name__ == '__main__':
    calc = MathCalculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Power: ", calc.power(10, 5))
    print("Square Root: ", calc.square_root(25))
