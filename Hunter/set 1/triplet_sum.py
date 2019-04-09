n1=map(int,input().split())
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]+a[j]==a[k]:
                print(a[i],a[j],a[k])
                break