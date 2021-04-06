# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re
from pprint import pprint


f = open('sh_cdp_n_sw1.txt')






def parse_sh_cdp_neighbors(listing_cdp):
    result_dict={}
    dict1={}
    regex_dev_name=(r'(\S+)[>|#]')
    regex_parce=(r'(\S+\d+)\s+(\S+\s+\S+).+\s(\S+\s\d+\/\d+)')
    dev_index=re.search(regex_dev_name,listing_cdp).group(1)
    
    for i in re.findall(regex_parce,listing_cdp):
        dict2={}
        dict2[i[0]]=i[2]
        dict1[i[1]]=dict2
    
    result_dict[dev_index]=dict1
    
    return result_dict


r=parse_sh_cdp_neighbors(f.read())

#pprint(r)


'''
#Вариант Наташи



import re


def parse_sh_cdp_neighbors(command_output):
    regex = re.compile(
        r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
        r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_dict = {}
    l_dev = re.search(r"(\S+)[>#]", command_output).group(1)
    connect_dict[l_dev] = {}
    for match in regex.finditer(command_output):
        r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
    return connect_dict


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))
'''





