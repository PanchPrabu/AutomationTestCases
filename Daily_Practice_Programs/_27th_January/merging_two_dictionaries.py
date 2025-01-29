# program to merge two dictionaries using copy method
# option 1
dict1={'A':1,'B': 2}
dict2={'C':3,'D':4}
dict1.update(dict2)
print(dict1)

# option2
dict1={'A':1,'B': 2}
dict2={'C':3,'D':4}
d=dict1.copy()
d.update(dict2)
print(d)