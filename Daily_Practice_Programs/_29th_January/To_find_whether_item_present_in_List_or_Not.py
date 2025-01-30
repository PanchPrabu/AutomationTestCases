# program to find whether the item is present in the list or not

List=[10,12,13,34,27,98]
#num=int(input('Enter the number to be searched in the given list:'))

for i in List:
    num=int(input('Enter the number to be searched in the given list:'))
    if num in List:
        print(f"The entered number {num} is present in the list")
        break
    else:
        print(f"The entered number {num} is NOT present in the list")
        continue


