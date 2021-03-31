# -*- coding: utf-8 -*-

import re
from pprint import pprint
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""


def convert_ios_nat_to_asa(file_name_ios,file_name_asa):
    with open(file_name_ios) as data, open(file_name_asa, 'w') as dest_write :
        regex = (r'(?P<port_type>tcp|udp)\s+'
                r'(?P<IP>\d+.\d+.\d+.\d+)\s+'
                r'(?P<src_port>\d+)\s+\S+\s+\S+\s+'
                r'(?P<dst_port>\d+)')
        for i in data:
            match = re.search(regex,i)
            IP = match.group('IP')
            port_type = match.group('port_type')
            src_port = match.group('src_port')
            dst_port = match.group('dst_port')
            line=(
            f'object network LOCAL_{IP}\n'
            f' host {IP}\n'
            f' nat (inside,outside) static interface service {port_type} {src_port} {dst_port}\n')
            dest_write.write(line)
            
            
convert_ios_nat_to_asa('cisco_nat_config.txt','file_config_nat_for_asa.txt')



