class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTTree:
    def __init__(self):
        self.top = None

def insertRec(node, data):
    if node.data > data:
        if node.left is None:
            node.left = Node(data)
        else:
            insertRec(node.left, data)
    else:
        if node.right is None:
            node.right = Node(data)
        else:
            insertRec(node.right, data)

def insert(tree, data):
    if tree.top is None:
        tree.top = Node(data)
        return
    insertRec(tree.top, data)
