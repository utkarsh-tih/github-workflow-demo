"""
Test suite for advanced calculator operations.
"""

import math

import pytest

from calculator.advanced_operations import factorial, logarithm, square_root


class TestAdvancedOperations:
    """Test advanced mathematical operations."""

    def test_square_root(self):
        """Test square root calculation."""
        assert square_root(4) == 2
        assert square_root(9) == 3
        assert square_root(2) == pytest.approx(1.414, rel=1e-3)

    def test_square_root_negative(self):
        """Test square root with negative input."""
        with pytest.raises(ValueError, match="Cannot calculate square root"):
            square_root(-4)

    def test_factorial(self):
        """Test factorial calculation."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_negative(self):
        """Test factorial with negative input."""
        with pytest.raises(ValueError, match="Factorial is not defined"):
            factorial(-1)

    def test_logarithm_natural(self):
        """Test natural logarithm."""
        assert logarithm(math.e) == pytest.approx(1.0)
        assert logarithm(1) == pytest.approx(0.0)

    def test_logarithm_base_10(self):
        """Test logarithm base 10."""
        assert logarithm(100, 10) == pytest.approx(2.0)
        assert logarithm(1000, 10) == pytest.approx(3.0)

    def test_logarithm_invalid_input(self):
        """Test logarithm with invalid inputs."""
        with pytest.raises(ValueError, match="not defined for non-positive"):
            logarithm(-1)

        with pytest.raises(ValueError, match="Base must be positive"):
            logarithm(10, -1)
