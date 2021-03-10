
# ===============================================================

# Describing Functions

"""
其实就是分析和猜测代码的原理，更多的其实就是阅读源代码的方法这个意思，去猜测代码表达的意思！

one approach
1. read the code
2. read the describing options
3. consider an example
"""


## Boolean Favorites
from typing import Generator


def likes(n):
    """Returns weather george boolean likes the non-negative integer n."""

    pass

def mystery1(n):
    k = 1
    while k < n:
        if likes(n):
            print(k)
        else:
            k += 2


# ===============================================================

# Generating environment diagram
# 根据 diagram 编写 code


# ===============================================================
# Implementing functions 执行函数（功能）

"""
1. read the description
2. verity the example & pick a simple one
3. read the template

"""

def remove(n, digit):
    """ remove digit in n
    >>> remove(231, 2)
    21
    >>> remove(243132, 2)
    4313
    """

# ===============================================================

# python decorator

def trace(fn):
    """
    return a version of fn that first print when it is called
    
    fn -a function of 1 argument
    """
    def traced(x):
        print(f"Calling {fn}, argument is {x}")
        return fn(x)
    return traced

# @trace
def square(x):
    return x * x

square = trace(square) # this is not understand, but you must to understand!!!

@trace
def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

# ===============================================================
