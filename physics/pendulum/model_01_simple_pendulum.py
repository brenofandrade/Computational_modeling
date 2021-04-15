import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')


# Variables

step_time = 0.01
g_aceleration = 10
length_pendulum = 1.5

initial_time = 0
final_time = 50
Nmax = int((final_time-initial_time)/step_time)

theta = np.zeros(Nmax)
omega = np.zeros(Nmax)
time = np.zeros(Nmax)

theta[0] = 0.1
omega[0] = 0.0
time[0] = 0.0
q = 0.25



for i in range(Nmax-1):
    time[i+1] = time[i] + step_time
    omega[i+1] = omega[i] - (g_aceleration/length_pendulum)*theta[i]*step_time - q*omega[i]*step_time
    theta[i+1] = theta[i] + omega[i]*step_time
    
plt.figure(figsize=(11,5))
plt.plot(time, theta,'r-')
plt.title('damped pendulum')
plt.xlabel('time(s)')
plt.ylabel('theta(rad)')
plt.show()