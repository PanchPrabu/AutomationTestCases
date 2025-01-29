# program to print the colors information (first color and last color) from the list

colors=input('enter the colors as comma separated:')
colors_list=colors.split(',')
print("The first color in the list is:",colors_list[0], '\n'
      "The last color in the list is:",colors_list[-1])