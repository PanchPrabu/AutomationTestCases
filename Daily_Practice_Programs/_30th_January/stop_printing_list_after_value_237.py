#program to print the list in the same order as provided and
# stop printing the list after find the value 237

lis=input('Enter the values in the list as comma separated:')
original_list=lis.split(' ')
print('The original list is :',original_list)
my_num_list=list(map(int,lis.split(' ')))

print('The number list is:',my_num_list)
for i in my_num_list:
    if i==237:
        break
    elif i%2==0:
        print(i,end=' ')
    # else:
    #     continue
