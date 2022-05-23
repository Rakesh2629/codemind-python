n=int(input())
l=0
k=list(map(int,input().split()))
for i in range(0,len(k)):
    if k[i]%2!=0:
        l+=1
if l<=2:
    print('YES')
else:
    print('NO')
    