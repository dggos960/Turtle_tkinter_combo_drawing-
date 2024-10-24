import turtle as t
import tkinter as tk
win=t.Turtle()
robo=tk.Tk()
win.color("blue","green")
win.begin_fill()
def fun():
	win.fd(10)
btn=tk.Button(robo,text="click for move 10m",bg="black",fg='red',bd=7,command=fun)
btn.pack()


def fun1():
	win.lt(10)
btn1=tk.Button(robo,text="10° LEFT",bg="black",fg='red',bd=7,command=fun1)
btn1.pack()


def fun2():
	win.bk(10)
btn2=tk.Button(robo,text="10m BACKWARD",bg="black",fg='red',bd=7,command=fun2)
btn2.pack()

def fun3():
	win.circle(10)
btn3=tk.Button(robo,text=" 10m CIRCLE",bg="black",fg='red',bd=7,command=fun3)
btn3.pack()

def fun4():
	win.clear()
btn4=tk.Button(robo,text="CLEAR",bg="black",fg='red',bd=7,command=fun4)
btn4.pack()
win.end_fill()

robo.mainloop()
