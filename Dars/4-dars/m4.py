# hajmi 1 ekranni egallovchi archa chizish dasturi. Boshida 5 yulduz bo'lsin. Agar * dan foydalanilsa o yordamida o'yinchoq qo'shish.

def yulduz(son):
   print(" " * (son*3 - 2)+'*')
   print(" " * (son*3 - 4)+'*****')
   print(" " * (son*3 - 4)+' * *')
   
#    print(" " * (son*3 - 2)+'*')
   
def archa(soni):
    for i in range(1, soni + 1):
        spaces = "   " * (soni - i)
        yulduz = "*o*" * (2*i - 1)
        print(spaces + yulduz)

yulduz(10)
archa(10)

