# -*- coding: utf-8 -*-

import re
from pprint import pprint
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""


def get_ip_from_cfg(file_name):
    with open(file_name) as data:
        regex_intf=(r'(interface.)(\S+\d+)' )
        regex=(r'(ip address) (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)')
        result_dict={}
        result_tupl=()
        for line in data:
            match = re.search(regex, line)
            match1 = re.search(regex_intf,line)
            if match1:
                a=match1.group(2)
                result_list=[]
            if match:
                result_tupl=(match.group(2),match.group(3))
                result_list.append(result_tupl)
                result_dict[a]=result_list
                
                
    return result_dict

    
dict1=get_ip_from_cfg('config_r2.txt')
pprint(dict1)














