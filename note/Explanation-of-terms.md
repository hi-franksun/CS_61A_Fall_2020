
## expression:表达式

subexpression:子表达式
```python
>>>1 # this is expression
1

>>> def sum_two_nums(n1, n2):
        return n1 + n2
>>> sum_two_nums(1, 2) # this is expression, is called expression 调用表达式
>>> result = sum_two_nums(1, 2) # this is expression
>>> 100 # a value is also expression
```

## statement

### assignment statement:赋值语句

```python
>>> message = "This is assignment statement" # this is assignment statement
>>> result = 100  # this is assignment statement
```

### def statement
```python
>>> def square(x): # this is def statement
        return mul(x, x)
```

### conditional statement (compound statement:复合语句，包含多行的意思)

conditional statement is dependend on `boolean contexts`(布尔上下文，也就是说 condition statement 依赖 boolean 判断，并且一个完整的 conditional statement 中只有一个为 true，也就是只有一个会执行（这也是为什么会有 else 进行兜底的原因）)

Boolean ：
false values in python: 0, "", None,False
true values in python: anything else

relational operators(关系运算符):` ==/!=/>/</>=/<=`
logical operators(逻辑运算符)：`not/and/or`

#### if statement

execution rule for statement

```python
if Condition1:
    Statements1
elif Condition2:
    Statements2
...
else:
    Statementsn
```


```python
def solution(x):
    if x == 0: # this is boolean expression, == is relational operator(关系运)
        return 0
    elif x == 1:
        return 1
    else:
        return 2
```

#### while statement

不满足条件，会不断重复的循环，而 if 一般只会一次判断，不会一直循环！

execution rule for while statement


paramenter:参数，Formal Parameter，形式参数，比如 fucntion 定义时候规定的参数，位置参数、形式参数、默认参数、可变参数等

> parameter是指函数定义中参数，而argument指的是函数调用时的实际参数。 当定义方法时，传递到方法中的变量称为参数，C语言英文版( The C Programming Language, 2nd Edition)就知道了。parameter是形参，在函数定义时放在小括号里。argument 是实参，在调用函数时放在小括号里。其实，形参的原本英文是 formal argument, 实参的原本英文是 actual argument.

```python
>>> def abs(number): # number is a paramenter
        return abs(number)
```

argument:参数，Actual Argument，实际传入的参数

```python
>>> abs(-1) # -1 is a argument
1
```


operator:操作符，+/*/%/**
operand:操作数 like 1+2 --> 1 and 2 is operands

division:除法

truedivision：整数除法
floordivision：地板除
mod：余数


conditional expression

```python
<consequent(结果)> if <predicate> else <alternative>`
```

pure functions
pure return a value by your input value.

non-pure functions(**has side effects**):print
print will display value your input, and print function has non return value, print return `None`.


Nested function:嵌套函数

evaluate:评估

syntax:语法

lambda expression is diffent between def statement，lambda has no function name

in fact,lambda is 