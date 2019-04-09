n1=map(int,input().split())
a=list(map(int,input().split()))
#print(a[0])
for i in a:
    print(i)
    if i%2==0 and a.index(i)%2!=0:
        print(i,end="")
    elif i%2!=0 and a.index(i)%2==0:
        print(i,end="")
