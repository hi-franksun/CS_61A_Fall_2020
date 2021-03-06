"""
you can use `python -i source.py`, then you will get this source file all things,
example, you get global variable `person_name` 、function get_username() in source files
"""

"""
division and mod
"""

def divide_exact(n, d):
    """ This is docstring
    you can use `python -m doctest file.py` to test this function, 
    add `-v` to get more used informations, like `python -m doctest file.py`

    >>> q, r = divide_exact(2021, 10)
    >>> q
    202
    >>> r
    1
    >>> r # this is error
    10 
    """
    return n // d, n % d


def prime_factors(n):
    """Print the prime factors of the n.

    >>> prime_factors(2)
    2
    >>> prime_factors(3)
    3
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(12)
    2
    2
    3
    """

# 使用函数以及合适的变量和函数命名，才是好的程序，而不是乱写！！！
