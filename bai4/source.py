import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.discrete.transforms import fft
from sympy.discrete.transforms import ifft
Fs = 100                       # sampling rate
Ts = 1.0/Fs                      # sampling interval
t = np.arange(0,1,Ts)            # time vector
ff = 5                           # frequency of the signal
#y = np.random.randn(Fs)
y = np.sin(2 * np.pi * ff * t)
plt.subplot(3,1,1)
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(3,1,2)
Y = fft(y)# fft computing and normalization
y1 = []
for i in Y:
    i = complex(i)
    y1.append(abs(i.real))
print(y1)
n1 = len(y1)//2
plt.plot(range(n1),y1[0:n1], 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.show()

