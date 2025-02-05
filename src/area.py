def calculate_area_square(length: int | float) -> int | float:
    """
    Function to calculate the area of a square
    :param length: length of the square
    :return: area of the square
    """
    # Check if the input length is neither an integer nor a float, or if it is less than or equal to zero
    if not isinstance(length, (int, float)) or length <= 0:
        # Raise a TypeError with an appropriate message if the condition is met
        raise TypeError("Length must be a positive non-zero number")
    # Calculate and return the area of the square by multiplying the length by itself
    return length * length
