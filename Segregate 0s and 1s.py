#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        i=0
    
        n=len(arr)
        j=n-1
        while i< j :
            while i<n  and arr[i]==0 :
                i+=1
            while j>=0 and arr[j]:
                j-=1
            if  i<j :
             arr[i],arr[j]=arr[j],arr[i]
       
                
