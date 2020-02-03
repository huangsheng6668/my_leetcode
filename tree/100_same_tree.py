"""
@File        : 100_same_tree.py
@Description : 给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
         / \       / \
        2   3     2   3

       [1,2,3],   [1,2,3]

输出: true
@author      : sheng
@date time   : 2020/2/3 23:22
@version     : v1.0
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    通过递归的方式来完成这道题。
    终止条件为:
    1.p和q都为None
    2.p为None或者q为None
    3.p.val != q.val
    """
    def isSameTree_1(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
        return False


    """
    通过迭代的方式完成本题。
    通过一个列表作为队列，当每次按顺序提取元素时，两棵树其实取的都是相同位置，
    当位置都相同且值都相等的情况下，两者相等.
    """
    def isSameTree_2(self, p: TreeNode, q: TreeNode) -> bool:
        list_tree = [p, q]
        while list_tree:
            tree_1 = list_tree.pop()
            tree_2 = list_tree.pop()
            if tree_1 is None and tree_2 is None:
                continue
            if tree_1 is None or tree_2 is None:
                return False
            if tree_1.val == tree_2.val:
                list_tree.append(tree_1.left)
                list_tree.append(tree_2.left)
                list_tree.append(tree_1.right)
                list_tree.append(tree_2.right)
        return True
