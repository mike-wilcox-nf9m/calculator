# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import devide
    >>> devide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.
    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the difference of two numbers.
    Examples:
    >>> subtract(4, 2)
    2.0
    >>> subtract(2, 4)
    -2.0
    >>> subtract(4.2, 2.0)
    2.2

    Args:
        a: A number representing the first addend in the difference.
        b: A number representing the second addend in the difference.
    
    Returns:
         A number representing the arithmetic difference of `a` and `b`.
    """
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.
    Examples:
    >>> multiply(2, 2)
    4.0
    >>> multiply(1.5, 3.5)
    5.25

    Args:
        a: A number representing the first addend in the product.
        b: A number representing the second addend in the product.
    
    Returns:
        A number representing the arithmetic product of `a` and `b`.
    """
    return float(a * b)


def devide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.
    examples:
    >>> devide(4, 8)
    0.5
    >>> devide(8, 4)
    2.0

    Args:
        a: A number representing the first addend in the quotient.
        b: A number representing the second addend in the quotient.
    
    Returns:
         A number representing the arithmetic quotient of `a` and `b`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
