# program to get a single string from 2 given strings, separated by a space and
# swap the first two characters of each string


str1=input('enter the first string')
str2=input('enter the second string')
new_str1=str2[:2]+str1[2:]
new_str2=str1[:2]+str2[2:]
print("The new string after swapping the first 2 characters of each string is:",new_str1+" "+new_str2)

print("Received the program out put successfully")

