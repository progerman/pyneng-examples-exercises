# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
input_ip_add=input('Введите IP-сеть в формате X.X.X.X/M :')
input_ip_add=input_ip_add.split('/')
ip_add=input_ip_add[0].split('.')

print('Network:')

print(
f'{(ip_add[0]):<10}'
f'{(ip_add[1]):<10}'
f'{(ip_add[2]):<10}'
f'{(ip_add[3]):<10}')

print(
f'{int(ip_add[0]):08b}  '
f'{int(ip_add[1]):08b}  '
f'{int(ip_add[2]):08b}  '
f'{int(ip_add[3]):08b}  ')

print('Mask:')
net_mask=int(input_ip_add[1])



print('/', net_mask, sep='')
bit_mask='1'*net_mask+'0'*(32-net_mask)

bit_octet_mask_1=bit_mask[0:8]
bit_octet_mask_2=bit_mask[8:16]
bit_octet_mask_3=bit_mask[16:24]
bit_octet_mask_4=bit_mask[24:32]

print(
f'{int((bit_octet_mask_1),2):<10}'
f'{int((bit_octet_mask_2),2):<10}'
f'{int((bit_octet_mask_3),2):<10}'
f'{int((bit_octet_mask_4),2):<10}')
    
print(
f'{(bit_octet_mask_1):<10}'
f'{(bit_octet_mask_2):<10}'
f'{(bit_octet_mask_3):<10}'
f'{(bit_octet_mask_4):<10}')









