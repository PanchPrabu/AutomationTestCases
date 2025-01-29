# Remove duplicates from a list
# option 1

list = [1,2,3,4,1,3,5,7,2,2,3]
# change_to_set=set(list)
# # option 1
# print(change_to_set)
# newlist=[]
# for i in change_to_set:
#     newlist.append(i)
# print(newlist)


#option 2
list_without_dup=[]
for i in list:
    if i not in list_without_dup:
        list_without_dup.append(i)
print("List without duplicate is:",list_without_dup)



