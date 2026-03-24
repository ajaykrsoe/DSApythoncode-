from heapq import * 
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n=len(val)
        rate=[]
        for i in range(n) :
            rate.append( (-val[i]/wt[i],wt[i] ) )
        
        heapify(rate)
        max_value=0
        while(rate) :
            r,w=heappop(rate)
            r=-r
  
            if(w<=capacity ) :
                 max_value+=(w*r)
                 capacity-=w
            else :
                max_value+=(capacity*r)
                break

        return max_value
                     



class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n=len(val)
        rate=[]
        for i in range(n) :
            rate.append( (val[i]/wt[i],wt[i] ) )
        rate.sort(key=lambda x :x[0],reverse=True)
        max_value=0
      
        for r ,w in rate :
                    if(w<=capacity ) :
                         max_value+=(w*r)
                         capacity-=w
                    else :
                        max_value+=(capacity*r)
                        break
        
        return max_value
                        
                        
                             
                             
                     
        
