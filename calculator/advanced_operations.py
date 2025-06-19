"""
Advanced calculator operations.
Testing feature branch workflow.
"""

import math


def square_root(number: float) -> float:
    """Calculate square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def logarithm(number: float, base: float = math.e) -> float:
    """Calculate logarithm of a number."""
    if number <= 0:
        raise ValueError("Logarithm is not defined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(number) / math.log(base)
