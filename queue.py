#QUEUE=FIFO

class Queue:
    def __init__(self):
        self.queue=list()

    def insert(self,value):
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False

    #delete data from the end of the queue
    def delete(self):
        if len(self.queue)>0:
            self.queue.pop()
        return("No more elements in the queue")

    def display(self):
        if len(self.queue)>0:
            print(self.queue)

Q=Queue()
Q.insert(1)
Q.insert(2)