""" Lecture 4 Exercise 0 : Linear Regression Class """

import numpy as np

from scipy.stats import linregress

class LinearRegressor(object):
    # TODO finish this

# generate some random data
n = 100
x_obs = np.random.uniform(0, 10, size=n)
y_obs = 3*x_obs + 2 + np.random.normal(loc=0, scale=5, size=n)

# compute linear regression and trendline
slope, intercept, _, _, _ = linregress(x_obs, y_obs)
x_trend = np.array([0, 10])
y_trend = slope*x_trend + intercept
