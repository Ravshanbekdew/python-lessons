table  =8 
for i in range(1,11):
    print(table , 'x',i , '= ? ')
    pup = input()
    if pup == 'bilmayman':
        break

    res = table*i
    if int(pup)==res:
        print('Barakallo')
    else:
        print('Noto`g`ri javob')
print('Uxladiz  Jomolxon :)')