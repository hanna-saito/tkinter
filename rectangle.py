from tkinter import*

root = Tk()
c = Canvas(root, width = 150, height = 150)
r1 = c.create_rectangle(5,5,15,15, fill = 'green') 
c.pack()

root.mainloop()
