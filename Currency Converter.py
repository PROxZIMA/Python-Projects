from tkinter import *

win = Tk()
win.geometry('600x450')
win.config(background='#0c0c0d')

def calculate():
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    e2.insert(END, round(e1_value.get()*0.0149,4))
    e3.insert(END, round(e1_value.get()*0.0105,4))
    e4.insert(END, round(e1_value.get()*0.0135,4))

l1 = Label(win, text = 'Enter Currency in Rupees', font = ('arial', 13))
l1.place(x=50, y=50, width=200, height=50)

e1_value = IntVar()
e1 = Entry(win, font = ('arial', 20), textvariable=e1_value)
e1.place(x=350, y=50, width=200, height=50)

b1 = Button(win,command=calculate, text = 'Calculate', font = ('arial', 15), background='#00ff00', activebackground='#ff0000')
b1.place(x=200, y=150, width=200, height=50)

e2 = Entry(win, font = ('arial', 20))
e2.place(x=37.5, y=250, width=150, height=50)

l2 = Label(win, text = 'Currency in Dollar', font = ('arial', 13))
l2.place(x=37.5, y=350, width=150, height=50)

e3 = Entry(win, font = ('arial', 20))
e3.place(x=225, y=250, width=150, height=50)

l3 = Label(win, text = 'Currency in Pound', font = ('arial', 13))
l3.place(x=225, y=350, width=150, height=50)

e4 = Entry(win, font = ('arial', 20))
e4.place(x=412.5, y=250, width=150, height=50)

l4 = Label(win, text = 'Currency in Euro', font = ('arial', 13))
l4.place(x=412.5, y=350, width=150, height=50)

win.mainloop()