# the spelled out intro to neural networks and backpropagation- building a micrograd
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**2 - 4*x + 5

#print(f(3.0))
xs = np.arange(-5, 5, 0.25)
#print(f(xs))
#plt.plot(xs, f(xs))
#plt.show()
h = 0.001
x = 3
#print(f(x+h))
