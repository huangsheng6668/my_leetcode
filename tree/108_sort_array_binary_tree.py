# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。 
# 
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。 
# 
#  示例: 
# 
#  给定有序数组: [-10,-3,0,5,9],
# 
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    通过递归的方式，
    首先先找到数组的中间数据作为根节点
    然后中间数据的左边就为树的左子树的数据
    右边数据就为右子树的数据
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) >> 1
        root = TreeNode(nums[mid])
        root.left, root.right = map(self.sortedArrayToBST, [nums[:mid], nums[mid+1:]])
        return root


# leetcode submit region end(Prohibit modification and deletion)
