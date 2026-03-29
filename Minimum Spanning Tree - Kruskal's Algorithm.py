#User function Template for python3
from typing import List


class DSU :
    def __init__(self,v) :
        self.parent=[e for e in range(v)]
        self.size=[1]*v
    def find(self,x) :
        if self.parent[x]==x :
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y) :
        px=self.find(x)
        py=self.find(y)
        if px==py :
            return False 
        if self.size[px]>= self.size[py]:
            self.parent[py]=px
            self.size[px]+=self.size[py]
        else :
              self.parent[px]=py
              self.size[py]+=self.size[px]
        return True
              
        
class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        dsu=DSU(V)
        weight=0
        count=1
        edges.sort(key=lambda x :x[2])
        for u,v,w in  edges :
            if dsu.union(u,v) :
                weight+=w
                count++1
            if count==V:
                break
            
        return weight
            
            
            
