n=int(input())
l=list(map(int,input().split()))
s=set()
for i in range(n):
    if i==l[i]:
       s.add(i)
q=[print(str(i)+" ",end="") for i in s]
