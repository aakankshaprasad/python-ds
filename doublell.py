class Node:
    def __init__(self, val=None):
        self.ptr = None
        self.data = val
        self.prevptr = None
class List:
    def __init__(self):
        self.head = None
        self.count = 0





    def insert(self, val):
        new_node = Node(val)
        #new_node.ptr = self.head
        #new_node.prevptr = None
        if self.head is None:
            self.head=new_node
            return
        new_node.ptr=self.head
        self.head.prevptr=new_node
        self.head = new_node



    def insertatend(self, val):
        new_node = Node(val)
        #new_node.ptr=None
        curr=self.head
        while(curr.ptr):
            #print(curr.data)
            curr = curr.ptr
        curr.ptr=new_node
        #new_node.prevptr=curr
        return

    def display(self):
        node = self.head
        while (node is not None):
            print(node.data)
            node = node.ptr

    def insertafter(self,prevnode,data):
        if (prevnode is None):
            print ("Given node cannot be NULL")
            return


        new_node=Node(data)
        new_node.ptr = prevnode.ptr
        prevnode.ptr=new_node
        new_node.prevptr=prevnode


        if (new_node.ptr is not None):
            new_node.ptr.prevptr=new_node


llist=List()

llist.insert(6)
llist.insert(4)
llist.insert(10)

llist.insertatend(99)
llist.insertatend(100)
llist.insertatend(108)
llist.insertafter(llist.head,177)

llist.display()




