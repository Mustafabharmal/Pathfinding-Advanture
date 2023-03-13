
from random import *
from settings import *
import networkx as nx

qustions = {

    "what is the degree of any node of compelete graph with 5 vertices?" : '4',
    "what is the no. of edges of a compelete graph with 5 vertices?" : '10',
    "what is the no. of spanning tree we get from K5?" : '125',
    "Can a regular graph with degree 4 be Euler graph? YES or NO" :'yes',
    "Consider a simple undirected graph of 10 vertices. If the graph is disconnected, then the maximum number of edges it can have is __" : "36",
    "In network topology, the property between two graphs so that both have got same Incidence matrix is known as" : "isomorphism"
}
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index += 1
    return []


GRAPH_EDGES = [
    (5372,9697),
    (5372,4391),
    (9697,6921),
    (7397,5933),
    (9397,6315),
    (7697,6315),
    (6921,2320),
    (6921,7013),
    (6921,5805),
    (2320,4391),
    (2320,2265),
    (2320,7464),
    (2320,6315),
    (4391,4687),
    (4391,5767),
    (4391,5372),
    (2265,5705),
    (2265,5402),
    (2265,5403),
    (7464,5933),
    (7464,6315),
    (7464,5372),
    (6315,7397),
    (6315,6921),
    (6315,9697),
    (5933,7464),
    (4687,6672),
    (6672,5767),
    (6672,7052),
    (6672,3896),
    (7052,3896),
    (5767,7052),
    (5767,3896),
    (3896,6330),
    (3896,2663),
    (2663,2888),
    (2663,1054),
    (2888,6330),
    (2888,4053),
    (2888,5403),
    (6330,5403),
    (6330,5705),
    (4053,5403),
    (4053,3454),
    (3454,5403),
    (3454,1054),
    (3454,1999),
    (1999,5403),
    (1999,5402),
    (1999,1436),
    (1436,1054),
    (1436,5805),
    (5402,2265),
    (5402,5403),
    (2265,5403),
    (2265,5705),
    (2265,2320),
    (5705,6330),
    (5705,5403),
    (7013,8821),
    (8821,9243),
    (8821,7110),
    (1054,8549),
    (8549,6709),
    (8549,5000),
    (6709,5000)
]
print(len(GRAPH_EDGES))
GRAPH_EDGES = set(GRAPH_EDGES)
GRAPH_EDGES = list(GRAPH_EDGES)
print(len(GRAPH_EDGES))

H=nx.Graph()
for i in GRAPH_EDGES:
    H.add_edge(*i)

max=0
node_traversal_longest_shortest_path=[]
start_node = choice(KEYS)

while(start_node == 5805):
    start_node = choice(KEYS)
print(start_node)
for j in range(0,len(H.nodes())):
    x = len(shortest_path(H,start_node,list(H.nodes())[j]))
    if x > max:
        max = x
        node_traversal_longest_shortest_path = shortest_path(H,start_node,list(H.nodes())[j])

print(max)
print(node_traversal_longest_shortest_path)

orig_shortest_path_length = len(node_traversal_longest_shortest_path)
