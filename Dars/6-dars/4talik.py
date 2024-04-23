n=1
print(n,'-masala')
a=int(input('a=(2 xonalik)'))
if (a//10)%2==1:
 
    print('toq')
else: print('Juft')
if a%2==1:
   
    print('toq')
else: print('Juft')

n=2
print(n,'-masala')
a=int(input('a=(3 xonalik)'))
a3=a%10
a=a//10
a2=a%10
a=a//10
a1=a
if ((a1)==(a2))and(a1==a3):
    print('3ta bir xil')
    print(a1,a2,a3)
elif (a1==a2)or(a1==a3)or(a2==a3):
    print('2ta bir xil')
    print(a1,a2,a3)
else: print('O\'xshash emas')

n=3
print(n,'-masala')
a=int(input('a='))
b=int(input('b='))

if a%2==1:
    print('a:toq')
else: print('a:juft')

if b%2==1:
    print('b:toq')
else: print('b:juft')


n=4
print(n,'-masala')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if a%2==0:
   print('a:juft')
elif b%2==0:
   print('b:juft')
elif c%2==0:
   print('c:juft')

else:   print('Juft son yo`q')
