#Muhammad Arvito Naufal / 12320026

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

figure, ax = plt.subplots(figsize=(10, 8))
plt.title("Amplitude Response")
plt.xlabel('Wavenumber (1/m)')
plt.ylabel('Amplitude Response (dB)')
plt.subplots_adjust(left=0.25, bottom=0.25)

#fungsi inisial
def amp_resp(k_1,k_2,d,N):
    k_a = np.sin(np.pi*k*d*N)
    k_b = N*np.sin(np.pi*d*k)
    k_c = 20*((np.log10(np.abs(k_a/k_b))))
    k_c = np.clip(k_c, -40, 0)
    return k_c

#input data inisial
d = int(input("masukkan nilai d = "))
N = int(input("masukkan nilai N = "))
k_1 = float(input("masukkan nilai batas atas k = "))
k_2 = float(input("masukkan nilai batas bawah k = "))
k = np.linspace(k_1,k_2,1000)

#set nilai sumbu vertical dengan fungsi amplitude response di atas + plot awal
k_final = amp_resp(k_1,k_2,d,N)
plot, = ax.plot(k, k_final)

#set up untuk matplotlib textbox
d_a = plt.axes([0.25, 0.15, 0.1, 0.02])
N_a = plt.axes([0.25, 0.1, 0.1, 0.02])
Input_d = TextBox(d_a, 'd = ', initial=str(d))
Input_N = TextBox(N_a, 'N = ', initial=str(N))

#fungsi untuk membuat plot baru
def plot_settings(value):
    set_d = int(Input_d.text)
    set_N = int(Input_N.text)
    plot.set_ydata(amp_resp(k_1,k_2,set_d,set_N))
    figure.canvas.draw_idle()

#menghubungkan fungsi plot settings dan textbox
Input_d.on_submit(plot_settings)
Input_N.on_submit(plot_settings)

plt.show()