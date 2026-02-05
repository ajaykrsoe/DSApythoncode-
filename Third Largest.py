class Solution:
    def thirdLargest(self,arr):
        # code here
        n=len(arr)
        if(n<3):
            return -1
        max1=0
        max2=0
        max3=0
        for e in arr :
            if(e>max1):
                max3=max2
                max2=max1
                max1=e
            elif(e>max2):
                max3=max2
                max2=e
            elif(e>max3):
                max3=e
        return max3
            
