# program to accept a word from user and reverse it

word=input("Enter the word to be reversed:")
print("The word before reversing",word)
for i in word[::-1]:
    print(i,end='')