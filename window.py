# ライブラリ読み込み
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import cmath
from scipy import signal

# 変数定義
fs = input("サンプリング周波数[Hz]")
dt = 1.0/float(fs)
t = dt
i = 0
y=[]
omega=2.0*math.pi*1.0

# 計測データの作成
time = input("計測時間[sec]")
while t<=float(time):
    y.append(1000*np.cos(omega*t))
    t += dt
    i+=1
y_copy = y.copy()

hanning = y*np.hanning(len(y))
hamming = y*np.hamming(len(y))
blackman = y*np.blackman(len(y))

print(hanning)


hanning = np.append(hanning,hanning)
hamming = np.append(hamming,hamming)
blackman= np.append(blackman,blackman)

sec = np.arange(0,11,(5.5*2)/len(y*2))

fig, ax = plt.subplots()
ax.plot(sec, hanning, label = "hanning")
ax.plot(sec, hamming, label = "hamming")
ax.plot(sec, blackman, label = "blackman")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.grid()
ax.legend()
plt.savefig("widow.png")
plt.show()



y = y + y_copy


# # print(x,datanum)

# df = pd.DataFrame({"data": y})
# print(df)

# # dftする関数
# def DFT(f):
#     N = len(f)
#     A = np.arange(N)
#     calc = np.exp(-1j * A.reshape(1,-1)* A.reshape(-1, 1) * 2 * cmath.pi / N) 
#     # dftの公式から計算 reshapeは行列定義で,
#     # 列ベクトルと行ベクトルを作成し、掛け算することでfor文をなくす工夫.
#     return np.sum(f*calc, axis=1)
#     # 計算結果の総和をリストで返す.

# def hunning(f):
#     n = 100
    
#     ht = dt
#     tmp = []
    
#     for i in f:
#         homega=2.0*np.pi*ht
#         calc = (1-np.cos(homega/n))/2
#         tmp.append(float(i)*calc)
#         ht+=dt
    
#     return tmp    


# name = str(fs)+"Hz_"+str(time)+"sec" # ファイル名の作成.
# filename = "csv/window"+name+".csv" # csvファイル名.
# fig,ax = plt.subplots()
# ax.set_xlabel("time[sec]")
# signalTime = np.arange(0,float(time)*2,float(time)*2/len(y)) # 横軸の作成
# ax.plot(signalTime,y,color = "k")
# plt.savefig("image/window/source"+name+".png") # 作成したグラフの保存先.
# plt.show() # グラフの表示.
# df.to_csv(filename) # 作成したデータフレームをcsvで保存.

# result = hunning(y)
# hdata = pd.DataFrame(result)
# hdata.plot(color="k")
# plt.savefig("image/window/hanning/hanning.png")
# plt.show()

# freq = np.arange(0,50,(50/len(y)))


# window = np.blackman(len(y))


# result = DFT(y*window)
# print(result)
# s=pd.Series(result)
# Amp = np.abs(result/(max(np.abs(result)))) #規格化

# df2 = pd.DataFrame({"data": result})
# print(df2)
# fig,ax = plt.subplots()
# ax.set_xlabel("frequecy [Hz]")
# df2.to_csv("csv/result"+name+".csv")
# freq = np.arange(0,50,(50/len(y)))
# sec = np.arange(0,11,(5.5*2)/len(y))
# ax.plot(sec,Amp,color="k")
# ax.set_xlim(0,float(time))

# plt.savefig("image/window/dftbla"+name+".png")
# plt.show()