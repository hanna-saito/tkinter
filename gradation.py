from tkinter import*
from numpy.random import*
import time

root=Tk()
root.title('Gradation') #ウィンドウタイトル
w = 600
h = w

c=Canvas(root, width=w, height=h,) #canvas作成

def Gradation():
	g1 = 99

	while True:
		c.delete('b')
		c.create_rectangle(100,100,500,500,fill = 'white', outline = 'white', tags = 'b')
		c.pack()
		c.update()
		time.sleep(1)

		
		for i in range(99): #白→黒
			c.delete('b')
			time.sleep(0.03)

			gs = 'grey' + str(g1) 

			c.create_rectangle(100,100,500,500,fill = gs, outline = gs, tags = 'b')
			print(gs)
			g1 = g1-1
			c.pack()
			c.update()

		c.delete('b')
		c.create_rectangle(100,100,500,500,fill = 'black', outline = 'black', tags = 'b')
		c.pack()
		c.update()
		time.sleep(1)

		for i in range(99): #黒→白
			c.delete('b')
			time.sleep(0.03)

			gs = "grey" + str(g1) 

			c.create_rectangle(100,100,500,500,fill = gs, outline = gs, tags = 'b')
			print(gs)
			g1 = g1+1
			c.pack()
			c.update()


			

Gradation()
root.mainloop()


