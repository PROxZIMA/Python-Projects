# Morse Code Translator

import tkinter as tk
from tkinter import messagebox

#Window initialiser
win = tk.Tk()
win.geometry('600x750')
win.config(background='#202124')
win.title('Morse-Code Translator')

#Menubar initialiser
menubar = tk.Menu(win)


# Dictionary representing the Morse Code Chart
Morse_Code_Dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
                    '-':'-....-', '(':'-.--.', ')':'-.--.-', '_':'..--.-', '!':'-.-.--',
                    '"': '.-..-.', '$':'...-..-', '&':'.-...', '\'':'.----.', '+':'.-.-.',
                    ':':'---...', ';':'-.-.-.', '=':'-...-', '@':'.--.-.', ' ':''}

#abcdefghijklmnopqrstuvwxyz 1234567890 ,.?/-()_!"'$@&+;:=

#Inverted Morse Code Dictionery
Morse_Code_Dict_Inverted = dict(map(reversed, Morse_Code_Dict.items()))

def helper():
    messagebox.showinfo('Basics', '1. This is a Morse Coder Translator created using Python 3.8\n2. Not all characters from Alphabetical language can be converted to Morse\n3. Chatacters like ~, `, #, %, *, <, >, [] and {} can\'t be converted\n4. If you want to try, you can!!!\n5. Also only meaningful combination of . and - can be converted from Morse to Alaphabet')

def author():
    messagebox.showinfo('Authors', 'Pratik Pingale')

#Clear Entry boxes
def clear():
    try:
        encode_block.e1.delete(0, tk.END)
        encode_block.e2.delete(0, tk.END)
        decode_block.e3.delete(0, tk.END)
        decode_block.e4.delete(0, tk.END)
    except AttributeError:
        pass

# Function to encrypt the input message according to the Morse Code Chart
def encryption():   # Function to encrypt Alphabetical String
    try:
        encode_block.e2.delete(0, tk.END)
        message_upper = encode_block.message.get().upper() #Convert lower case to upper case

        if message_upper == '':
            messagebox.showinfo('Blank', 'This field can\'t be empty')

        cipher = ''

        for text in message_upper:
            #Convert letters to morse code and combining them
            cipher += Morse_Code_Dict[text] + ' '

        encode_block.e2.insert(tk.END, cipher)

    except KeyError:
        messagebox.showerror('Error', 'Improper characters detected')

# Function to decrypt the Morse Code according to the Morse Code Chart
def decryption(): #Function to decrpt Morse Code
    try:
        decode_block.e4.delete(0, tk.END)

        morse_code_list = decode_block.morse_code.get().split(' ') #Reads entered morse code and convert it to list

        if morse_code_list == '':
            messagebox.showinfo('Blank', 'This field can\'t be empty')

        decipher = ''

        for text in morse_code_list:
            #converts morse code to letters and combine them
            decipher += Morse_Code_Dict_Inverted[text]

        decode_block.e4.insert(tk.END, decipher)

    except KeyError:
        messagebox.showerror('Error', 'Morse code is incorrect')


#Encode window
def encode_block():
    label_1.place_forget()
    selector_1.place_forget()
    selector_2.place_configure(x=150, y=650)

    #Alphabet to Morse
    Enter_Msg = tk.Label(win, text = 'Enter Message', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    Enter_Msg.place(x=200, y=50, width=200, height=50)

    encode_block.message = tk.StringVar()
    encode_block.e1 = tk.Entry(win, font = ('arial', 16), textvariable=encode_block.message, bd=10, justify='center')
    encode_block.e1.place(x=50, y=150, width=500, height=100)

    encode = tk.Button(win, command=encryption, text = 'Encode', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    encode.place(x=225, y=300, width=150, height=50)

    Morse_Code = tk.Label(win, text = 'Morse Code', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    Morse_Code.place(x=200, y=400, width=200, height=50)

    encode_block.e2 = tk.Entry(win, font = ('arial', 16), bd=10, justify='center')
    encode_block.e2.place(x=50, y=500, width=500, height=100)


#Decode window
def decode_block():
    label_1.place_forget()
    selector_2.place_forget()
    selector_1.place_configure(x=150, y=650)
    
    #Morse to Alphabet
    Enter_Morse = tk.Label(win, text = 'Enter Morse Code', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    Enter_Morse.place(x=200, y=50, width=200, height=50)

    decode_block.morse_code = tk.StringVar()
    decode_block.e3 = tk.Entry(win, font = ('arial', 16), textvariable=decode_block.morse_code, bd=10, justify='center')
    decode_block.e3.place(x=50, y=150, width=500, height=100)

    decode = tk.Button(win, command=decryption, text = 'Decode', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    decode.place(x=225, y=300, width=150, height=50)

    Msg = tk.Label(win, text = 'Message', font = ('arial', 18), bg='#2d2e31', fg='#fff')
    Msg.place(x=200, y=400, width=200, height=50)

    decode_block.e4 = tk.Entry(win, font = ('arial', 16), bd=10, justify='center')
    decode_block.e4.place(x=50, y=500, width=500, height=100)


#Starting window
label_1 = tk.Label(win, text = 'Select operation', font = ('arial', 18), bg='#2d2e31', fg='#fff')
label_1.place(x=200, y=125, width=200, height=50)

selector_1 = tk.Button(win, command=encode_block, text='1. Alphabet to Morse Code', font = ('arial', 18), bg='#2d2e31', fg='#fff')
selector_1.place(x=150, y=300, width=300, height=50)
selector_2 = tk.Button(win, command=decode_block, text='2. Morse Code to Alphabet', font = ('arial', 18), bg='#2d2e31', fg='#fff')
selector_2.place(x=150, y=475, width=300, height=50)

#File and Help menu creation
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear", command=clear)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Info", command=helper)
helpmenu.add_separator()
helpmenu.add_command(label="Author", command=author)
menubar.add_cascade(label="Help", menu=helpmenu)


#Run all above together
win.config(menu=menubar)
win.mainloop()
