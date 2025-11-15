"""
Basic arithmetic operations module.

This module provides simple functions for performing basic arithmetic operations
including addition, subtraction, multiplication, and division.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of a and b.
    
    Args:
        a: The first number (int or float).
        b: The second number (int or float).
    
    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Return the difference of a and b (a - b).
    
    Args:
        a: The minuend (int or float).
        b: The subtrahend (int or float).
    
    Returns:
        The difference of a and b.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of a and b.
    
    Args:
        a: The first number (int or float).
        b: The second number (int or float).
    
    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Return the quotient of a divided by b.
    
    Args:
        a: The dividend (int or float).
        b: The divisor (int or float).
    
    Returns:
        The quotient of a divided by b as a float.
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Example usage
    print("add(2, 3) =", add(2, 3))
    print("subtract(7, 5) =", subtract(7, 5))
    print("multiply(4, 2.5) =", multiply(4, 2.5))
    try:
        print("divide(10, 2) =", divide(10, 2))
    except ZeroDivisionError as e:
        print("Error:", e)