# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
from task_21_3 import parse_command_dynamic
from textfsm import clitable
from pprint import pprint
from task_18_1 import send_show_command

def send_and_parse_show_command(device_dict, command, templates_path, index, attributes):
    show_command_result = send_show_command(device_dict, command)
    parse_result = parse_command_dynamic(show_command_result, attributes, index, templates_path ) 
    return parse_result
    



if __name__ == "__main__":
    device = {
            "device_type": "cisco_ios_telnet",
            "host": "192.168.100.1",
            "username": "cisco",
            "password": "cisco",
            "secret": "cisco",
            }
    command = "sh ip int br"
    attributes = {'Command' : 'sh ip int br', 'Vendor' : 'cisco_ios'}
    index_file ='index'
    templ_path ="templates"
    result = send_and_parse_show_command(device, command, templ_path , index_file , attributes)
    pprint(result)
