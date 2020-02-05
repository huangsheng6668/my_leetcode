# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其自底向上的层次遍历为：
#
#  [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#  Related Topics 树 广度优先搜索
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    通过DFS（深度优先遍历），先找到最深的那一层，然后层层添加进一个新的列表
    每一层的元素都在一个列表当中，然后添加进要返回的列表当中，然后使得列表倒序即可
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [[root]]
        stack_value = [[root.val]]
        while stack:
            nodes = stack[-1]
            cur_node = []
            cur_values = []
            for node in nodes:
                if node:
                    if node.left:
                        cur_node.append(node.left)
                        cur_values.append(node.left.val)
                    if node.right:
                        cur_node.append(node.right)
                        cur_values.append(node.right.val)
            if cur_node:
                stack.append(cur_node)
                stack_value.append(cur_values)
            else:
                break
        return stack_value[::-1]

    """
    通过递归的方式解决
    终止条件为遍历所有叶子节点为止
    """
    def levelOrderBottom_2(self, root: TreeNode) -> List[List[int]]:
        list_tree = []
        def recursive(root, depth):
            if not root:
                return
            # 当list_tree为[]时，为里面的函数添加一层列表
            if depth == len(list_tree):
                list_tree.insert(0, [])
            list_tree[-(depth + 1)].append(root.val)
            recursive(root.left, depth + 1)
            recursive(root.right, depth + 1)
            return list_tree
        return recursive(root, 0)

# leetcode submit region end(Prohibit modification and deletion)
