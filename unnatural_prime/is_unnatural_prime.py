import math

def is_unnatural_prime(n: int) -> bool:
    """
    This function determines if a given integer n is a prime number or a negative prime number.
    
    It is part of a Daily Coding Challenge from freeCodeCamp.

    Parameters:
    ----------
    n : int
        The integer to be evaluated as a prime or negative prime.

    Returns:
    -------
    bool
        True if n is a prime number or a negative prime number, False otherwise.

    Raises:
    ------
    TypeError
        If n is not an integer.
    """

    # checking n is integer
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    # using the absolute value to unificate positive and negative integers
    n_abs = abs(n)

    # 0 and 1 are not primes
    if n_abs < 2:
        return False

    # going through all the possible divisors
    for divisor in range(2, math.isqrt(n_abs) + 1):
        if n_abs % divisor == 0:
            return False
            
    return True