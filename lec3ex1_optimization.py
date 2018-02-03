import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import minimize

def func(X):
    return X[0, ...]**2 + X[1, ...]**2

def grad(X):
    return np.stack((2*X[0, ...], 2*X[1, ...]), axis=0)

# select random starting point and minimize
x0 = np.random.uniform(-5, 5, size=2)
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