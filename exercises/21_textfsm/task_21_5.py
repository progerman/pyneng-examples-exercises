# -*- coding: utf-8 -*-
"""
Задание 21.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в
параллельных потоках функцию send_and_parse_show_command из задания 21.4.

Параметры функции send_and_parse_command_parallel:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* templates_path - путь к каталогу с шаблонами TextFSM
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать словарь:
* ключи - IP-адрес устройства с которого получен вывод
* значения - список словарей (вывод который возвращает функция send_and_parse_show_command)

Пример словаря:
{'192.168.100.1': [{'address': '192.168.100.1',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '192.168.200.1',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.2': [{'address': '192.168.100.2',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '10.100.23.2',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}]}

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
import yaml
from netmiko import ConnectHandler
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
import textfsm


def send_show(devices, command):
    with ConnectHandler(**devices) as ssh:
        list_result = []
        ssh.enable()
        result = ssh.send_command(command,strip_command=True, strip_prompt=True)
        for i in result.split('\n'):
            list_result.append(i)
            list_result.append(devices['host'])
    return list_result 


def send_show_command_to_devices(devices, command,  limit = 3):
    with ThreadPoolExecutor(max_workers = limit) as executor:
        list_1 = []
        result = executor.map(send_show, devices, repeat(command))
        for i in result:
            list_1.append(i)
        return list_1
    

def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        parse_result = fsm.ParseText(command_output)
        result_dict = {}
        for j in parse_result:
            result_dict = dict(zip(fsm.header, j))
        return result_dict
    
    
def send_and_parse_command_parallel(devices, command, templates_path, limit = 3):
    result_dict = {}
    for output_list in send_show_command_to_devices(devices, command, limit):
        parse_result_list=[]
        for output in output_list[::-1]:
            dict_parse_command = parse_output_to_dict(templates_path, output)
            if dict_parse_command != {}:
                parse_result_list.append(dict_parse_command)
            result_dict[output_list[-1]] = parse_result_list
    return result_dict
        
    
if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    result = send_and_parse_command_parallel(devices, command, "templates/sh_ip_int_br.template" )
    pprint(result)
    
    
    








