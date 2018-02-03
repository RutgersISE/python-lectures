""" Lecture 3 Exercise 2 : Graphs """

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from scipy.spatial.distance import pdist, squareform

np.random.seed(100)

# generate random coordinates, a distance matrix, and 
# convert into a graph.
coords = np.random.uniform(0, 10, size=(30, 2))
distance = squareform(pdist(coords))
graph = nx.from_numpy_matrix(distance)

# compute minimum spanning tree
tree = nx.minimum_spanning_tree(graph)

pos = dict((i, coords[i]) for i in graph.nodes)
nx.draw(tree, pos=pos, node_size=100)
plt.show()