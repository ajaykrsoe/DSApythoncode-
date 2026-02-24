class myQueue:
    def __init__(self):
        # define your queue
        self.queue=[]
        

    def enqueue(self, x):
        # insert x into queue
        self.queue.append(x)

    def dequeue(self):
        # remove front element from queue
        if(self.queue) :
            return self.queue.pop(0)
        else :
            return False 
        


    def getFront(self):
        if(self.queue) :
            return self.queue[0]
        else :
            return False 
        
    def getRear(self):
        if(self.queue) :
            return self.queue[-1]
        else :
            return False         # return the rear element of the queue

    def isEmpty(self):
        if(self.queue) :
            return False
        else :
            return True         # check whether queue is empty

    def size(self):
        # return size of the queue
        return len(self.queue)
