"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""


def averageOfLevels(root):
    res = []
    if not root:
        return res
    q = [root]
    while q:
        q1 = []
        total = 0
        cnt = 0
        while q:
            node = q.pop()
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
            total += node.val
            cnt+= 1
        res.append(total * 1.0 /cnt)
        q = list(q1)
    return res