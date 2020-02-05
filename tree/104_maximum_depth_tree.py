"""
@File        : 104_maximum_depth_tree.py
@Description : Leetcode第104题二叉树的最大深度
给定一个二叉树，找出其最大深度。

 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

 说明: 叶子节点是指没有子节点的节点。

 示例：
给定二叉树 [3,9,20,null,null,15,7]，

     3
   / \
  9  20
    /  \
   15   7

 返回它的最大深度 3 。
 Related Topics 树 深度优先搜索
@author      : sheng
@date time   : 2020/2/5 0:08
@version     : v1.0
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    通过迭代的方式，通过深度优先遍历来获取，
    可以通过栈的方式，把根节点载入进栈，
    一次取出一个节点，当取出的那个节点不为空，则
    开始进行迭代，只要还有叶子节点存在就可以一直深度遍历
    然后通过max函数比较当前深度与记录的深度谁最大取谁
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_depth, node = stack.pop()
            if node:
                stack.append((cur_depth + 1, node.left))
                stack.append((cur_depth + 1, node.right))
                depth = max(cur_depth, depth)
        return depth

    """
    通过递归的方式解决，
    终止条件为当前节点为None
    """
    def maxDepth_2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth_2(root.left), self.maxDepth_2(root.right)) + 1
