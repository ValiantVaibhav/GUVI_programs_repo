class ValueInvalid(Exception):
    pass
try:
    n=int(input())
    if n<0:
        raise ValueInvalid
    else:
        if n%2==0:
            print("Even")
        else:
            print("Odd")

except ValueInvalid:
    print("Invalid")
    
except ValueError:
    print("Invalid")
    