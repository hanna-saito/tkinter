from tkinter import*
from numpy.random import*
import time

root=Tk()
root.title('Senses of Light')
w = 600
h = w
na = 20
d = 5 
ll = [[0,0,0],[0,0,0],[0,0,0]] #ライトフェイスの初期状態　0 = 点灯　1 = 消灯

c=Canvas(root, width=w, height=h,)

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
            print(l1, l2)
            if ll[l1][l2] == 1:
                c.create_rectangle(i,j,i+cs,j+cs, fill = 'black', outline = 'black', tags = 'b')
        
            elif ll[l1][l2] == 0:
                c.create_rectangle(i,j,i+cs,j+cs, fill = 'white', outline = 'white', tags = 'w')

            l2 = l2+1
        l1 = l1+1

    c.pack()
                

def Brounshrimp_d(na):

    for i in range(na):
        rx = int(rand()*w)
        ry = int(rand()*w)
        ax.append(rx)
        ay.append(ry)
        c.create_oval(rx, ry, rx+3, ry+3, tags = 'o')



def Brounshrimp(na):

    c.delete('o')

    for j in range(na):
        #time.sleep(0.1)
        r = int(rand()*4)

        if r == 0:
                ax[j] = ax[j] + int(rand()*2)
                ay[j] = ay[j] + int(rand()*2)

        if r == 1:
                ax[j] = ax[j] + int(rand()*2)
                ay[j] = ay[j] - int(rand()*2)

        if r == 2:
                ax[j] = ax[j] - int(rand()*2)
                ay[j] = ay[j] - int(rand()*2)

        if r == 3:
                ax[j] = ax[j] - int(rand()*2)
                ay[j] = ay[j] + int(rand()*2)       

        
        c.create_oval(ax[j], ay[j], ax[j]+3, ay[j]+3, tags = 'o')


    #BS位置座標を場所ごとに分ける

    if ax[j] <= h/3 and ay[j] <= h/3 and ax[j] >= 0 and ay[j] >= 0:
                    la.append([ax[j],ay[j]])

    elif ax[j] <= h*2/3 and ay[j] <= h/3 and ax[j] >= 0 and ay[j] >= 3/h:
                    lb.append([ax[j],ay[j]])

    elif ax[j] <= h and ay[j] <= h/3 and ax[j] >= h*2/3 and ay[j] >= 0:
                    lc.append([ax[j],ay[j]])

    elif ax[j] <= h/3 and ay[j] <= h*2/3 and ax[j] >= 0 and ay[j] >= 3/h:
                    ld.append([ax[j],ay[j]])

    elif ax[j] <= h*2/3 and ay[j] <= h*2/3 and ax[j] >= 3/h and ay[j] >= 3/h:
                    le.append([ax[j],ay[j]])

    elif ax[j] <= h and ay[j] <= h*2/3 and ax[j] >= h*2/3 and ay[j] >= 3/h:
                    lf.append([ax[j],ay[j]])  

    elif ax[j] <= h/3 and ay[j] <= h and ax[j] >= 0 and ay[j] >= h*2/3:
                    lg.append([ax[j],ay[j]])

    elif ax[j] <= h*2/3 and ay[j] <= h and ax[j] >= 3/h and ay[j] >= h*2/3:
                    lh.append([ax[j],ay[j]])

    elif ax[j] <= h and ay[j] <= h and ax[j] >= h*2/3 and ay[j] >= h*2/3:
                    li.append([ax[j],ay[j]])

    ll[2][2] = 1


    if len(la) >= int(na/d):
        ll[0][0] = 1

    if len(lb) >= int(na/d):
        ll[0][1] = 1

    if len(lc) >= int(na/d):
        ll[0][2] = 1

    if len(ld) >= int(na/d):
        ll[1][0] = 1

    if len(le) >= int(na/d):
        ll[1][1]= 1

    if len(lf) >= int(na/d):
        ll[1][2] = 1

    if len(lg) >= int(na/d):
        ll[2][0] = 1

    if len(lh) >= int(na/d):
        ll[2][1] = 1

    if len(li) >= int(na/d):
        ll[2][2] = 1


ax = []
ay = []

la = []
lb = []
lc = []
ld = []
le = []
lf = []
lg = []
lh = []
li = []

Brounshrimp_d(na)

while True:

    Lighface(ll)

    la.clear()
    lb.clear()
    lc.clear()
    ld.clear()
    le.clear()
    lf.clear()
    lg.clear()
    lh.clear()
    li.clear()

    Brounshrimp(na)
    
    c.pack()
    c.update()

    print('len(la) = ', len(la), 'len(lb) = ', len(lb), 'len(lc) = ', len(lc), 'len(ld) = ', len(ld), 'len(le) = ', len(le), 'len(lf) = ', len(lf), 'len(lg) = ', len(lg), 'len(lh) = ', len(lh), 'len(li) = ', len(li))
    print('la = ' , la, 'lb = ', lb, 'lc = ', lc, 'ld = ', ld, 'le = ', le, 'lf = ', lf, 'lg = ', lg, 'lh = ', lh,'li = ', li)
    print(ll)

root.mainloop()
