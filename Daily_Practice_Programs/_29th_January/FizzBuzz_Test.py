num=int(input('Enter the numbers limit to be printed'))

for i in range(1,num+1):
    if i%3!=0 and i%5!=0:
        print(i)
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    else:
        print("Buzz")