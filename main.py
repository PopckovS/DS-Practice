import numpy as np
import matplotlib
import matplotlib.pyplot as plt


mass = [161, 164, 157, 166, 167, 167, 159, 165, 166, 167]
ca = 163.9
result = 0

for elem in mass:
    result += int(ca - elem)
    print('- ', int(ca - elem))

print('result = ', result)
print('mass = ', np.mean(mass))

# plt.plot(y)
#
# plt.grid()
# plt.show()




