# Modify your solution to Exercise 19.2 by adding an Entry widget and a 
# second button. When the user presses the second button, it should read a
# color name from the Entry and use it to change the fill color of the circle.
# Use config to modify the existing circle; don’t create a new one.
# Your program should handle the case where the user tries to change the color 
# of a circle that hasn't been created, and the case where the color name is 
# invalid. You can see my solution at thinkpython.com/code/circle_demo.py.

# Current Status: Incomplete
from tkinter import  *

master = Tk()
master.title('GUI')
circle=False
entry=True

canvas=Canvas(master,width=300,height=300)
canvas.pack()
canvas.config(bg='red')
def draw_circle():
    global circle
    circle= canvas.create_oval(50,50,200,200,fill='blue')


def change_color():
    if circle==False:
        Label(text='Please make circle').pack()
        return
    try:
        color=entry.get()
        circle.config(fill=str(color))
    except:
        Label(text='Please enter valid color')
        return


button=Button(master,text='Create Circle',command=draw_circle,bg='green')
entry=Entry(text='Enter a color').pack()
button1=Button(master,text='Change Color', command=change_color).pack()


button.pack()
mainloop()
