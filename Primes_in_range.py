import math 
def prime(a):
    for i in range(2,round(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if prime(i)==1 and i!=1:
        c+=1
print(c)