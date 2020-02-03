"""
@File        : StackException.py
@Description : 栈的自定义异常类
@author      : sheng
@date time   : 2020/1/31 21:26
@version     : v1.0
"""


class StackException(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message
