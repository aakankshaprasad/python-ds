class Node:
    def ___init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def createTree(self,data):
        n=Node(data)
    def printtree(self):
        print(self.data)

root = Node()

root.printtree()

##
