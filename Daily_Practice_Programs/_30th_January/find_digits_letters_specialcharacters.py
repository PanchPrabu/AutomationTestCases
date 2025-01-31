# find the digits, letters and special characters from the given string
str1=input("Enter the string")

digit_count=0
letters_count=0
special_chr_count=0
for i in str1:
    if i.isdigit():
        digit_count+=1
    elif i.isalpha():
        letters_count+=1
    else:
        special_chr_count+=1

print(f"The number of digits in the provided {str1} is {digit_count} ")
print(f"The number of letters in the provided {str1} is {letters_count} ")
print(f"The number of special characters in the provided {str1} is {special_chr_count} ")