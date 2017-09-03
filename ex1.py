
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

fs = 60     #frequência de amostragem
f = 25      # RA: 171730
size = 60   # Ts = 0.016s --> Para ter 1s no eixo x, multiplica por 60

# Cria vetor do tempo
t = range(size)
t = np.array(range(size))/float(fs)

# w = 2pif
x1 = np.cos(2*np.pi*f*t)

#plota gráfico do sinal com as amostragens
plt.figure()

# -- dashed line
# g  green
# o  circle marker
plt.plot(t, x1, '--go')
plt.xlabel('Tempo [s]')
plt.title('Sinal x1 com Frequência de amostragem = 60 Hz')
plt.show()

# Calcula o espectro do sinal absoluto
X1 = np.fft.fft(x1)
y1 = np.abs(X1)
plt.figure()
plt.plot(y1)
plt.xlabel('Frequência')
plt.title('Módulo do espectro do sinal x1[n] com fs = 60Hz')
plt.ylabel('A/N')
plt.show()


# frequência de amostragem com 200Hz a mais
fs = fs + 200
size = size + 200
# Cria vetor do tempo
t = range(size)
t = np.array(range(size))/float(fs)

# w = 2pif
x2 = np.cos(2*np.pi*f*t)

plt.figure()
plt.plot(t, x2, '--go')
plt.xlabel('Tempo [s]')
plt.title('Sinal x2 com Frequência de amostragem = 260 Hz')
plt.show()

X2 = np.fft.fft(x2)
y2 = np.abs(X2)
plt.figure()
plt.plot(y2)
plt.xlabel('Frequência')
plt.title('Módulo do espectro do sinal x2[n] com fs = 260 Hz')
plt.ylabel('A/N')
plt.show()

#senoide
fs = 260    # Fs que é variada para observar os efeitos no espectro
fsin = 60
size = fs

# Cria senoide com Fsin = 60 Hz
t = range(size)
t = np.array(range(size))/float(fs)
sin = np.sin(2*np.pi*fsin*t)

# Cria sinal cosseno com f = 25Hz
f = 25

t = range(size)
t = np.array(range(size))/float(fs)
x2 = np.cos(2*np.pi*f*t)

# Soma os dois sinais e plota o gráfico
x3 = x2 + sin
plt.figure()
plt.plot(t, x3, '--go')
plt.xlabel('Tempo [s]')
plt.title('Gráfico de amostragem da soma dos sinais X2 e sin')
plt.show()

# Calcula o espectro absoluto
X3 = np.fft.fft(x3)
y3 = np.abs(X3)
plt.figure()
plt.plot(y3)
plt.xlabel('Frequência')
plt.title('Módulo do espectro do sinal x2[n] + sin com fs = ' + str(fs) + ' Hz')
plt.ylabel('A/N')
plt.show()
