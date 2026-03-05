class Solution:
    def dfs(self,u,adj,visited,parent) :
            visited[u]=True
            for v in adj[u] :
                if visited[v]  :
                    if(v!=parent) :
                        return True
                else :
                    if  self.dfs(v,adj,visited,u) :
                       return True
            return False
            
                
    
         
	def isCycle(self, V, edges):
		#Code here
		visited=[False for e in range(V)]
		adj=[[] for e in range(V)]
		for u ,v in edges :
		    adj[u].append(v)
		    adj[v].append(u)
		for e in range(V) :
		    if not visited[e] and self.dfs(e,adj,visited,-1):
	        	return True
	    return False
		
	
		
 
		        
		 
