import numpy as np
import matplotlib.pyplot as plt

N = 20000          # サンプル数
dt = 1/3       # サンプリング周期 [s]
f1, f2 = 100, 350    # 周波数 [Hz]

t = np.arange(0, N * dt, dt) # 時間 [s]
omega=2.0*np.pi*2.0
x = 5*np.cos(0.2*omega*t)+2*np.cos(omega*t)+np.cos(3*omega*t) # データ

# fig, ax = plt.subplots()
# ax.plot(t, x)
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Signal")
# ax.grid()
# plt.show()

F = np.fft.fft(x)                       # フーリエ変換
freq = np.fft.fftfreq(N, d=dt) # 周波数スケール

# フーリエ変換の結果を正規化
F = F / max(F)

# 振幅スペクトル
Amp = np.abs(F)
fig, ax = plt.subplots()
ax.set_xlim(0,5)
# ax.set_ylim(0,1)

ax.plot(freq, Amp, color="k")
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Amplitude")
ax.grid()
plt.savefig("50Hz.png")
plt.show()