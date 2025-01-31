# remove the duplicates from the list

# option 1
# lis=input('Enter the values for the list as space separated')
# my_list=lis.split(' ')
# my_set=set(my_list)
# after_dup_removal=list(my_set)
# print("After removing the duplicates from the list are:",after_dup_removal)

# option 2
lis=input('Enter the values for the list as space separated')
my_list=lis.split(' ')
dup_removed_list=[]
for i in my_list:
    if i not in dup_removed_list:
        dup_removed_list.append(i)
print('After removing the duplicates from teh lise:',dup_removed_list)