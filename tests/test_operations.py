"""
Test suite for calculator operations.
Demo tests for GitHub workflow testing.
"""

import pytest

from calculator.operations import add, divide, multiply, power, subtract


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_subtract_numbers(self):
        """Test subtraction."""
        assert subtract(10, 3) == 7
        assert subtract(5, 10) == -5

    def test_multiply_numbers(self):
        """Test multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10

    def test_divide_numbers(self):
        """Test division."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5

    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_power_operation(self):
        """Test power operation."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_operations_with_zero(self):
        """Test operations involving zero."""
        assert add(0, 5) == 5
        assert subtract(0, 5) == -5
        assert multiply(0, 5) == 0

    def test_operations_with_floats(self):
        """Test operations with floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)
        assert multiply(2.5, 4) == 10.0

    def test_power_edge_cases(self):
        """Test power operation edge cases."""
        assert power(5, 0) == 1
        assert power(1, 100) == 1
