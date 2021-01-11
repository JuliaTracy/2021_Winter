import scipy.integrate as spi
import numpy as np
from matplotlib import pyplot as plt
beta=3.8
gamma=0.09
TS=1.0
ND=40.0
S0=1-2.89e-5
I0=2.89e-5
INPUT = (S0, I0, 0.0)

def diff_eqs(INP,t):
	Y=np.zeros((3))
	V = INP
	Y[0] = - beta * V[0] * V[1]
	Y[1] = beta * V[0] * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y
 
t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)
 
print(RES)

plt.plot(RES[:,1], '-ro', label='Infected')
plt.plot(RES[:,0], '-bs', label='Suspected')
plt.plot(RES[:,2], '-g^', label='Recovered')
plt.legend(loc=0)
plt.title('SIR_Model.py')
plt.xlabel('Time')
plt.ylabel('Infected, Suspected and Recovered')
plt.show()
