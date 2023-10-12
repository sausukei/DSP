import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

omegan = 2.0/100.0

zeta = 2.0/100.0

rt = float(1)
dt = 2.5


data = np.arange(-1,4000)
t = [i*dt for i in data]
RT = [rt]*len(t)

print(data,t)
print(len(data),len(t),len(RT))

Kp = 0.3
Ki = 0.0005
Kd = 200

#ちょっと複雑な計算
eledt = 1/(dt**2) # 0.16
sqron = omegan ** 2 #0.0004
ele2zo = (2*zeta*omegan)/dt #0.00032

#eの定義初期値だけ決まってる e=rt-yt
e = [1]
e2 = [1]
e3 = [1]
#yの定義, -1と0の時、初期値0
y = [0,0]
y2 = [0,0]
y3 = [0,0]

#uの定義初期値0
u = [0]
u2 = [0]
u3 = [0]

#Eの定義、前のeにdtをかけたものを加算していくため、-1と0の時は0
E = [0,0]
E2 = [0,0]
E3 = [0,0]

print(t,RT,e,u,y,E)
i = 1
while i < 4000:
    e.append(rt-y[i])
    calcU = Kp*e[i]+Ki*(E[i-1]+dt*e[i])+Kd*((e[i]-e[i-1])/dt)
    u.append(calcU)
    Ymol = (sqron*u[i]+y[i]*((2*eledt)+ele2zo)-(eledt)*y[i-1])
    Yden = ((eledt)+(ele2zo)+(sqron))
    calcY = Ymol/Yden
    y.append(calcY)
    E.append(E[i]+e[i-1]*dt)
    i+=1
e.append(rt-y[i])
calcU = Kp*e[i]+Ki*(E[i-1]+dt*e[i])+Kd*((e[i]-e[i-1])/dt)
u.append(calcU)
print(e,u)
print(len(t),len(RT),len(e),len(u),len(y),len(E))



df = pd.DataFrame({"t":t,"r(t)":RT,"e(t)":e,"u(t)":u,"y(t)":y,"E(t)":E})

df.to_csv("PID.csv")

Kp = 0.3
Ki = 0
Kd = 0

i = 1
while i < 4000:
    e2.append(rt-y2[i])
    calcU = Kp*e2[i]+Ki*(E2[i-1]+dt*e2[i])+Kd*((e2[i]-e2[i-1])/dt)
    u2.append(calcU)
    Ymol = (sqron*u2[i]+y2[i]*((2*eledt)+ele2zo)-(eledt)*y2[i-1])
    Yden = ((eledt)+(ele2zo)+(sqron))
    calcY = Ymol/Yden
    y2.append(calcY)
    E2.append(E2[i]+e2[i-1]*dt)
    i+=1
e2.append(rt-y[i])
calcU = Kp*e2[i]+Ki*(E2[i-1]+dt*e2[i])+Kd*((e2[i]-e2[i-1])/dt)
u2.append(calcU)
print(e2,u2)

Kp = 0.3
Ki = 0.0005
Kd = 0

i = 1
while i < 4000:
    e3.append(rt-y3[i])
    calcU = Kp*e3[i]+Ki*(E3[i-1]+dt*e3[i])+Kd*((e3[i]-e3[i-1])/dt)
    u3.append(calcU)
    Ymol = (sqron*u3[i]+y3[i]*((2*eledt)+ele2zo)-(eledt)*y3[i-1])
    Yden = ((eledt)+(ele2zo)+(sqron))
    calcY = Ymol/Yden
    y3.append(calcY)
    E3.append(E3[i]+e3[i-1]*dt)
    i+=1
e3.append(rt-y3[i])
calcU = Kp*e3[i]+Ki*(E3[i-1]+dt*e3[i])+Kd*((e3[i]-e3[i-1])/dt)
u3.append(calcU)
print(e3,u3)


fig, ax = plt.subplots()

ax.grid()
ax.legend()
ax.plot(t,y)
ax.plot(t,y2)
ax.plot(t,y3)
plt.savefig("a.png")