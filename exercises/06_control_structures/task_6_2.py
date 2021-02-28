# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_addr = input(' ввод IP-адреса в формате 10.0.1.1 : ')
ip_addr = ip_addr.split('.')
ip_addr1 = []
for line in ip_addr:
    ip_addr1.append(int(line)) 
if   1 <= ip_addr1[0] <= 223:
    print('unicast')
elif 224 <= ip_addr1[0] <= 239:
    print('multicast')
elif ip_addr1[0] == ip_addr1[1] == ip_addr1[2] == ip_addr1[3] == 255:
    print('local broadcast')
elif ip_addr1[0] == ip_addr1[1] == ip_addr1[2] == ip_addr1[3] == 0:
    print('unassigned')
else:
    print('unused')
