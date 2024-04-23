a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

if a<(b+c) and b<(a+c) and c<(a+b):
    p=float(a+b+c)/2.0
    s=float(p*(p-a)*(p-b)*(p-c))**1.0/2
    print("Yuza ",s)
else:
    print("Bu sonlardan uchburchak yasab bo'lmaydi!")