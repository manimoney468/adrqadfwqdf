# graph_ex = [
#   [0,1,1,0],
#   [1,0,0,1],
#   [1,0,0,1],
#   [0,1,1,0]
# ]


# graph_ex_list = {
#   1: [4,3],
#   3:[1,5],
#   4:[1,5],
#   5:[3,4]
# }

import collections
class graph:
    def __init__(self,gdict=None):
        if gdict is NOne:
            gdict ={}
        self.gdict = gdict
    def bfs(graph, startnode):
    # Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
    def marked(n):
        print(n)
        
gdict = {
        "a" : set(["b","c"]),
        "b" : set(["a","d"]),
        "c" : set(["a","d"]),
        "d" : set(["e"]),
        "e" : set(["a"])
        }
bfs(gdict, "a")        
                              

                            
# Graph is a non-linear data structure cinsistibg of nodes and edges. The nodes are sometimes also reffered to as vertices and the edges are lines or arcs that connect any two nodes in the graoy. More formally a graph can be defined as,

# A Graph consistes of a finite set of vertices(or nodes) and set of edges which connect a pair of nodes.

                        0        1
                                        2
                            /        
                        4        3
                        
# The following are the most commly used representations of a graph

# Adjacency Matrix
# Adjacency List 

# The adjacency matrix for the above example graph is:

        0   1   2   3   4      
        -----------------                 
    0   0   1   0   0   1
    1   1   0   1   1   1
    2   0   1   0   1   0
    3   0   1   1   0   1
    4   1   1   0   1   0
                       
                                                                            
