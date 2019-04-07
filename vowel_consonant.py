class InputError(Exception):
    pass
try:
    n=input()
    if n>='A' and n<='Z' or n>='a' and n<='z':
        l=['a','e','i','o','u']
        if n in l:
            print("Vowel")
        else:
            print("Consonant")

    else:
        
        raise InputError
except InputError:
    print("Invalid")