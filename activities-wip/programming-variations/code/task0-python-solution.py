class Node:
    def __init__(self, value):
        self.data = value
        self.left  = None
        self.right = None

def insert(tree, value):
    if tree is None:
        return Node(value)
    if value == tree.data:
        return tree
    if value < tree.data:
        tree.left = insert(tree.left, value)
        return tree
    # value > tree.data
    tree.left = insert(tree.left, value)
    return tree
  
def lookup(tree, value):
    if tree is None:
        return False
    if tree.data == value:
        return True
    if value < tree.data:
        return lookup(tree.left, value)
    # value > tree.data
    return lookup(tree.right, value)
