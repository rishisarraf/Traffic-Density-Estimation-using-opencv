from math import log, exp 
import matplotlib.pyplot as plt

time = [33,32, 29, 28, 29, 30, 28, 27]
num_thread = [1,2,3,4,5,6,7,8]

plt.plot(num_thread, time, label = "line")

plt.title('Runtime vs num of threads')
  
plt.legend()
plt.show()