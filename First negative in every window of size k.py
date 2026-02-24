#User function Template for python3

class Solution:
    def firstNegInt(self, arr, k): 
        n=len(arr)
        ans=[]
        i=0
        j=k-1
        window=arr[i:j+1:]
        for indx in range(k):
             if(arr[indx]<0):
                 break
        if(arr[indx]<0) :
            ans.append(arr[indx])
        else :
            ans.append(0)
            indx=0
        i+=1
        j+=1
        while(j<n):
            if(indx<i) :
                indx=i
                while(indx<=j and arr[indx]>=0):
                    indx+=1
                if(indx <=j) :
                      ans.append(arr[indx])
                   
                else :
                    ans.append(0)
                  
            else  :
                if( arr[indx]<0):
                         ans.append(arr[indx])
                else :
                    ans.append(0)
                    indx+=1
                    

                
                    
            i+=1
            j+=1
        return ans 

                
                
            
        
            
            
        
