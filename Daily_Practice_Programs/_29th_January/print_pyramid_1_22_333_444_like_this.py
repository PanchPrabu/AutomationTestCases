#print pyramid based on the input received from the user:
# for example :
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
num=int(input('Get the number from the user to print the pyramid:'))

for i in range(1,num+1):
    for j in range(0,i):
        print(i,end=' ')

    print('\n')

print('The pyramid has been printed successfully based on the user input')