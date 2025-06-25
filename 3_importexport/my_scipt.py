from functools import cache


def youngs_modulus(stress, strain):
    """Calculates youngs modulus, defined as stress/strain"""
    return stress / strain


@cache
def fast_fibonacci(n):
    """Calculates the nth fibonacci number

    Parameters:
        n: the fibonacci number

    Notes:
        See https://en.wikipedia.org/wiki/Young%27s_modulus
    """
    if n < 0:
        raise ValueError("Cannot calculate fibonacci numbers less that 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)
