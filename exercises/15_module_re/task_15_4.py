# -*- coding: utf-8 -*-
import re
from pprint import pprint
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""



def get_ints_without_description(config_file_name):
    with open(config_file_name) as data:
        a = 0
        b = ''
        result_list = []
        regex=(r'\S+\s+(\S+)')
        for num ,i in  enumerate(data):
            if  i.startswith('interface'): 
                a = num
                b = re.search(regex,i).group(1)
            elif i.startswith(' description') == False and (num == a+1 and b != ''):
                result_list.append(b.rstrip())
    return result_list
            
            
            
    
    


for_print=get_ints_without_description('config_r1.txt')


pprint(for_print)

'''
#Вариант Наташи


import re


def get_ints_without_description(config):
    regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
                       r"(?P<descr> description \S+)?")
    with open(config) as src:
        match = regex.finditer(src.read())
        result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        return result
'''











