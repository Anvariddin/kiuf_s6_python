n = input("Son kiriting: k(0<k<9999)")
n = int(n)
d1 = n % 10
d2 = n % 100 // 10
d3 = n % 1000 // 100
d4 = n // 1000
print("Natija:", d1 + d2 + d3 + d4)

print("Natija:", d1 * d2 * d3 * d4)