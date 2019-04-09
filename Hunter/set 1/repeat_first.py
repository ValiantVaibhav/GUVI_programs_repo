#import sys
n=int(input())
l=list(map(int,input().split()))
l1=[max(l)+1]*(max(l))
#print(l1)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            l1[l[i]]=j
            
#print(l1)
print(l1.index(min(l1)))