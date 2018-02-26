from tkinter import*
from numpy.random import*
import time

root=Tk()
root.title('Mouse Motion')
w = 500
h = w

c=Canvas(root, width=w, height=h,)

def print_motion(event):
    print("Motion %d,%d" % (event.x, event.y))
    return (event.x, event.y)
    
def print_button(event):
    print("  Button %d,%d" % (event.x, event.y))
    return (event.x, event.y)

def Brounshrimp(na):

    a = True 

    ax = []
    ay = []

    for i in range(na):
        rx = int(rand()*w)
        ry = int(rand()*w)
        ax.append(rx)
        ay.append(ry)
        c.create_oval(rx, ry, rx+3, ry+3, tags = 'o')

    while a == True:
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
            c.pack()
        
        c.update()



c.bind("<Motion>", print_motion)
c.bind("<Button>", print_button)
c.pack()

    
Brounshrimp(1000)
root.mainloop()
