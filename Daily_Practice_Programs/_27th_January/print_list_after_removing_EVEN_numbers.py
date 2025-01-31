# program to remove the even numbers from the list
lis=input('Enter the numbers as space separated:')
my_list=list(map(int,lis.split(' ')))
new_list=[]
for i in my_list:
    if i%2 !=0:
        new_list.append(i)
    else:
        continue
print("The new list after removing the even numbers are :", new_list)


