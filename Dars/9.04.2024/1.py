table=8
for i in range(1,11):
   print(table, 'x', i, '= ?' )
   pup=input()
   res=table*i
   if pup=='bilmayman':
      break
   if pup=='keyingisi':
      print('Keyingi savol')
      continue
   if int(pup)==res:
        print('Barakalla!')
   else: print('Noto\'gri, javob:', res)
print('Tugadi')