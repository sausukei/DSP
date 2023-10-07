import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


omegan = 2.0/100.0
zeta = 2.0/100.0

rt = 1
dt = 2.5
t = np.arange(-1.0*dt,25.0*dt,dt)
y = []
u = []
e = []

y0 = 0


# Kp = int(input("Kp "))
# Ki = int(input("Ki "))
# Kd = int(input("Kd "))

fig, ax = plt.subplots()
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.grid()
ax.legend()
plt.savefig("widow.png")
plt.show()


print(t)



