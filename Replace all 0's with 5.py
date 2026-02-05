# Function should return an integer value
class Solution:

    def convertFive(self, n):
        # Code here
        if(n==0):
            return 5
        reverse=0
        while(n):
            digit=n%10
            if(digit==0):
                digit=5
                
            reverse=reverse*10+digit
            n//=10
        ans=0
        while(reverse):
            digit=reverse%10
            ans=ans*10+digit
            reverse//=10
        return ans
        
                
    
