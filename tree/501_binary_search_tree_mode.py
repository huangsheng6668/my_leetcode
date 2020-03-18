# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
#  假定 BST 有如下定义：
#
#
#  结点左子树中所含结点的值小于等于当前结点的值
#  结点右子树中所含结点的值大于等于当前结点的值
#  左子树和右子树都是二叉搜索树
#
#
#  例如：
# 给定 BST [1,null,2,2],
#
#     1
#     \
#      2
#     /
#    2
#
#
#  返回[2].
#
#  提示：如果众数超过1个，不需考虑输出顺序
#
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        通过递归+dict来解决该题，没有使用二叉搜索树的特性
        而是使用了广度优先遍历，通过dict来实现出现次数的存储，
        通过max函数选出字典当中最大的键，然后遍历字典，选出出现次数
        为最多的，加进要返回的列表当中。
    """
    def findMode(self, root: "TreeNode") -> List[int]:
        nums = {}
        num = []
        if not root:
            return []
        def recorsive(node):
            if not node:
                return
            # 这里可以要nonlocal也可以不要，因为dict属于不可变类型
            nonlocal nums
            count = nums.setdefault(node.val, 0) + 1
            nums[node.val] = count
            recorsive(node.left)
            recorsive(node.right)
        recorsive(root)
        max_key = max(nums, key=lambda x: nums[x])
        for key, value in nums.items():
            if value == nums[max_key]:
                num.append(key)
        return num
# leetcode submit region end(Prohibit modification and deletion)
