# program to remove the nth index from the string

String=input('enter the string: ')
n=int(input('enter the index number to be removed from the string'))
first_part=String[:n-1]
last_part=String[n:]
print("The Original String is:",String)
print(f'The new string after removing the {n}th index from the string {String} is:',first_part+last_part)