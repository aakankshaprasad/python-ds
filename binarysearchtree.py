class Node:
    def __init__(self, dataval):
        self.data=dataval
        self.right=None
        self.left=None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def insert(self, dataval):
        if self.data:
            if dataval < self.data:
                if self.left is None:
                    self.left = Node(dataval)
                else:
                    self.left.insert(dataval)
            elif dataval > self.data:
                if self.right is None:
                    self.right = Node(dataval)
                else:
                    self.right.insert(dataval)
        else:
            self.data = dataval

root=Node(10)
root.insert(20)
root.insert(9)
root.printTree()
