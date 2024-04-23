print('*****************')
def min4(a, b, c, d):
   
    return min(a,b,c,d)

# Test qilish
son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))
son3 = float(input("3-sonni kiriting: "))
son4 = float(input("4-sonni kiriting: "))

eng_kichik = min4(son1, son2, son3, son4)
print("Eng kichik son:", eng_kichik)


print('*****************')
def m2(a,k):
    print(a**k)
a=float(input("a Sonni kiriting: "))
k=int(input(("k Sonni kiriting: ")))
m2(a,k)
print('*****************')

def hisoblash(satr):
    raqam_soni = 0
    
    for belgi in satr:
        if belgi.isdigit():
            raqam_soni += 1
    
    return raqam_soni

satr = input("Satr kiriting: ")
raqam = hisoblash(satr)
print("Satrdagi raqam soni:", raqam)

print('*****************')
def akslantirish(son):
    akslantirilgan_son = int(str(son)[::-1])
    return akslantirilgan_son

son = int(input("Sonni kiriting: "))
natija = akslantirish(son)
print("Akslantirilgan son:", natija)


print('*****************')
def yigindi(sonlar):
    raqamlar = sonlar.split()  
    yig = sum(map(int, raqamlar)) 
    return yig

ketma_ketlik = input("0 bilan ajratilgan sonlar ketma-ketligini kiriting: ")
natija = yigindi(ketma_ketlik)
print("Raqamlar yig'indisi:", natija)

print('*****************')
def birlikni_grammga_aylantirish(tonna, kilogramm, gramm):
    umumiy_gramm = tonna * 1000000 + kilogramm * 1000 + gramm
    return umumiy_gramm

tonna = int(input("Tonni kiriting: "))
kilogramm = int(input("Kilogramni kiriting: "))
gramm = int(input("Grammni kiriting: "))

natija = birlikni_grammga_aylantirish(tonna, kilogramm, gramm)
print("Umumiy gramm:", natija)
