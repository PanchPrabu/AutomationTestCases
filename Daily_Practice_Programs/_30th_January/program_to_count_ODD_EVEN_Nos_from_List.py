# program to count odd and even numbers from the list

lis=input("Enter the values for the list as space separated")
my_list=list(map(int,lis.split(' ')))
odd_count=0
even_count=0
for i in my_list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"The odd numbers count in the list is: {odd_count}")
print(f"The odd numbers count in the list is: {even_count}")