import numpy as np
import matplotlib
import matplotlib.pyplot as plt


y = [161, 164, 157, 166, 167, 167, 159, 165, 166, 167]
y.sort()

fig, line = plt.subplots()
line.vlines(3, 167, 158, color='red')

plt.plot(y)

plt.grid()
plt.show()




