#program to interchange the first and last character of a string
String=input('Enter a string:')
print('The string before interchanging:',String)

print('The string after interchanging:',String[-1]+String[1:-1]+String[0])