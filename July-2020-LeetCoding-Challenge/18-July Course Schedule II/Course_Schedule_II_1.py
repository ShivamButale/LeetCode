class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        for p in prerequisites:
            g[p[1]].append(p[0])
        
        vis = [False] * numCourses
        st = [False] * numCourses
        res = []
        
        def dfs(u):
            vis[u] = st[u] = True        
            for v in g[u]:
                if not vis[v]:
                    if not dfs(v):
                        return False
                elif st[v]:               # Trying to visit a node already in current path, so it's a cycle.
                    return False
            st[u] = False            # Backtrack when returning from current path
            res.append(u)         
            return True
        
        f = True
        for x in range(numCourses):
            if not vis[x]:
                f = dfs(x)
            if not f:
                return []
        
        return res[::-1]
