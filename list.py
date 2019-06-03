class Node:
    def __init__(self, data=None):
        self.nextval = None
        self.dataval = data


#Insert: inserts a new node into the list

#Size: returns size of list

#Search: searches list for a node containing the requested data and returns that node if found, otherwise raises an error

#Delete: searches list for a node containing the requested data and removes it from list if found, otherwise raises an error

class LinkedList:
    def __init__(self):
        self.head = Node() # creating a head node that should point to the first node
        self.count=0

    def insert(self, val):
        new_node = Node(val)
        curr = self.head
        #print (self.head.nextval)
        if self.head.nextval is None:
            self.head.nextval=new_node
            self.count += 1
        else:
            while curr.nextval != None:
                curr = curr.nextval
                #print("insert my foot up your ass")
            curr.nextval = new_node
            self.count += 1


    def size(self):
        # current = self.head
        # count = 0
        # while current.nextval:
        #     count += 1
        #     current = current.nextval
        return self.count

    def display(self):
        elements = []
        current = self.head
        while current.nextval is not None:
            current = current.nextval
            elements.append(current.dataval)
        print (elements)

    def search(self, index): #return the value of the index
        if index>self.count:
            print IndexError
            return None
        else:
            curr=self.head
            currindex=0
            while True: #emulating do while since python doesnt have the same.
                if index==currindex:
                    return curr.dataval
                else:
                    currindex += 1
                    curr=curr.nextval


    def deleteNode(self,index): #deleting the node present at the specific index
        if index>=self.count:
            print IndexError
            return None
        else:
            curr=self.head
            curindex=0
            while True:
                if index==curindex:
                    prev.nextval=curr.nextval
                    return
                else:
                    curindex+=1
                    prev=curr
                    curr=curr.nextval


my_list=LinkedList()
my_list.insert(23)
my_list.insert(20)
my_list.insert(15)
my_list.display()
print("Size of the linked list is: %d"%my_list.size())
print("Value at 3rd index: %d"%  my_list.search(3))
my_list.deleteNode(2)
my_list.display()
