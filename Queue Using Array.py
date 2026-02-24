class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue=[]
        self.n=n
        

    
    def isEmpty(self):
        # Check if queue is empty
        if(not self.queue):
            return 1
        return 0

    
    def isFull(self):
        # Check if queue is full
        if( len(self.queue)==self.n):
            return 1
        return 0

    
    def enqueue(self, x):
        if( len(self.queue)==self.n):
            return -1
        self.queue.append(x)
        # Enqueue

    
    def dequeue(self):
        if(not self.queue):
            return -1
        return self.queue.pop(0)
        # Dequeue

    
    def getFront(self):
        if(not self.queue):
            return -1
        return self.queue[0]
        # Get front element
       
    
    def getRear(self):
        if(not self.queue):
            return -1
        return self.queue[-1]
        # Get rear element 
        
        
