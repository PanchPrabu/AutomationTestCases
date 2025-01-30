# program to find the vowels count in a string
Str=input("Enter the string to find the vowels count:")
vowels_count=0
for i in Str:
    if i in 'aeiouAEIOU':
        vowels_count=vowels_count+1

if vowels_count>=1:
    print(f"The total number of vowels from the {Str} is :", vowels_count)
else:
    print("There is no vowels present in the string")



