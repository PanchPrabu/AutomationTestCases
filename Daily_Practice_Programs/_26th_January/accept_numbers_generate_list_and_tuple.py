# accept numbers from user as comma separated and generata list and tuple

numbers=input('enter the numbers as comma separated')
gen_list=numbers.split(',')
gen_tuple=tuple(gen_list)
print("The newly generated list is:",gen_list)
print("The newly generated tuple is :",gen_tuple)

