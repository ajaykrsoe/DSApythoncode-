
class Solution:
    def generateAllWords(self,arr,ind,cs,digitToWord,ans) :
     
    
        if(ind==len(arr)):
            ans.append(cs.lower())
            return 
        if(digitToWord[arr[ind]] ) :
           for e in digitToWord[arr[ind]] :
                self.generateAllWords(arr,ind+1,cs+e,digitToWord,ans)
        else :
             self.generateAllWords(arr,ind+1,cs,digitToWord,ans)
            
          
      
        
        
        
        
    def possibleWords(self, arr):
        # code here
        d={1:"",2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ",0:""}
        words=[]
        self.generateAllWords(arr,0,"",d,words)
        return words 
        
