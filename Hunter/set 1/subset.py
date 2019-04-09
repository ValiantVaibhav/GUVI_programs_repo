n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
flag=False
for i in b:
    if i in a:
        flag=True
    else:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")
