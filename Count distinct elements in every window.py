class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        i=0
        j=k-1
        hashMap={e:0 for e in arr}
        ans=[]
        window=arr[i:j+1:]
        count=len(set(window))
        ans=[count]
        for e in window :
            hashMap[e]+=1
 

        while(j<n):
                if(hashMap[arr[i]]==1) :
                   count-=1
                hashMap[arr[i]]-=1
                i+=1
                j+=1
                if(j<n) :
                    if( hashMap[arr[j]]==0) :
                       count+=1 
                    hashMap[arr[j]]+=1
                else :
                    return ans 
                ans.append(count)

               
                 
                   
        return ans
                
                
            
            
        
        
        
        
