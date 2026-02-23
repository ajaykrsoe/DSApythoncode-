class Solution:
    def isBalanced(self, s):
        # code here
        stack=[]
        parmap={  "]":"[" , "}":"{" , ")":"("}
        for e in s :
            if(e  in parmap.values() ):
                stack.append(e)
            else :
                if(not stack  or stack[-1]!=parmap[e]) :
                    return False
                else :
                    stack.pop()
        if(stack ):
            return False
        return True 
        
        
