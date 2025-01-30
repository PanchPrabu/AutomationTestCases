# program to find the number of occurrences of a number

Str=input('Enter the numbers as space separated to form the list:')
#print('List before mapping',Str.split(' '))

List=list(map(int,Str.split(' ')))
#print('List after mapping',List)
number=int(input('Enter the number to be searched for their occurrences from the given list'))
count=List.count(number)
print(f"The number of occurrences of {number} from the list is {count} times")
