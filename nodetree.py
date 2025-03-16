class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.Right = right
        self.Left = left

class Tree:
    def __init__(self, root_val):
        self.root = Node(root_val)
    def findroot(self):
        return self.root.item
    def find(self, value):
        if value is None:
            return False
        def bsearch(node):
            if node is None:
                return False
            if node.item > value:
                return bsearch(node.Left)
            elif node.item < value:
                return bsearch(node.Right)
            else:
                return True
        return bsearch(self.root)
    def insert(self, value):
        def insertElement(node):
            if node is None:
                return Node(value)
            if value < node.item:
                node.Left = insertElement(node.Left)
            elif value > node.item:
                node.Right = insertElement(node.Right)
            return node 

        self.root = insertElement(self.root) 

    def traverse(self):
        final = []
        def traverseTree(branch): 
            if branch is None:
                return
            if isinstance(branch.Left, Node): 
                traverseTree(branch.Left) 
            final.append(branch.item) 
            if isinstance(branch.Right, Node): 
                traverseTree(branch.Right) 
        traverseTree(self.root)
        return final
