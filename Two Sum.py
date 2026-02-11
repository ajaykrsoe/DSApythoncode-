class Solution:
	def twoSum(self, arr, target):
		# code here
	    arr.sort()
	    i=0
	    j=len(arr)-1
	    while(i<j):
	        Sum=arr[i]+arr[j]
	        if(Sum==target):
	            return True
	        elif(Sum<target):
	            i+=1
	        else :
	            j-=1
	    return False
	    
	        
