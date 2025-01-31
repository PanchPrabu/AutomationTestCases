#program to concatenate all the element in the list to string

# Option 1
#
# lis=input('Enter the values of the list as comma separated:')
# my_list=lis.split(' ')
# print("Original list is:",my_list)
# Str=''
# for i in my_list:
#     #print(i,end='')
#     Str=Str+i
# print(Str)
# print(type(Str))

# option 2
lis=input('Enter the values of the list as comma separated:')
my_list=lis.split(' ')
print("Original list is:",my_list)

for i in my_list:
    print(i,end='')


