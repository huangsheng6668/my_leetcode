# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
#
#  注意：
#
#
#  给定的目标值 target 是一个浮点数
#  题目保证在该二叉搜索树中只会存在一个最接近目标值的数
#
#
#  示例：
#
#  输入: root = [4,2,5,1,3]，目标值 target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# 输出: 4
#
#  Related Topics 树 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        不管是递归还是迭代的解法，我们都要先从题目这个二叉搜索树来出发
        二叉搜索树的左孩子比根节点小，右孩子比根节点大
        所以我们最需要判断的是：
            这个目标节点是否比当前的根节点大
        理解了这个，我们几乎就可以写出代码了，还需要注意的是：
            接近某个值，那个值可以比目标值大，也可以比目标值小，
            只是需要两者之间的差值是最小的即为最接近的。
    """
    def closestValue(self, root: "TreeNode", target: float) -> int:
        def recorsive(node, appreach_node):
            if not node:
                return appreach_node
            if abs(node.val - target) < abs(appreach_node.val - target):
                appreach_node = node
            if target > node.val:
                return recorsive(node.right, appreach_node)
            else:
                return recorsive(node.left, appreach_node)
        return recorsive(node=root, appreach_node=root).val

    def closestValue1(self, root: "TreeNode", target: float) -> int:
        stack = [(root, root)]
        while stack:
            node, appreach_node = stack.pop()
            if not node:
                return appreach_node.val
            if abs(node.val - target) < abs(appreach_node.val - target):
                appreach_node = node
            if target > node.val:
                stack.append((node.right, appreach_node))
            else:
                stack.append((node.left, appreach_node))
# leetcode submit region end(Prohibit modification and deletion)
