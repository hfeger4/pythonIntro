"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""



def levelOrder(self, root):
    level_order_traversal = []
    queue = [(root,0)]
    for node,level in queue:
        if node:
            if level >= len(level_order_traversal):
                level_order_traversal.append([])
            level_order_traversal[level].append(node.val)
            queue.append((node.left,level+1))
            queue.append((node.right,level+1))
    return level_order_traversal