from tkinter import*
from numpy.random import*
import time

root = Tk()
root.title('SOLsimulation')
w = 600 #ウィンドウサイズ横
h = w #ウィンドウサイズ縦
na = 500 #ブラインシュリンプの数
c = Canvas(root, width = w, height = h) 
fs = 3

ax = []
ay = []

for i in range(na):
    rx = int(rand()*w)
    ry = int(rand()*w)
    ax.append(rx)
    ay.append(ry)
    c.create_oval(rx, ry, rx+3, ry+3, tags = 'o')

while True:
    c.delete('o')

    for j in range(na):
        #time.sleep(0.1)
        r = int(rand()*8)

        if r == 0:
            ax[j] = ax[j] + int(rand()*fs)
            ay[j] = ay[j] + int(rand()*fs)

        if r == 1:
            ax[j] = ax[j] + int(rand()*fs)
            ay[j] = ay[j] - int(rand()*fs)

        if r == 2:
            ax[j] = ax[j] - int(rand()*fs)
            ay[j] = ay[j] - int(rand()*fs)

        if r == 3:
            ax[j] = ax[j] - int(rand()*fs)
            ay[j] = ay[j] + int(rand()*fs)

        if r == 4:
            ax[j] = ax[j] + int(rand()*fs)

        if r == 5:
            ax[j] = ax[j] - int(rand()*fs)

        if r == 6:
            ay[j] = ay[j] + int(rand()*fs)

        if r == 7:
            ay[j] = ay[j] - int(rand()*fs)


        
        c.create_oval(ax[j], ay[j], ax[j]+3, ay[j]+3, tags = 'o')
        c.pack()
        
    c.update()

root.mainloop()
