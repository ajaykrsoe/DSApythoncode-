#User function Template for python3

class Solution:
    '''
    The function should do the stated modifications in the given array arr[]
    Do not return anything.
    '''
    # arr[]: Input Array
    # N: Size of the Array arr[]
    #Function to segregate 0s, 1s and 2s in sorted increasing order.
    def segragate012(self,arr, N):
        # Your Code Here
        count0=0
        count1=0
        count2=0
        for e in arr :
            if(e==0):
                count0+=1
            elif(e==1):
                count1+=1
            else:
                count2+=1
        k=0
        for e in range(count0):
            arr[k]=0
            k+=1
        for e in range(count1):
            arr[k]=1
            k+=1
        for e in range(count2):
            arr[k]=2
            k+=1
