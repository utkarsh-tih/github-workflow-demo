"""
Main calculator application.
Demo application for testing GitHub workflow.
"""

from calculator.advanced_operations import factorial, logarithm, square_root
from calculator.operations import add, divide, multiply, power, subtract


def main():
    """Main application function."""
    print("🧮 Demo Calculator")
    print("=" * 20)

    # Basic operations demo
    print("Basic Operations:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2 ^ 8 = {power(2, 8)}")

    # Advanced operations demo
    print("\nAdvanced Operations:")
    print(f"√16 = {square_root(16)}")
    print(f"5! = {factorial(5)}")
    print(f"log₁₀(100) = {logarithm(100, 10)}")


if __name__ == "__main__":
    main()
