#program to find the sum of all numbers from a list

numbers=input("Enter the numbers for a list as comma separated")
num_list=numbers.split(',')
#print(num_list)
sum=0
for i in num_list:
    sum=sum+int(i)

print("The sum of all numbers from the generated list is :",sum)

