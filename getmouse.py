import tkinter as Tk
root=Tk.Tk()

f=Tk.Frame(root,
           width=200,
           height=100,
)
def print_motion(event):
    print("Motion %d,%d" % (event.x, event.y))
def print_button(event):
    print("  Button %d,%d" % (event.x, event.y))

f.bind("<Motion>", print_motion)
f.bind("<Button>", print_button)
f.pack()

root.mainloop()
