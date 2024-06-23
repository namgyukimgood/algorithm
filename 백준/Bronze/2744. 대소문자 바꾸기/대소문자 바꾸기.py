inputString=input()
for i in inputString:
    if i.isupper(): 
        i= i.lower()
    else:
        i= i.upper()
    print(i,end='')