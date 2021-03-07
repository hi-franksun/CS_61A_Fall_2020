
"""
todo:code fib function in 3 way
"""



"""
design functions
"""

def make_adder(n):

    def adder(k):
        return k + n
    return adder


add_three = make_adder(2000)
result = add_three(21)
print(result)

result = make_adder(2000)(21)
print(result)




def end(n, d):
    """
    Print the final digits of N in reverse order until D is found.
    
    1. first method: for loop find d, and print value after d
    2. second method: use math method
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if last == d:
            break


# ============================================================================

def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    """
    if x == 3:
        return True
    else:
        return False
    """
    return x == 3 # compare this code with docstring code, this is so clean!




# ============================================================================


from math import sqrt

def has_big_sqrt(x):

    return x > 0 and sqrt(x) > 10






# ============================================================================
# 理解这种高阶函数的东西，要从抽象入手，不要陷进去，抽象，无非就是先加后平方，没啥的，但是你要是陷进去了（实际代码会复杂很多），就很难出来！
def composel(f, g):
    def composed(x):
        return f(g(x))
    return composed

def square(x):
    return x * x

def add_one(y):
    return y + 1

h = composel(square, add_one)
result = h(5)
print(result) # 36


result = composel(square, add_one)(5) # 这种写法更加方便一点，其实也很好理解，(composel(square, add_one))(5) --> composel(squarem add_one) = f --> f(5) -->
# ============================================================================

a, b = 0, 1
a, b = b, a+b # 1, 1 注意这个地方是 1, 1
a, b = b, a+b # 1, 2
a, b = b, a+b # 2, 3
a, b = b, a+b # 3, 5
a, b = b, a+b # 5, 8


# ============================================================================


# ============================================================================


# ============================================================================
# ============================================================================








# ============================================================================