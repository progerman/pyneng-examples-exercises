# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

input_ip_add=input('Введите IP-сеть в формате X.X.X.X/M :')
input_ip_add=input_ip_add.split('/')
ip_add=input_ip_add[0].split('.')
net_mask=int(input_ip_add[1])

bin_ip_addr=(
f'{int(ip_add[0]):08b}'
f'{int(ip_add[1]):08b}'
f'{int(ip_add[2]):08b}'
f'{int(ip_add[3]):08b}')

bin_ip_addr=(bin_ip_addr[:(net_mask)]+ '0'*(32-net_mask))
#print(bin_ip_addr)

bit_octet_addr_1=bin_ip_addr[0:8]
bit_octet_addr_2=bin_ip_addr[8:16]
bit_octet_addr_3=bin_ip_addr[16:24]
bit_octet_addr_4=bin_ip_addr[24:32]

print('Network:')
print(
f'{int((bit_octet_addr_1),2):<10}'
f'{int((bit_octet_addr_2),2):<10}'
f'{int((bit_octet_addr_3),2):<10}'
f'{int((bit_octet_addr_4),2):<10}')

print(
f'{(bit_octet_addr_1):<10}'
f'{(bit_octet_addr_2):<10}'
f'{(bit_octet_addr_3):<10}'
f'{(bit_octet_addr_4):<10}')


print('Mask:')
net_mask=int(input_ip_add[1])
print('/', net_mask, sep="")
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


