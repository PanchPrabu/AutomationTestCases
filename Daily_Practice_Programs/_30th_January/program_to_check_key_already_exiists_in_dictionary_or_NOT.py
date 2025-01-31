# program to check key already exists in dictionary or NOT

d= {1:10,2:20,3:30,4:40,5:50,6:60}

key=int(input('Enter the value for the key to check exists or not'))

if key in d:
    print("The key exists")
else:
    print("The key not exists")