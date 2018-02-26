from tkinter import*
from numpy.random import*

root = Tk()
root.title('SOLsimulation')
w = 500
h = w
c = Canvas(root, width = w, height = h)

def Artemia(n):

    for i in range(n):
        r1 = int(rand()*w)
        r2 = int(rand()*w)
        
        c.create_oval(r1, r2, r1+3, r2+3)

if __name__ == '__main__':

    t = True
    ry = []  
    rx = []
    cs = int(h/3)

    for i in range(3):
        ry.append(i*cs)
        rx.append(i*cs)
    

    for i in rx:
        for j in ry:
            if t == True:
                c.create_rectangle(i,j,i+cs,j+cs, fill = 'white', outline = 'black')
                t = False
        
            elif t == False:
                c.create_rectangle(i,j,i+cs,j+cs, fill = 'white', outline = 'black')
                t = True

    Artemia(500)
            
    
c.pack()

root.mainloop()
