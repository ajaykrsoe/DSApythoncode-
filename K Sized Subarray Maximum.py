class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        i=0
        j=k-1
        window=arr[i:j+1:]
        n=len(arr)
        Max=max(window)
        ans=[Max]

        for l in range(k):
            if(arr[l]==Max):
                maxIndex=l
                break
        j+=1
        i+=1
    
        while(j<n):
            # print(maxIndex)
            if(maxIndex>=i ) :
                if(arr[j]>arr[maxIndex]):
                    ans.append(arr[j])
                    maxIndex=j
                else :
                    ans.append(arr[maxIndex])               
            else :

                    window = arr[i:j+1]
                    m = max(window)
                    maxIndex = i + window.index(m)   # make it absolute index
                    ans.append(m)



            i+=1
            j+=1
        return ans 
            
            
        
        
        
        
