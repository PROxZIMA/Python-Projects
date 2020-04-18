from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry('300x300')
win.config(background='#0c0c0d')
win.title('Tic-Tac-Toe')

count=0

def insert(b):
    global count
    if b['text'] == '' and count%2==0:
        count+=1
        b.config(text='X')
    elif b['text'] == '' and count%2==1:
        count+=1
        b.config(text='O')
    else:
        messagebox.showwarning('Oops', 'Button already pressed')
    
    if (b1['text']==b2['text']==b3['text']=='X') or (b4['text']==b5['text']==b6['text']=='X') or (b7['text']==b8['text']==b9['text']=='X') or (b1['text']==b4['text']==b7['text']=='X') or (b2['text']==b5['text']==b8['text']=='X') or (b3['text']==b6['text']==b9['text']=='X') or (b1['text']==b5['text']==b9['text']=='X') or (b3['text']==b5['text']==b7['text']=='X'):
        messagebox.showinfo('Winner', 'Player 1 WON!!!!!!!!!!!!!')

    elif (b1['text']==b2['text']==b3['text']=='O') or (b4['text']==b5['text']==b6['text']=='O') or (b7['text']==b8['text']==b9['text']=='O') or (b1['text']==b4['text']==b7['text']=='O') or (b2['text']==b5['text']==b8['text']=='O') or (b3['text']==b6['text']==b9['text']=='O') or (b1['text']==b5['text']==b9['text']=='O') or (b3['text']==b5['text']==b7['text']=='O'):
        messagebox.showinfo('Winner', 'Player 2 WON!!!!!!!!!!!!!')

    elif draw():
        messagebox.showinfo('Draw', 'Match is DRAW!!!!!!!!!!!!!!')


def draw():
    for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
        if i['text'] == '':
            return False
    return True


b1 = Button(win,command=lambda:insert(b1), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b1.place(x=0, y=0, width=100, height=100)

b2 = Button(win,command=lambda:insert(b2), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b2.place(x=100, y=0, width=100, height=100)

b3 = Button(win,command=lambda:insert(b3), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b3.place(x=200, y=0, width=100, height=100)

b4 = Button(win,command=lambda:insert(b4), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b4.place(x=0, y=100, width=100, height=100)

b5 = Button(win,command=lambda:insert(b5), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b5.place(x=100, y=100, width=100, height=100)

b6 = Button(win,command=lambda:insert(b6), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b6.place(x=200, y=100, width=100, height=100)

b7 = Button(win,command=lambda:insert(b7), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b7.place(x=0, y=200, width=100, height=100)

b8 = Button(win,command=lambda:insert(b8), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b8.place(x=100, y=200, width=100, height=100)

b9 = Button(win,command=lambda:insert(b9), bd=5, font = ('arial', 15, 'bold'), bg='#e4e4e4', activebackground='#ff0000')
b9.place(x=200, y=200, width=100, height=100)


win.mainloop()