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

def asset_type_check(asset_type: str) -> bool:
    """
    Function to check if an asset type is valid.

    Parameters
    ---------
    asset_type : str
        Asset type category.

    Returns
    ---------
    bool
        True if valid asset type, False if not.
    """
    valid_types = ['pipe', 'bend', 'valve']

    if asset_type.lower() not in valid_types:
        return False
    return True

if __name__ == "__main__":
    pass