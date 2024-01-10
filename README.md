# Treasure Hunt Game

## Introduction 🎮
Treasure Hunt is an interactive and educational game designed to enhance your understanding of graph theory concepts. It combines graphical gameplay with quiz challenges related to graph theory.

## Features 🚀
1. **Graph Theory Challenges:** Explore the world filled with nodes and edges, representing a graph. Solve graph theory questions to progress in the game.

2. **Interactive Map:** Navigate through the game world, filled with obstacles and exciting graphical elements, using arrow keys or on-screen controls.

3. **Quiz Dialogs:** Engage in dialogues with different characters represented by graph nodes. Answer graph theory questions correctly to unlock new areas and challenges.

4. **Dynamic Graphics:** Enjoy visually appealing graphics, including grassy terrains, objects, and obstacles. Each element is strategically placed to create an immersive gaming experience.

5. **Graph Representation:** The game uses a graphical representation of a graph, where nodes represent locations and edges represent connections between them. Explore the connections and find the treasure!

## How to Play 🕹️
1. Launch the game using `main.py`.
2. Navigate the main menu to start playing or exit the game.
3. Solve graph theory questions to progress through the game.
4. Explore the map, answer questions from characters, and reach the treasure!

## Algorithms Overview 🧠

### Shortest Path Algorithm
The game employs a breadth-first search algorithm to find the shortest path between nodes. This algorithm efficiently explores the graph, ensuring the player can navigate through the map and reach the treasure.

```python
#inside the TH_terminal.py

def shortest_path(graph, node1, node2):
```
### Graph Matching
Nodes in the graph are matched based on their connections (edges). The game uses NetworkX to represent the graph and find matches, ensuring proper traversal and interaction between nodes.

```python
#inside the TH_terminal.py

import networkx as nx

# Create a graph using NetworkX
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(node1, node2), ...])

```
## Dependencies 🔗

Ensure you have Python installed on your system. If not, download and install it from the official [Python website](https://www.python.org/).

Install the required Python libraries using the following command:

```bash
pip install pygame pillow networkx easygui
```

## Technical Details 🔧

The Treasure Hunt game is developed using Python and several key libraries for different functionalities:

### Tkinter
- **Purpose:** Tkinter is used for creating the main menu interface of the game.
- **Implementation:** The main menu is initialized using Tkinter, allowing users to navigate through options such as starting the game or exiting.

### Pygame
- **Purpose:** Pygame is employed to manage the graphical aspects of the game, including player movement, rendering, and handling user input.
- **Implementation:** Graphics such as terrains, objects, and characters are displayed using Pygame. Player controls are managed to navigate through the map.

### PIL (Pillow)
- **Purpose:** PIL (Python Imaging Library, or Pillow) is utilized for image processing and displaying graphics.
- **Implementation:** Images, including background graphics and character sprites, are loaded, processed, and displayed using PIL.

### NetworkX
- **Purpose:** NetworkX is a powerful library for the creation, manipulation, and study of complex networks or graphs.
- **Implementation:** The game uses NetworkX to represent the graph structure of the game world. Nodes represent locations, and edges represent connections between them. Graph algorithms, such as finding the shortest path, are implemented using NetworkX.

### EasyGui
- **Purpose:** EasyGui simplifies the creation of GUIs by providing easy-to-use dialog boxes for user interaction.
- **Implementation:** Dialog boxes are used for quiz questions and answers, allowing users to engage with characters in the game. EasyGui enhances the interactive elements of the game.

These libraries collectively contribute to the functionality and aesthetics of the Treasure Hunt game, providing an engaging and educational gaming experience.

## Enjoy the Treasure Hunt adventure! 🌟
