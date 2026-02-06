class Solution:
    def transitionPoint(self, arr): 
        # Code here
        for i in range(len(arr)):
            if(arr[i]):
                return i
        return   -1
