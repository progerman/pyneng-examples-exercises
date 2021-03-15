d=dict(a='1',b='2',c='3') # первый словарь


print(d)    

stroka = 'a3a2c'
print('stroka=',stroka)


for m in stroka:                #поиск элементов из stroka в ключах d
    if m in d.keys():                   #вывод значений этих лючей
        print('буква ', m, 'из строки "stroka" является ключом значения ', d[m]) 

s=[]
for i in d.keys():      #второй
    s.append((d[i],i))  #словарь
b=dict(s)               #является обратным для первого
                        #значения являются ключами, а ключи значениями

stroka_=stroka


for i in stroka_:               #поиск элементов из stroka в значениях d 
    if i in b.keys():               #вывод ключей этих значений
        print('цифра ', i, 'из строки "stroka" является значением ключа', b[i])
