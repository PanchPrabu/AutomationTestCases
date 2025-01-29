String=input('enter the string')
first_char=String[0]
String=String.replace(first_char,'$')
new_String=first_char+String[1:]
print("The new string is :",new_String)




