
from heapq import * 
class Solution:
    def getMedian(self, arr):
        heap1=[-arr[0]]
        heap2=[]
        count1=1
        count2=0
        medians=[arr[0]]
        for e in  arr[1::]:
            temp=-heappop(heap1)
            if e>=temp :
                if count1==count2 :
                    heappush(heap1,-temp)
                    heappush(heap2,e)
                    heappush(heap1,-heappop(heap2))
                    count1+=1
                else :
                    
                    heappush(heap1,-temp)
                    heappush(heap2,e)
                    count2+=1
            else :
                if count1==count2 :
                        heappush(heap1,-temp)
                        heappush(heap1,-e)
                        count1+=1
                else :
                        
                        heappush(heap1,-e)
                        heappush(heap2,temp)
                        count2+=1
            if count1==count2 :
                  x=-heappop(heap1)
                  y=heappop(heap2)
                  medians.append((x+y)/2 )
                  heappush(heap1,-x)
                  heappush(heap2,y)
             
                  
            else :
                 x=-heappop(heap1)
                 heappush(heap1,-x)
                 medians.append(x)
            
        return medians 
                 
                 
                   
            
            
            
    
                    
             
                 
        
        
