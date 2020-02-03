"""
@File        : Node.py
@Description : TODO 链表的节点
@author      : sheng
@date time   : 2019/9/4 15:04
@version     : v1.0
"""
from collections import namedtuple

Node = namedtuple('node', 'data next')
head = Node


def insert_node(node):
    Node.next = node

