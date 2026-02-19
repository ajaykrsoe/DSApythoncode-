'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        speedx=head
        speed2x=head
        while(speed2x and speed2x.next):
            speedx=speedx.next
            if(speed2x.next):
                speed2x=speed2x.next.next
            else:
                speed2x=None
        return speedx.data
                
        
