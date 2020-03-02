# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
        用迭代的方式来解这题，
        需要注意的是迭代的时候None值也需要添加
    """
    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                break
            left, right = node.left, node.right
            node.right = left
            node.left = right
            if left:
                stack.append(node.right)
            if right:
                stack.append(node.left)
        return root

    def invertTree2(self, root):
        """
            通过递归的方式解决，
            终止条件为node == None
            需要通过临时变量来存储左孩子或者右孩子，或者都存储
            这里采取都存储的方式
        """
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = self.invertTree2(right)
        root.right = self.invertTree2(left)
        return root
# leetcode submit region end(Prohibit modification and deletion)
