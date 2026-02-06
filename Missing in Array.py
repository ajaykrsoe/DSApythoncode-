class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        
        
        sum1=sum(arr)
        sum2=n*(n+1)
        sum2//=2
        return sum2-sum1
