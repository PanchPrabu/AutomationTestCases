# program to find the item found at the index in the list

List=[24,56,67,90,102,23,45,69,89]
num=int(input("Enter the number to find the index of the number from the list:"))

for item in range(len(List)):
    if List[item]==num:
        print(f"The number {num} found  in the list at the index:",item+1)
        break
else:
    print(f"The {num} is NOT found in the list")