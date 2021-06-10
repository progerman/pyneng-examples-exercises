# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""


from pprint import pprint
from tabulate import tabulate
import textfsm

def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        parse_result = fsm.ParseText(command_output)
    result_dict={}
    parse_result_list=[]
    for j in parse_result:
        result_dict = dict(zip(fsm.header, j))
        parse_result_list.append(result_dict)
    return parse_result_list
    

if __name__ == "__main__":
    with open('output/sh_ip_int_br.txt' , 'r') as f:
        file_output=f.read()
    result = parse_output_to_dict("templates/sh_ip_int_br.template",file_output)
    pprint(result)
    






'''
'С переворотом массива на 90 градусов '

def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        parse_result = fsm.ParseText(command_output)
        parse_result_list=[]
        t=0
        for i in parse_result:
            parse_result_m=[]
            for n in parse_result:
                parse_result_m.append(n[t])
            t=t+1
            parse_result_list.append(parse_result_m)
            if t == len(n):break    
    result_dict = dict(zip(fsm.header, parse_result_list))
    return result_dict

'====Результат=====' 
{'address': ['15.0.15.1',
             '10.0.12.1',
             '10.0.13.1',
             'unassigned',
             '10.1.1.1',
             '100.0.0.1'],
 'intf': ['FastEthernet0/0',
          'FastEthernet0/1',
          'FastEthernet0/2',
          'FastEthernet0/3',
          'Loopback0',
          'Loopback100'],
 'protocol': ['up', 'up', 'up', 'up', 'up', 'up'],
 'status': ['up', 'up', 'up', 'up', 'up', 'up']}

'''





