# program to print a set containing all the colors from the color list 1 which ar not
# present in color list 2

# option 1
# color_list1=input('enter the color list1 as comma separated')
# color_list2=input('enter the color list2 as comma separated')
# c1=set(color_list1.split(','))
# c2=set(color_list2.split(','))
# c3=c1.difference(c2)
# print("The difference between the two sets of colors are ",c3)

# option 2
color_list1=input('enter the color list1 as comma separated')
color_list2=input('enter the color list2 as comma separated')
c1=set(color_list1.split(','))
c2=set(color_list2.split(','))
print("The difference between the two sets of colors are ",c1.difference(c2))