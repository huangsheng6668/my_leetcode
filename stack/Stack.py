"""
@File        : Stack.py
@Description : 创建栈的类
@author      : sheng
@date time   : 2020/1/31 21:16
@version     : v1.0
"""
from daily_me.algorithm.stack.StackException import StackException


class Stack:
    def __init__(self, size):
        self._stack = [None for i in range(0, size)]
        self.size = size
        self.top = 0

    def push(self, obj):
        if self.top == self.size - 1:
            raise StackException('Stack is full!')
        else:
            self._stack[self.top] = obj
            self.top += 1

    def pop(self):
        if self.top == 0:
            raise StackException('Stack is None!')
        else:
            pop_value = self._stack[self.top - 1]
            self._stack[self.top - 1] = None
            self.top -= 1
            return pop_value

    def peek(self):
        return self._stack[self.top - 1]

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    stack = Stack(2)
    stack.push(1)
    print(stack.empty())
    print(stack.peek())
    print(stack.pop())

