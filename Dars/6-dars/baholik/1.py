#1
print('1-masala')
a=float(input('a='))
b=float(input('b='))
if a>b:
    
    b=0
    print(b)
else:
   print(b)

#2   
print('2-masala')
a=float(input('a='))
b=float(input('b='))
if a%b==0:
    print('qoldiqsiz bo\'linadi')
else: print('qoldiqli bo\'linadi')

#3   
print('3-masala')
a=float(input('a='))
b=float(input('b='))
if a%b==0:   
    print(a+b)
else: print(a*b)

#4   
print('4-masala')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if ((a*a)-(b*b))==(c*c):   
    print(a*b*c)
else: print(a+b+c)

#5   
print('5-masala')
a=int(input('a='))
if a>0:   
    a=a+1
    print(a)
else: print(a)

#6
print('6-masala')
a=int(input('a='))
if a>0:   
    a=a*10
    print(a)
else: print(a)

#7  
print('7-masala')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
# x=float(input('x='))
d=b*b-4*c*a
x1=(-b-(d**1.2))/(2*a)
x2=(-b+(d**1.2))/(2*a)

if d>0:
    print('x1=',x1)
    print('x2=',x2)
elif d==0:
    print('x1=',x1)
else: print('yechim yo`q')


    