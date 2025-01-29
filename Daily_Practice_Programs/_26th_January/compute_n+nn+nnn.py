# program to compute the value of n+nn+nnn

n=input('enter the number')
n1=int('%s'% n)
#print(type(n1))
n2=int('%s%s'%(n,n))
n3=int('%s%s%s'%(n,n,n))
print(n1,"",n2,"",n3)
print("sum=",n1+n2+n3)