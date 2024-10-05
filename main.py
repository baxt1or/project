

def add_numbers(a : int, b: int) -> int:
    """
       Sum of the two numbers

    Args:
        a (int): the first input
        b (int): the second input

    Returns:
        int: sum of a plus b
    """
    return a + b

def divide_numbers(a:float, b: float) -> float:

    """
        Gives the division of two numbers

    Raises:
        ValueError: denominator is 0

    Returns:
        float: a / b
    """

    if b == 0:
        raise ValueError("Denominator cannot be 0")
    return a/ b