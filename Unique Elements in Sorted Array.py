class Solution1:
	def pushZerosToEnd(self, arr):
	    n=len(arr)
	    slow=0
	    fast=0
	    while(fast<n):
	       if(arr[fast]):
	           arr[slow],arr[fast]=arr[fast],arr[slow]
	           slow+=1
	        
	       fast+=1
	            
class Solution2:
	def pushZerosToEnd(self, arr):
      pass
