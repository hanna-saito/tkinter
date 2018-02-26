from tkinter import*
from numpy.random import*
import time

root=Tk()
root.title('Senses of Light') #ウィンドウタイトル
w = 600
h = w

c=Canvas(root, width=w, height=h,) #canvas作成

ll = [[0,0,0],[0,0,0],[0,0,0]] #ライトフェイスの初期状態　0 = 点灯　1 = 消灯

def Lighface(ll):
    ry = []  
    rx = []
    cs = int(h/3)

    for i in range(3):
        ry.append(i*cs)
        rx.append(i*cs)

        l1 = 0
        l2 = 0
    

    for i in rx:
        l2 = 0
        for j in ry:
            if ll[l1][l2] == 1:
                g1 = 99
                c.create_rectangle(i,j,i+cs,j+cs, fill = '#005005005', outline = 'black', tags = 'b')
        
            elif ll[l1][l2] == 0:
                g1 = 1
                c.create_rectangle(i,j,i+cs,j+cs, fill = 'white', outline = 'white', tags = 'w')

            l2 = l2+1
        l1 = l1+1

    c.pack()

def Randomnum():
    nl = [] 
    nln = 0
    
    for i in range(9):
        nl.append(int(rand()*10))

    print(nl)

    for i in range(3):
        for j in range(3):
            if nl[nln] >= 5:
                ll[i][j] = 1
            elif nl[0] <= 5:
                ll[i][j] = 0
            nln = nln+1

    print(ll) 

#main

print(ll)

while True:
    time.sleep(1)
    Lighface(ll)
    Randomnum()
    c.update()

root.mainloop()