n=int(input())
l=list(map(int,input().split()))
s=set()
for i in l:
    if l.count(i)>1:
       s.add(i) 
    else:
        print("unique")
for i in s:
    print(str(i)+" ",end="")