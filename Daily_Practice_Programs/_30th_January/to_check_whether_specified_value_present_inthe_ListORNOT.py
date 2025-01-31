# program to check whether specified value is present in the list or not
lis=input('enter the list as space separated:')
my_list=lis.split(' ')

val=input("Enter the element or specified value to be checked in the list:")

if val in my_list:
    print("Element/Specified value is found in the list")
else:
    print("Not found in the list")