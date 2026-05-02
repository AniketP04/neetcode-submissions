class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        visit = [False]*n

        for u,v in edges:

            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(n):
            for nod in adj[n]:
                if not visit[nod]:
                    visit[nod] = True
                    dfs(nod)
        
        count = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                count+=1
        return count