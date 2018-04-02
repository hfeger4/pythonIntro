class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

def validate_bst(root, min = -float("inf"), max = float("inf")):
    if root == None:
        return True
    if (root.value > min and
        root.value < max and
        validate_bst(root.left_child, min, root.value) and
        validate_bst(root.right_child, root.value, max)):
        return True
    else:
        return False

#Test Case
root = Node(5)
l = Node(4)
r = Node(6)
root.left_child = l
root.right_child = r

print(validate_bst(root))

#Test Case
root = Node(5)
l = Node(4)
r = Node(3)
root.left_child = l
root.right_child = r

print(validate_bst(root))

#Test Case
root = Node(1)
l = Node(4)
r = Node(3)
root.left_child = l
root.right_child = r

print(validate_bst(root))
