# Morse Code Translator

# Dictionary representing the Morse Code Chart
Morse_Code_Dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.',
                    '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ':'', '!':'-.-.--',
                    '"': '.-..-.', '$':'...-..-', '&':'.-...', '\'':'.----.', '+':'.-.-.',
                    ':':'---...', ';':'-.-.-.', '=':'-...-', '@':'.--.-.', '_':'..--.-'}

#Inverted Morse Code Dictionery
Morse_Code_Dict_Inverted = dict(map(reversed, Morse_Code_Dict.items()))


# Function to encrypt the input message according to the Morse Code Chart
def encryption(message):   # Function to encrypt Alphabetical String
    cipher = ''

    for text in message:

        #Convert letters to morse code and combining them
        cipher = cipher + Morse_Code_Dict[text] + ' '

    return cipher

# Function to decrypt the Morse Code according to the Morse Code Chart
def decryption(message): #Function to decrpt Morse Code

    message += ' ' #Reads last Morse Code
    decipher = ''
    morse = ''

    for text in message:

        if (text != ' '): #Checks no spaces

            morse += text #Makes morse letter

        else: #For spaces

            #Converting morse code to letters
            decipher += Morse_Code_Dict_Inverted[morse]
            morse = '' #Resets variable

    return decipher

try:
    opt = input('1) Alphabet to Mores (1)\n2) Morse to Alphabet (2)\nSelect the conversion you want : ')
    while 1:
        if opt == '1':
            message = input('Enter the secret message : ')
            result = encryption(message.upper())
            print (result)

        elif opt == '2':
            message = input('Enter the morse code : ')
            result = decryption(message)
            print (result)

        else:
            print('Enter correct conversion keyword')

        opt_2 = input('Enter next conversion (enter 0 to exit) : ')
        if opt_2 == '0':
            break
        opt = opt_2

except ValueError:
    print('Enter correct code language')