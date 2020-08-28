s = input('Enter a Palindrome string: ').casefold()
print('String is Palindrome') if s == s[::-1] else print('String isn\'t Palindrome')