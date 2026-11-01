class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            res = n1

            while res!=parent[res]:
                # path compression
                parent[res] = parent[parent[res]]
                res = parent[res]
            return parent[res]
        
        def union(a, b):
            parentA, parentB = find(a), find(b)
            if parentA == parentB:
                return 0
            
            if rank[parentA] > rank[parentB]: # a is the bigger component
                rank[parentA] = rank[parentA] + rank[parentB]
                parent[parentB] = parentA
            else: # b is the bigger component
                rank[parentB] = rank[parentA] + rank[parentB]
                parent[parentA] = parentB
            return 1
        
        connected = n

        for a, b in edges:
            connected-=union(a,b)

        return connected


            
