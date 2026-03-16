class LRUCache:
      
    def __init__(self, cap):
        #code here
        self.cache={}
        self.cap=cap

    def get(self, key):
        #code here
        if( key in self.cache):
           value=self.cache.pop(key)
           self.cache[key]=value
           return value
           
        else :
            return -1
            
        

    def put(self, key, value):
        #code here
        if(self.cap==0) :
            return 
 
        if( key in self.cache  ):
                self.cache.pop(key)
                self.cache[key]=value
                
        else :  
                n=len(self.cache)

                # self.cache[key]=value  
                if(n==self.cap) :
                            for k in self.cache :
                                firstKey=k
                                break
                            self.cache.pop(firstKey)  
                            self.cache[key]=value
                    
                    
                else :
                      self.cache[key]=value
                
                 

  
            
