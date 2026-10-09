def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if an integer is even, otherwise False."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the Python lab."