""" Lecture 3 Exercise 2 : Graphs """

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from scipy.spatial import KDTree
from scipy.spatial import distance_matrix

np.random.seed(100)

# generate random coordinates, a distance matrix, and 
# convert into a graph.
n_nodes = 100
min_x, max_x = 0, 100
coords = np.random.uniform(min_x, max_x, size=(n_nodes, 2))


# compute distance matrix and convert to graph - two methods. 

# this method is conceptually simpler.
distance = distance_matrix(coords, coords) 
graph = nx.from_numpy_matrix(distance)

# This method will scale better as n_nodes increases. (try n_nodes = 5000)
#kdtree = KDTree(coords)
#max_distance = 250*(max_x - min_x)/n_nodes
#distance = kdtree.sparse_distance_matrix(kdtree, max_distance=max_distance)
#graph = nx.from_scipy_sparse_matrix(distance)

tree = nx.minimum_spanning_tree(graph)

pos = dict((i, coords[i]) for i in graph.nodes)
nx.draw(tree, pos=pos, node_size=50)
plt.show()