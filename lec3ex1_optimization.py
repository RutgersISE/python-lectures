import numpy as np
import matplotlib.pyplot as plt

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
opt = res.x

# plot function and the optimal point
x = np.linspace(-3, 3, num=500)
y = np.linspace(-3, 3, num=500)
X, Y = np.meshgrid(x, y)
Z = func(np.stack((X, Y), axis=0))
plt.contour(X, Y, Z, 10)
plt.plot(opt[0], opt[1], "r*", ms=10)
plt.show()
