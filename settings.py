from random import randint

# game setup
WIDTH    = 1920	
HEIGTH   = 1080
FPS      = 60
TILESIZE = 64

DIALOG_OBJECT = {
    (2368, 1024): "5372",
    (6464, 1088): "9697",
    (640, 1280): "8305",
    (3328, 1728): "5933",
    (5504, 1728): "7397",
    (11904, 1920): "9243",
    (10944, 3008): "8821",
    (9920, 3136): "7013",
    (3264, 3520): "7464",
    (5568, 3520): "6315",
    (6592, 4288): "6921",
    (2496, 4352): "4391",
    (4480, 4352): "2320",
    (1344, 4416): "4687",
    (10688, 4480): "7110",
    (4672, 5184): "2265",
    (2240, 5376): "5767",
    (1344, 5440): "6672",
    (3840, 5760): "5705",
    (5696, 5760): "5402",
    (6336, 5888): "5805",
    (7488, 6464): "1436",
    (3264, 6592): "6330",
    (4736, 6592): "5403",
    (1344, 6656): "7052",
    (2176, 6656): "3896",
    (6336, 6656): "1999",
    (3776, 7552): "2888",
    (5632, 7552): "3454",
    (4800, 8064): "4053",
    (7360, 8576): "1054",
    (2368, 8896): "2663",
    (8576, 9216): "5000",
    (7488, 9920): "8549",
    (8000, 11456): "6709"
}
KEYS = [
    5372,
    9697,
    8305,
    5933,
    7397,
    9243,
    8821,
    7013,
    7464,
    6315,
    6921,
    4391,
    2320,
    4687,
    7110,
    2265,
    5767,
    6672,
    5705,
    5402,
    5805,
    1436,
    6330,
    5403,
    7052,
    3896,
    1999,
    2888,
    3454,
    4053,
    1054,
    2663,
    5000,
    8549,
    6709
]

# GRAPH_EDGES = [(1,2),(2,3)]
GRAPH_EDGES = [
    (5372,9697),
    (5372,4391),
    (5372,8305),
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

QUESTIONS = {
    # "math-riddle-2.jpg" : '10'
    "edge connectivity of circuit is: " : '2',
    "edge connectivity of circuit is: " : '2',
    "edge connectivity of tree is : " : '1',
    "Vertex with degree 1 is known as: " : 'pendant vertex',
    "Tree can have circuit. true or false: " : 'false',
    "no of edges in a tree with 26 vertices is : " : '25', 
    "Is adjacency mtrix always symmetric for directed graphs? yes or no: " : 'no', 
    "Is adjacency mtrix always symmetric for undirected graphs? yes or no: " : 'yes', 
    "is every tree a bipartite graph" : 'yes', 
    "chromatic no. for K(34,21): " : '2',
    "chromatic no. for K(34): " : '34',
    "is minimum weight of spanning tree always uniQe?" : 'yes',
    "what is the degree of any node of compelete graph with 5 vertices?" : '4',
    "what is the no. of edges of a compelete graph with 5 vertices?" : '10',
    "what is the no. of spanning tree we get from K5?" : '125',
    "Can a regular graph with degree 4 be Euler graph? YES or NO" :'yes',
    "Consider a simple undirected graph of 10 vertices. If the graph is disconnected, then the maximum number of edges it can have is __" : "36",
    "In network topology, the property between two graphs so that both have got same Incidence matrix is known as" : "isomorphism",
    "Let G be a connected planar graph with 10 vertices. If the number of edges on each face is three, then the number of edges in G is__" : "24",
    "_______ of graph is a vertex whose removal disconnects graph."  : "cut vertex",
    "The minimum number of colours that is sufficient to vertex-colour a planar graph is_______":"4"
}

WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]