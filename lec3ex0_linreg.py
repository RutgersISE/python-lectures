""" Lecture 3 Exercise 0 : Linear Regression """

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import linregress
# note: there are many libraries with linear regression. 
# I just used scipy because it had a convenient interface. 
# statsmodels and sklearn also have great linear regression
# options. 

# generate some random data
n = 100
x_obs = np.random.uniform(0, 10, size=n)
y_obs = 3*x_obs + 2 + np.random.normal(loc=0, scale=5, size=n)

# compute linear regression and trendline
slope, intercept, _, _, _ = linregress(x_obs, y_obs)
x_trend = np.array([0, 10])
y_trend = slope*x_trend + intercept

# plot the data and trendline
plt.scatter(x_obs, y_obs, c="k", marker="x", label="Observed")
plt.plot(x_trend, y_trend, c="r", label="Trend")
plt.title("Randomly Generated Data")
plt.legend()
plt.show()
#plt.savefig("linreg.jpg") # uncomment to save to file