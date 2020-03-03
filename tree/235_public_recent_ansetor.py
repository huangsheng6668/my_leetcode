#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   235_public_recent_ansetor.py    
@Email      :   huangsheng6668@163.com
@Modify Time:   2020/3/3 9:41    
@Author     :   sheng
@Version    :   1.0 
@Description:   None
"""
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#  例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
#
#
#  示例 1:
#
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#
#
#  示例 2:
#
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#  说明:
#
#
#  所有节点的值都是唯一的。
#  p、q 为不同节点且均存在于给定的二叉搜索树中。
#
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
        这题只要知道公共祖先的特点就可以推出来了，首先，祖先节点与两个节点都处在左子树或者右子树
        否则当前节点（递归会一直返回，当两个判断都不符合直接返回根节点，但是这期间有一个符合
        则那个期间的当前root就为祖先节点）
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 两个节点都在左子树的情况
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 两个节点都在右子树的情况
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    """
        几乎所有能递归的都能改写成用栈的形式解决，其实递归所用到的也是栈
    """
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > p.val and node.val > q.val:
                stack.append(node.left)
            elif node.val < p.val and node.val < q.val:
                stack.append(node.right)
            else:
                return node
        return root

# leetcode submit region end(Prohibit modification and deletion)

