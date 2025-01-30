# print the pyramid in the below mentioned format based on the user input
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

num=int(input("Get the input from the user to print the pyramid:"))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print('\n')

print('The pyramid has been printed successfully based on the user input')