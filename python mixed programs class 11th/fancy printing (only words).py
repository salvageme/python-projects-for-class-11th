a=input("enter a word or a sentence: ")
x=''
d=''
for i in a:
    b=97
    print(x)
    if i==' ':
        x=x+' '
        continue
    while True:
        c=chr(b)
        e=d+c
        print(e)
        b=b+1
        if c==i:
            x=x+c
            break
    d=x
