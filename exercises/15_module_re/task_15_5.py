# -*- coding: utf-8 -*-
import re
from pprint import pprint

"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""


def generate_description_from_cdp(file_name):
    with open(file_name) as data:
        regex=(r'(?P<dev>\S+\d+)\s+(?P<local_port>\S+\s+\S+).+ (?P<dest_port>\S+ \S+)')
        result_dict={}
        for line in data:
            match=re.search(regex,line)
            if match:
                dev=match.group('dev')
                local_port = match.group('local_port')
                dest_port = match.group('dest_port')
                result_dict[local_port]=f'description Connected to {dev} port {dest_port}'
    return result_dict
            
            
pprint(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
    
