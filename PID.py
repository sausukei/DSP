import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


omegan = 2.0/100.0
zeta = 2.0/100.0

rt = 1
dt = 2.5
t = np.arange(-1,25*dt,dt)



Kp = int(input("Kp "))
Ki = int(input("Ki "))
Kd = int(input("Kd "))




