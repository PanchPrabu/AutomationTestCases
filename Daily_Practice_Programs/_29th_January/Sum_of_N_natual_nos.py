
# program to find the sum of n natural nos

num=int(input('Enter the number to find the sum of n natural nos:'))

sum=0
for i in range(num+1):
    sum =sum+int(i)

print(f"The sum of {num} natural nos is:",sum)