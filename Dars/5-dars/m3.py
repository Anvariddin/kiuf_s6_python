a = 20
c = False
print(a > 17 or c)

a = 20
c = False
print(not a > 17 or not c)


a = True
b = True
c = False
print(not(a and c) and (a or b) or c)

a = 66
b = 22
c = 7
print(not((a > b) or (b < c)))