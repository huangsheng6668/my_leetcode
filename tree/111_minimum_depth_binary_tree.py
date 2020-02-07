# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最小深度 2. 
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    本题用递归解法，
    需要注意的是其终止条件，
    需要考虑到这几种情况：
    1.当只有根节点
    2.当只存在左/右孩子
    3.当树为空树时
    """
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not any([root.left, root.right]):
            return 1

        def recorsive(node):
            if node is not None:
                depth_left = recorsive(node.left) + 1
                depth_right = recorsive(node.right) + 1
                if depth_left == 1 and depth_right:
                    return depth_right
                elif depth_right == 1 and depth_left:
                    return depth_left
                return min(depth_left, depth_right)
            else:
                return 0
        return recorsive(root)
# leetcode submit region end(Prohibit modification and deletion)
