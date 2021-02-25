# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addr1 = []
ip_addr2 = []
b=0
octet_status = True
'------------------Ввод сообщения------------------------------'
ip_addr = input('ввод IP-адреса в формате 10.0.1.1 : ')
'------проверка длинны сообщения ------'
if 7 <= len(ip_addr) <= 15:
    check_len_input=True
else:check_len_input=False
'-------Проверка цифр и точек----------------------'
for point in list(ip_addr):
    if point.isdigit() == True:
        ip_addr2.append(point)
    elif point == '.': 
        b=b+1
        ip_addr2.append(point)
    else:octet_status = False
'-----Проверка на точку в конце в начале и количество точек не равное 4м-----'
if ip_addr2[0] == '.' or ip_addr2[-1] == '.' or b != 3 : 
    octet_status = False
'-----------проверка типа порта----------------------------------'    
if octet_status == True and check_len_input == True:
    ip_addr = ip_addr.split('.')
    for line in ip_addr:
        ip_addr1.append(int(line)) 
    if 1 <= ip_addr1[0] <= 223:
        print('unicast')
    elif 224 <= ip_addr1[0] <= 239:
        print('multicast')
    elif ip_addr1[0] == ip_addr1[1] == ip_addr1[2] == ip_addr1[3] == 255:
        print('local broadcast')
    elif ip_addr1[0] == ip_addr1[1] == ip_addr1[2] == ip_addr1[3] == 0:
        print('unassigned')
    elif ip_addr1[0] >255 or  ip_addr1[1] >255 or ip_addr1[2] >255 or  ip_addr1[3] > 255:
        print('Неправильный IP-адрес') 
    else:print('unused')
else:
    print('Неправильный IP-адрес')



