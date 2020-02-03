"""
@File        : 101_symmetric_binary_tree.py
@Description : 给定一个二叉树，检查它是否是镜像对称的。
@author      : sheng
@date time   : 2020/2/3 21:56
@version     : v1.0
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    通过迭代的形式结题,通过一个列表，从中依次存放根节点的左孩子和右孩子，
    最初先按顺序取出两个元素，通过判断两个是否一个为空一个不为空；
    两者节点的值是否相等来分析两者是否不一样，接下来就是把孩子节点的叶子节点
    两边交叉添加进列表，使得所有叶子节点都能得到遍历。
    """
    def isSymmetric_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        qe = [root.left, root.right]
        while qe:
            qe_1 = qe.pop()
            qe_2 = qe.pop()
            if qe_1 is None and qe_2 is None:
                continue
            if qe_1 is None or qe_2 is None:
                return False
            if qe_1.val == qe_2.val:
                qe.append(qe_1.left)
                qe.append(qe_2.right)
                qe.append(qe_1.right)
                qe.append(qe_2.left)
            else:
                return False
        return True

    """
    通过递归的方式 把所有节点一一比对，这里需要判断的是，
    两个是否一个为空一个不为空；两者节点的值是否相等来分析两者是否不一样。
    """
    def isSymmetric_2(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.recursive(root.left, root.right)

    def recursive(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.recursive(left.left, right.right) and \
                self.recursive(left.right, right.left)
        else:
            return False
