# program to concatenate  dictionaries to create a new one

dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}

for d in (dict1,dict2,dict3):
    dict4.update(d)

print("After concatenating the dictionaries . the newly formed dictionary is :",dict4)