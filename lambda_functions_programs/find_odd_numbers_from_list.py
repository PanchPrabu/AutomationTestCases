# program to print or list out only the odd numbers from the list

num_list=[1,2,5,7,12,19,25,23,67,88,98,99,101,103]
odd_list=list(filter(lambda x:(x%2!=0),num_list))
print(odd_list)


