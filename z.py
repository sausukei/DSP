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
    x.append(10*np.sin(omega1*t)+5*np.sin(omega2*t)) # 信号
    t += dt
    i+=1

N = int(input("移動度"))

def DFT(f):
    N = len(f) # データ数.
    A = np.arange(N) # 0からN-1までのデータ数分の配列.
    calc = np.exp(-1j * A.reshape(1,-1)* A.reshape(-1, 1) * 2 * cmath.pi / N) 
    # dftの公式から計算 reshapeは行列定義で,
    # 列ベクトルと行ベクトルを作成し、掛け算することでfor文をなくす工夫.
    return np.sum(f*calc, axis=1)
    # 計算結果の総和をリストで返す.


#移動平均関数
def skipMove(f,N):
    z = []
    i = 0
    k = N-1
    for i in range(k,len(f)-k):# 値が存在する範囲でループ
        # 前後の数字を参照
        a = f[i]
        a_minus_1 = f[i - k:i] #0からk番目までの値を全て取得
        calc = float(a+sum(a_minus_1)/N) 
        z.append(calc)
    
    

    return z


skip = skipMove(x,N)
result = DFT(skip)

df = pd.DataFrame({"data": x}) # 計測データをデータフレームとして保存.

name = str(fs)+"Hz_"+str(time)+"sec"+str(N) # ファイル名の作成.
filename = "csv/"+name+".csv" # csvファイル名.
fig,ax = plt.subplots()
ax.set_xlabel("time[sec]")
signalTime = np.arange(0,float(time),float(time)/len(skip)) # 横軸の作成
ax.plot(signalTime,skip,color = "k")
ax.set_xlim(0,0.3)
plt.savefig("image/source/3"+name+".png") # 作成したグラフの保存先.
plt.show() # グラフの表示.
df.to_csv(filename) # 作成したデータフレームをcsvで保存.

df1 = pd.DataFrame({"data":x})
df = pd.DataFrame({"data": skip}) # 計測データをデータフレームとして保存.
print(df)
print(df1)

Amp = np.abs(result)
fig,ax = plt.subplots() # グラフ領域の定義
ax.set_xlabel("frequecy [Hz]") # 横軸ラベル
# Amp = np.abs(result/(max(np.abs(result)))) #規格化.
freq = np.arange(0,float(fs),float(fs)/len(skip)) # 横軸の決定
# plt.xticks(np.arange(0,float(fs),float(fs)*7/len(x)))
ax.plot(freq,Amp,color="k") # プロット
ax.set_xlim(0,float(fs)/2) # 横軸の領域の決定
plt.savefig("image/"+name+".png") # ファイル保存先
plt.show()