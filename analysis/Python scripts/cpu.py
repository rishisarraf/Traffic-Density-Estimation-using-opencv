import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
data1 = [572.2,562.9, 553.4,544.6 ,544.5,536.9, 540.7,533.8]
data2 = [128,127,123,122,120,118,116,114]
num = [8,7,6,5,4,3,2,1]

fig, ax1 = plt.subplots()

color = 'red'
ax1.set_xlabel('num of threads')
ax1.set_ylabel('%CPU', color=color)
ax1.plot(num, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'blue'
ax2.set_ylabel('Memory(MB)', color=color)  # we already handled the x-label with ax1
ax2.plot(num, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()