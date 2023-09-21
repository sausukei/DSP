import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 20000          # サンプル数
dt = 1/3       # サンプリング周期 [s]
f1, f2 = 100, 350    # 周波数 [Hz]

t = np.arange(0, N * dt, dt) # 時間 [s]
omega=2.0*np.pi*1.0
x = 1000*np.cos(omega*t)# データ

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

window = signal.hann(N)  # ハニング窓関数

fig, ax = plt.subplots()
ax.plot(t, window)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
ax.grid()
plt.show()

# 高速フーリエ変換
F = np.fft.fft(x * window)
freq = np.fft.fftfreq(N, d=dt) # 周波数スケール

# フーリエ変換の結果を正規化
F = F / (N / 2)

# 窓関数による振幅減少を補正する
F = F * (N / np.sum(window))

# 振幅スペクトル
Amp = np.abs(F)
fig, ax = plt.subplots()
ax.plot(freq[:N//2], Amp[:N//2])
ax.set_xlabel("Frequency [Hz]")
ax.set_ylabel("Amplitude")
ax.grid()
plt.show()