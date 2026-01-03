class Solution:
    # Returns shortest distances from src to all other vertices
    def decreaseKey(self,arr,i,pos) :
        c=i
        p=(i-1)//2
        while(p>=0) :
            if(arr[p][1]>arr[c][1]):
                pv=arr[p][0]
                cv=arr[c][0]
                pos[pv]=c
                pos[cv]=p
                arr[p],arr[c]=arr[c],arr[p]
                c=p
                p=(p-1)//2
            else :
                break



    def heapifyDown(self,arr,i,pos) :
        l=i*2+1
        r=l+1
        n=len(arr)
        m=i
        if(l<n and arr[l][1]<arr[m][1]):
            m=l
        if(r<n and arr[r][1]<arr[m][1]) :
            m=r
        if(m!=i):
            i1=arr[i][0]
            i2=arr[m][0]
            pos[i1]=m
            pos[i2]=i
            arr[m],arr[i]=arr[i],arr[m]
            self.heapifyDown(arr,m,pos)
        
        
    def extractMin(self,arr,pos) :
        if(len(arr)==1) :
            return arr.pop()
        temp=arr[0]
        arr[0]=arr.pop()
        v=arr[0][0]
        pos[v]=0
        self.heapifyDown(arr,0,pos)
        return temp
        
        
 
    
    def dijkstra(self, V, edges, src):
        # code here
        #implememt using heap data str
        arr=[[e,float('inf') ]for e in range(V)]
        pos=[e for e in range(V)]
     
        dis=[float('inf') for e  in range(V)]
        dis[src]=0
        arr[src][1]=0
        self.decreaseKey(arr,src,pos)
        
        adj=[[] for e in range(V)]
        for u,v,w in edges :
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        while(arr) :
            u,d=self.extractMin(arr,pos)
            for v,w in adj[u] :
                if(dis[u]+w < dis[v]) :
                      dis[v]=dis[u]+w
                      ind=pos[v]
                      arr[ind][1]=dis[u]+w
                      self.decreaseKey(arr,pos[v],pos)
        return   dis
            
        
        
         
