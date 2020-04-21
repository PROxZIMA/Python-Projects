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
def encryption(mes):   # Function to encrypt Alphabetical String
    cipher = ''

    for text in mes:

        #Convert letters to morse code and combining them
        cipher += Morse_Code_Dict[text] + ' '

    return cipher

# Function to decrypt the Morse Code according to the Morse Code Chart
def decryption(mes): #Function to decrpt Morse Code

    decipher = ''

    for text in mes:
        #Converting morse code to letters
        decipher += Morse_Code_Dict_Inverted[text]

    return decipher

try:
    opt = input('1) Alphabet to Mores (1)\n2) Morse to Alphabet (2)\nSelect the conversion you want : ')
    while 1:
        if opt == '1':
            message = input('Enter the secret message : ')
            print(encryption(message.upper()))

        elif opt == '2':
            message = input('Enter the morse code : ')
            print(decryption(message.split(' ')))

        else:
            print('Enter correct conversion keyword')

        opt_2 = input('Enter next conversion (enter 0 to exit) : ')
        if opt_2 == '0':
            break
        opt = opt_2

except ValueError:
    print('Enter correct code language')