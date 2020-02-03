"""
@File        : Fibonacci.py
@Description : 用Python实现斐波那契数列
@auth        : sheng
@date time   : 2019/9/19 9:44
@version     : v1.0
"""


def fibonacci(n):
    a, b = 0, 1
    while n >= 0:
        a, b = b, a + b
        n -= 1
        yield a


def fibonacci_recursive(n):
    if n <= 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


for i in fibonacci_recursive(10):
    print(i)
