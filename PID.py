import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


omegan = 2.0/100.0
zeta = 2.0/100.0

rt = float(1)
RT=[]
dt = 2.5
t = np.arange(-1*dt,25.0*dt+dt,dt)
y = [0,0]
u = [0,]
e = [1]
E = [0,0]


# Kp = float(input("Kp "))
# Ki = float(input("Ki "))
# Kd = float(input("Kd "))

Kp = 0.01
Ki = 0.00005
Kd = 40

for i in range(len(t)):
    print(i)
    e.append(rt-y[i])

    RT.append(1)

    E.append(E[i]+e[i-1]*dt)
    calcU=(Kp*e[i])+(Ki*(E[i-1]+dt*e[i]))+(Kd*((e[i]-e[i-1])/dt))
    u.append(calcU)
    Ymol = (omegan*omegan*u[i]+y[i]*((2/dt*dt)+(2*zeta*omegan/dt))-(1/dt*dt)*y[i-1])
    Yden = ((1/(dt*dt))+(2*zeta*omegan/dt)+(omegan*omegan))
    calcY= float(Ymol/Yden)
    y.append(calcY)

        

t = np.append(t,1)
t = np.append(t,1)
e.append(0)
RT.append(0)
RT.append(0)

u.append(0)

y0 = 0

print(len(t),len(RT),len(e),len(u),len(y),len(E))
df = pd.DataFrame({"t":t,"r(t)":RT,"e(t)":e,"u(t)":u,"y(t)":y,"E(t)":E})

df.to_csv("PID.csv")

fig, ax = plt.subplots()
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Amplitude")
ax.grid()
ax.legend()
plt.savefig("widow.png")



print(t)



