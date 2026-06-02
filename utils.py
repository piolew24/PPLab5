"""Basic arithmetic utility functions."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of a divided by b."""
    return a / b


def natural_to_binary(value: int) -> str:
    """Convert a natural number in range 0..100 to a binary string."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("value must be a natural number (int)")
    if value < 0 or value > 100:
        raise ValueError("value must be in range 0..100")

    return format(value, "b")
