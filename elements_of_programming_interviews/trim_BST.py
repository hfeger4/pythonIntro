"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1"""

def trimbst(tree, minVal, maxVal):
    if not tree:
        return

    tree.left = trimbst(tree.left, minVal, maxVal)
    tree.right = trimbst(tree.right, minVal, maxVal)

    if minVal <= tree.val <= maxVal:
        return tree
    if tree.val < minVal:
        return tree.right
    if tree.val > maxVal:
        return tree.left



