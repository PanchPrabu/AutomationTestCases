# program to find the factorial of a number
num=int(input('Enter the number to find the factorial:'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"The factorial of {num} is :",fact)
