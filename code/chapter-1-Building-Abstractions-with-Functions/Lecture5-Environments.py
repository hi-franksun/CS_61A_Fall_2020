
# ======================================================
def square(x):
    return x * x

def apply_twice(f, x):
    return f(f(x))

# apply_twice(3) # 9


# =====================================================

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3
    
repeat(g, 5) # 2

# =====================================================

def make_adder(n):
    def adder(k):
        return n + k
    return adder

add_three = make_adder(3) # this is right use methods
add_three(4) # 7

# =====================================================
# decorator


# =====================================================
# Local Names

def f(x, y):
    return g(x)

def g(a):
    # return a + y # commemt this,else this will be error
    pass

f(1, 2) # 
# this will error, not found y because y not in global frame, compare with last function make_adder, function adder can find n in fmake_adder function



# =====================================================
# function composition

def make_adder(n):
    def adder(k):
        return n + k
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

squiple = compose1(square, triple)
squiple(5) # 255

tripare = compose1(triple, square)
tripare(5) # 75

squadder = compose1(square, make_adder(2))
squadder(3) # 25

# =====================================================
# lambda expression






# =====================================================
# self-reference 自引用

def print_all(x):
    print(x)
    return print_all

print_all(10)(100)(1000) # 10 100 1000

def print_sum(x):
    print(x)
    def next_sum(k):
        return print_sum(x+k)
    return next_sum
print_sum(1)(3)(5) # this is interesting and amazing

print_all(10)(100)(1000) # 10 100 1000

# =====================================================
# Function Currying 操作函数的一种方法


# =====================================================
# =====================================================
# =====================================================