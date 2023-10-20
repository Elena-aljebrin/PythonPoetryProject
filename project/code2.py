"""
This module defines a function to check if a number is even.
"""
def is_even(num: int) -> bool:
    """
    Check if a number is even.
    Args:
        num (int): The number to be checked.
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return num%2 ==0
print("Example:")
print(is_even(2))
