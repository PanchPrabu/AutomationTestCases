# program to get a string made of teh first 2 and last 2 characters from a given string.
# If the string length is less than 2, return instead the empty string.

str1=input('Enter the string')
if len(str1)<2:
    print(None)
else:
    new_string=str1[:2]+str1[-2:]
    print('The new string from the given string is:', new_string)



