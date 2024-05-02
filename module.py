def reverse(text: str) -> str:
    """
    Function that reverses a string.

    Parameters
    ----------
    text : str
        Text to be reversed.

    Returns
    ----------
    str
        Reversed text
    """
    return text[::-1]

def tolerance_check(input: float, reference: float = 12.00, tolerance: float = 0.25) -> bool:
    """
    Function to check if a float value is equal to a reference value with tolerance.

    Parameters
    ----------
    input : float
        Input value to compare against a reference value.
    reference : float
        Reference value to compare input value against (default=12.00).
    tolerance : float
        Tolerance range (default=0.25). 

    Returns
    ----------
    bool
        True if within tolerance, False if not.

    """
    diff = abs(reference - input)

    return diff <= tolerance

if __name__ == "__main__":
    pass