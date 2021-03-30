# -*- coding: utf-8 -*-

from pprint import pprint
import re
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""



def parse_sh_ip_int_br(file_name):
    with open(file_name) as data:
        regex1=(r'(\S+\d+)\s+(\S+)\s+(?:YES)\s(?:\S+)\s+(\S+)\s+(\S+)')
        regex2=(r'(\S+\d+)\s+(\S+)\s+(?:YES)\s(?:\S+)\s+(\S+\s+\S+)\s+(\S+)')
        result_tupl1=()
        result_tupl2=()
        result_list=[]
        
        for line in data:
            if not 'administratively down' in line: 
                match=re.search(regex1,line)
                if match:
                    result_tupl1=(match.group(1),match.group(2),match.group(3),match.group(4))
                    result_list.append(result_tupl1)
            else:
                match2=re.search(regex2,line)
                if match2:
                    result_tupl2=(match2.group(1),match2.group(2),match2.group(3),match2.group(4))
                    result_list.append(result_tupl2)
                    
    return result_list
    
    
forprint=parse_sh_ip_int_br('sh_ip_int_br.txt')

pprint(forprint)
