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






       import heapq
import sys

def dijkstra(adj, src):

    V = len(adj)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    dist = [sys.maxsize] * V

    # Distance from source to itself is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # Process the queue until all reachable vertices are finalized
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > dist[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adj[u]:

            # If we found a shorter path to v through u, update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    # Return the final shortest distances from the source
    return dist


if __name__ == "__main__":
    src = 0
    
    adj = [
        [(1, 4), (2, 8)],
        [(0, 4), (4, 6), (2, 3)],
        [(0, 8), (3, 2), (1, 3)],
        [(2, 2), (4, 10)],
        [(1, 6), (3, 10)]
    ]
    
    result = dijkstra(adj, src)
    print(*result)
     
        
        
         
