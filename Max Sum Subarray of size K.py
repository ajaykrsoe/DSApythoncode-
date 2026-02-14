class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        i=0
        j=k
        windowSum=sum(arr[i:j:])
        maxSum=windowSum
        n=len(arr)
        while(j<n):
                    windowSum=windowSum-arr[i]+arr[j]
                    if(windowSum>maxSum):
                         maxSum=windowSum 
                         
                    i+=1
                    j+=1
                

      
        return  maxSum
                    
                    
                     
        
