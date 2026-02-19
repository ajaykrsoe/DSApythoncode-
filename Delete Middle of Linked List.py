'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        if(not head.next) :
            return None
        if(not head.next.next):
            head.next=None
            return head 
        speedx=head
        speed2x=head
        while(speed2x and speed2x.next ):
            speedx=speedx.next
            if(speed2x.next):
                speed2x=speed2x.next.next
            else :
                speed2x=None
        middleNode=speedx
        middleNode.data=middleNode.next.data
        middleNode.next=middleNode.next.next
        return head











        #code here
