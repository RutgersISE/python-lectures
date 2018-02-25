import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import cdist

def plot_tsp(path, coords):
    """ plots a solved tsp """
    plt.scatter(coords[:, 0], coords[:, 1])
    for i, j in list(zip(path[1:], path[:-1])) + [(path[-1], path[0])]:
        x, y = coords[i, 0], coords[i, 1]
        dx, dy = coords[j, 0] - coords[i, 0], coords[j, 1] - coords[i, 1]
        plt.arrow(x, y, dx, dy, shape='full', lw=1, length_includes_head=True, head_width=0)
    plt.show()    

def path_length(path, dist):
    """ computes the length of a solved tsp """ 
    length = dist[-1, 1]
    for i, j in zip(path[1:], path[:-1]):
        length += dist[i, j]
    return length

def solve_tsp(dist):
    """ THIS IS THE FUNCTION YOU SHOULD UPDATE """
    path = list(range(len(dist)))
    length = path_length(path, dist)
    return path, length

if __name__ == "__main__":
    np.random.seed(1000) # CHANGE YOUR SEED TO YOUR GROUP NUMBER
    coords = np.random.uniform(0, 10, size=(25, 2))
    dist = cdist(coords, coords)

    path, length = solve_tsp(dist)
    print("path found:", path)
    print("length of path: ", length)
    
    plot_tsp(path, coords)
