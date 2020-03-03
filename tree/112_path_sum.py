# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
#  
# 
#  返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。 
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        利用栈来处理，通过判断是否是叶子节点和当前和是否被减成0，
        与根节点是不是个空节点为终止条件。
    """
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == 0:
                return True
            if node.left:
                stack.append((node.left, cur_sum - node.left.val))
            if node.right:
                stack.append((node.right, cur_sum - node.right.val))
        return False

    """
        利用递归来解决这题，通过判断是否是叶子节点和当前和是否被减成0，
        与根节点是不是个空节点为终止条件
    """
    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.right and not root.left:
            return sum == 0
        return self.hasPathSum2(root.left, sum) or self.hasPathSum2(
            root.right, sum)
# leetcode submit region end(Prohibit modification and deletion)
