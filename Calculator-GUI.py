from tkinter import *

win = Tk()
win.geometry('500x600')
win.config(background='#1f1f1f')

exp = ''

def insert(num):
    global exp
    exp += str(num)
    inp.delete(0, END)
    inp.insert(END, exp)

def delete():
    pass

def evaluate():
    global exp
    total = eval(exp)
    display.delete(0, END)
    display.insert(END, total)
    exp = ''

def clear():
    global exp
    inp.delete(0, END)
    display.delete(0, END)
    exp = ''

def plus_minus():
    pass

inp = Entry(win, font = ('arial', 20), justify='right', bd=10, bg='#1f1f1f', fg='#ffffff')
inp.place(x=5, y=5, width=490, height=90)

display = Entry(win, font = ('arial', 20), justify='right', bd=10, bg='#1f1f1f', fg='#ffffff')
display.place(x=5, y=105, width=490, height=90)

#1st Row
dot = Button(win,command=lambda:insert('.'), text = '.', bd=5 , font = ('arial', 25), bg='#131313', fg='#ffffff')
dot.place(x=200, y=500, width=100, height=100)

zero = Button(win,command=lambda:insert(0), text = '0', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
zero.place(x=100, y=500, width=100, height=100)

equal = Button(win, command=evaluate, text = '=', bd=5 , font = ('arial', 25), bg='#2d2b2b', fg='#ffffff')
equal.place(x=400, y=500, width=100, height=100)

plus = Button(win,command=lambda:insert('+'), text = '+', bd=5 , font = ('arial', 25), bg='#131313', fg='#ffffff')
plus.place(x=300, y=500, width=100, height=100)

plus_minus = Button(win, command=plus_minus, text = '+/-', bd=5 , font = ('arial', 25), bg='#2d2b2b', fg='#ffffff')
plus_minus.place(x=0, y=500, width=100, height=100)


#2nd Row
one = Button(win,command=lambda:insert(1), text = '1', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
one.place(x=0, y=400, width=100, height=100)

two = Button(win,command=lambda:insert(2), text = '2', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
two.place(x=100, y=400, width=100, height=100)

three = Button(win,command=lambda:insert(3), text = '3', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
three.place(x=200, y=400, width=100, height=100)

minus = Button(win,command=lambda:insert('-'), text = '-', bd=5 , font = ('arial', 25), bg='#131313', fg='#ffffff')
minus.place(x=300, y=400, width=100, height=100)


#3rd Row
four = Button(win,command=lambda:insert(4), text = '4', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
four.place(x=0, y=300, width=100, height=100)

five = Button(win,command=lambda:insert(5), text = '5', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
five.place(x=100, y=300, width=100, height=100)

six = Button(win,command=lambda:insert(6), text = '6', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
six.place(x=200, y=300, width=100, height=100)

div = Button(win,command=lambda:insert('/'), text = '/', bd=5 , font = ('arial', 25), bg='#131313', fg='#ffffff')
div.place(x=300, y=300, width=100, height=100)

all_clear = Button(win, command=clear, text = 'CE', bd=5 , font = ('arial', 25), bg='#2d2b2b', fg='#ffffff')
all_clear.place(x=400, y=300, width=100, height=100)


#4th Row
seven = Button(win,command=lambda:insert(7), text = '7', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
seven.place(x=0, y=200, width=100, height=100)

eight = Button(win,command=lambda:insert(8), text = '8', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
eight.place(x=100, y=200, width=100, height=100)

nine = Button(win,command=lambda:insert(9), text = '9', bd=5 , font = ('arial', 25), bg='#060606', fg='#ffffff')
nine.place(x=200, y=200, width=100, height=100)

mult = Button(win,command=lambda:insert('*'), text = '*', bd=5 , font = ('arial', 25), bg='#131313', fg='#ffffff')
mult.place(x=300, y=200, width=100, height=100)

delete = Button(win, command=delete, text = 'Del', bd=5 , font = ('arial', 25), bg='#2d2b2b', fg='#ffffff')
delete.place(x=400, y=200, width=100, height=100)


win.mainloop()