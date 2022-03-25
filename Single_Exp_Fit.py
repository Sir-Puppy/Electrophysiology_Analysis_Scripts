# -*- coding: utf-8 -*-
#Made 210929 for in Spyder fitting

"Single Exponential fitting that returns TAU and R2"

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

xs = np.arange(12) + 1 # 12 data points, Evenly spaced out
ys = np.array([0,-0.729378909,-0.882950644,-0.922148569,-0.934474881,-0.93882252,-0.940872608,-0.941838795,-0.942224169,-0.942402192,-0.942266627,-0.94244689])

plt.plot(xs, ys, '.')
plt.title("Original Data")

def monoExp(x, m, t, b):
    return m * np.exp(-t * x) + b

# perform the fit
p0 = (2000, .1, 50) # start with values near those we expect
params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0, maxfev=5000)
m, t, b = params
sampleRate = 20_000 # Hz
tauSec = (1 / t) / sampleRate #Attention, this will give you Tau, and not the Inv Tau

# fit parameters
squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
squaredDiffsFromMean = np.square(ys - np.mean(ys))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# plot the results
plt.plot(xs, ys, '.', label="data")
plt.plot(xs, monoExp(xs, m, t, b), '--', label="fitted")
plt.title("Title")

# inspect the parameters
#print(f"Y = {m} * e^(-{t} * x) + {b}")
#print(f"Tau = {tauSec * 1e6} µs")
print(rSquared)
print(t)
print(m)
