n1=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==0:
            l.append([a[i],a[j]])
for i in range(2):
    print(l[0][i],end=" ")