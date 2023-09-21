# ライブラリ読み込み.
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import cmath

# 変数定義.
fs = input("周波数") # 周波数は任意で決定.
dt = 1.0/float(fs) # 刻み幅.
t = dt
i = 0
x=[]
omega1=2.0*np.pi*20.0
omega2=2.0*np.pi*50.0


# 計測データの作成.
time = input("計測時間")
while t<=float(time):
    x.append(10*np.sin(omega1*t)+5*np.sin(omega2*t))
    t += dt
    i+=1

df = pd.DataFrame({"data": x}) # 計測データをデータフレームとして保存.
print(df)

# dftする関数.
def DFT(f):
    N = len(f) # データ数.
    A = np.arange(N) # 0からN-1までのデータ数分の配列.
    calc = np.exp(-1j * A.reshape(1,-1)* A.reshape(-1, 1) * 2 * cmath.pi / N) 
    # dftの公式から計算 reshapeは行列定義で,
    # 列ベクトルと行ベクトルを作成し、掛け算することでfor文をなくす工夫.
    return np.sum(f*calc, axis=1)
    # 計算結果の総和をリストで返す.
    

name = str(fs)+"Hz_"+str(time)+"sec" # ファイル名の作成.
filename = "csv/"+name+".csv" # csvファイル名.
fig,ax = plt.subplots()
ax.set_xlabel("time[sec]")
signalTime = np.arange(0,float(time),float(time)/len(x)) # 横軸の作成
ax.plot(signalTime,x,color = "k")
plt.savefig("image/source/"+name+".png") # 作成したグラフの保存先.
plt.show() # グラフの表示.
df.to_csv(filename) # 作成したデータフレームをcsvで保存.

window = np.hanning(len(x))
result = DFT(x*window) # 元データをdftする.
print(result) # dftの表示.


df2 = pd.DataFrame({"data": result}) # dftの結果をデータフレーム化
print(df2)
df2.to_csv("csv/result"+name+".csv") # 結果をcsvに保存

fig,ax = plt.subplots() # グラフ領域の定義
ax.set_xlabel("frequecy [Hz]") # 横軸ラベル


Amp = np.abs(result/(max(np.abs(result)))) #規格化.
freq = np.arange(0,float(fs),float(fs)/len(x)) # 横軸の決定
# plt.xticks(np.arange(0,float(fs),float(fs)*7/len(x)))
ax.plot(freq,Amp,color="k") # プロット
ax.set_xlim(90,120) # 横軸の領域の決定
plt.savefig("image/dft/"+name+".png") # ファイル保存先

plt.show() # グラフ表示
