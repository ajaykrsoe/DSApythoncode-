# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top=None
        

    def isEmpty(self):
        # Check if the stack is empty
        if(self.top==None) :
            return True 
        else :
            return False
        

    def push(self, x):
        # Adds element x to the top of the stack
        newNode=Node(x)
        if(self.top):
            newNode.next=self.top
            self.top=newNode
        else :
            self.top=newNode
        
        
        

    def pop(self):
        
        # Removes an element from the top of the stack
        if(self.top):
            self.top=self.top.next
        else :
            self.top=None
        

    def peek(self):
        if(self.top==None) :
            return -1
        temp=self.top
     
        return  temp.data
                # Returns the top element of the stack
        # If the stack is empty, return -1


    def size(self):
        # Returns the current size of the stack
        count=0
        temp=self.top
        while(temp):
            count+=1
            temp=temp.next
        return count 
