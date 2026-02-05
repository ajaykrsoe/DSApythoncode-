class Solution:
    def largestAndSecondLargest(self, arr: list[int]) -> list[int]:
        # code here 
        max1=0
        max2=0
        for e in arr :
            if(e>max1):
                max2=max1
                max1=e
            elif(e>max2 and e!=max1):
                max2=e
        if(max1==max2 or max2==0 ):
            return [max1,-1]
        return [max1,max2]
