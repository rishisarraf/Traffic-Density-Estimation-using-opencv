from math import log, exp 
import matplotlib.pyplot as plt

theta = 10

def utility(val):
    out = 1 + exp(theta*val)
    return 1/ out

time = [27, 28, 28, 29, 28, 29, 30, 33]
error = [0.0674, 0.0638, 0.0578, 0.0495, 0.0516, 0.0355, 0.0286, 0.00]
utili  = []

for e in error:
    hey = utility(e)
    utili.append(hey)

print(utili)

plt.plot(time, utili, label = "line")

plt.title('Utility vs time')
  
plt.legend()
plt.show()
