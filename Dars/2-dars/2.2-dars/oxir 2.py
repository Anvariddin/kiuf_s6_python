a=int(input("Uzunlikni kiriting(mm): "))
k=a//1000000
m=a%1000000//1000
d=a%1000//100
c=a%100//10
mm=a%10


print(k,"km",m,"m",d,"dm",c,"cm",mm,"mm")

