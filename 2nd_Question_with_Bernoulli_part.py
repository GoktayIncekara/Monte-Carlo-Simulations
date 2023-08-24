import numpy as np
from matplotlib import pyplot as plt

p = 0.5
Y = []

for j in range(1000):
    X = 1
    u = np.random.rand()
    while(u>p):
        X+=1
        u = np.random.rand()
    Y.append(X)

plt.figure()
plt.hist(Y,20,density=True)
plt.show()
