""" Lecture 3 Exercise 1 : Optimization """

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.optimize import minimize
# note: scipy.optimize focuses on smooth 
# multivariate functions. For more specific
# functions, there's generally a better option. 
# For linear programming: PuLP (if modeling is the focus)
# For convex programming: cvxopt
# For global optimization: scikit-opt

def func(X):
    """ x_1**2 + x_2**2 + ... + x_n**2 """
    return np.sum(np.square(X), axis=0)

def grad(X):
    """ 2*x_1, 2*x_2, ..., 2*x_n """
    return 2*X

# select random starting point and minimize
x0 = np.random.uniform(-3, 3, size=2)
res = minimize(func, x0, jac=grad)
print("optimal x =", res.x)
opt_x = res.x
opt_fun = res.fun

# plot function and the optimal point
x = np.linspace(-3, 3, num=500)
y = np.linspace(-3, 3, num=500)
X, Y = np.meshgrid(x, y)
Z = func(np.stack((X, Y), axis=0))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, alpha=.25)
ax.scatter([opt_x[0]], [opt_x[1]], [opt_fun], c="r")
plt.show()
