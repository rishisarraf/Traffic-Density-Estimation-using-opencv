from math import log, exp 
import matplotlib.pyplot as plt

theta = 0.1

def utility(val):
    out = 1 + exp(theta*val)
    return 1/ out


n = [2,3,4,5,7,10,20,30]
# time = [27.059414, 25.652809, 25.254792, 23.460330, 22.951533, 22.437487, 22.271877, 20.944003, 20.112003]
error = [0.0278, 0.0305, 0.0393, 0.0458, 0.0626, 0.0865, 0.1329, 0.1538]
utili  = []

for e in error:
    hey = utility(e)
    utili.append(hey)

print(utili)

plt.plot(n, utili, label = "line")

plt.title('Utility vs n')
  
plt.legend()
plt.show()
