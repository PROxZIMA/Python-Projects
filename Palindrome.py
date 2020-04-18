s = input('Enter a Palindrome string: ').casefold()
if s == s[::-1]:
    print('String is Palindrome')
else:
    print('String isn\'t Palindrome')