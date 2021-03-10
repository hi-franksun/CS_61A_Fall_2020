

## Design Functions

函数设计的原则
1. Each function should have exactly one job. That job should be identifiable with a short name and characterizable in a single line of text. Functions that perform multiple jobs in sequence should be divided into multiple functions.每个函数都应该有专一的职责，负责一个功能的处理，不应该大包大揽，如果不是单一职责的就应拆成多个函数；
2. Don't repeat yourself is a central tenet of software engineering. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.DRY 原则，如果除了重复的 block of code，你得反思一下是不是自己设计出问题了！
3. Functions should be defined generally. Squaring is not in the Python Library precisely because it is a special case of the pow function, which raises numbers to arbitrary powers.函数的定义应该更加的通用和包容，类似很多可选的参数一样，默认平方，如果想要立方，加一个 3 参数即刻，而不需要每一个都定义，通用很重要！

design example



## Higher-Order Functions

why we need higher-order function
- express general methods of computation. 表达通用的方法
- remove repetition from programs.移除不必要的重复
- separate concerns among functions.功能之间的分离关注点


### Function is First-Class 

fuction can as arguments also as return value

so, just because function can as arguments also as return value, we call this higher-order function


### Lambda expression

lambda syntax
```python
square = lambda x: x * x # this is expression evaluates to a function  # important: has no return keyword
       # a function
               # with formal parameter x
                   # that returns the value of "x * x"
                                              # return must be s single expression

```
lambda expressions versus def statements

the most diffence is function name
```python
square = lambda x: x * x # <function <lambda> at 0x000001E6B5BBD558>

def square(x): # <function square at 0x000001E6B5BBD438>
    return lambda
```
