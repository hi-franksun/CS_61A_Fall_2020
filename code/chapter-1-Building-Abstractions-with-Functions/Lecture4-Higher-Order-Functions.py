
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
