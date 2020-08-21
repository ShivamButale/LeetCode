class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        solution = []
    
        def dfs(vertex, edge):
            if edge[-1] == len(graph)-1:
                solution.append(edge)
                return 
            for vertice in graph[vertex]:
                dfs(vertice, edge+[vertice])
                
        dfs(0, [0])
        return solution
        
