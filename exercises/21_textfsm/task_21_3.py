# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""

from task_21_1a import parse_output_to_dict
from textfsm import clitable
from pprint import pprint


def parse_command_dynamic(command_output, attributes_dict, index_file, templ_path):
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    result_dict={}
    parse_result_list=[]
    for j in cli_table:
        result_dict = dict(zip(cli_table.header, j))
        parse_result_list.append(result_dict)
    return parse_result_list
    


if __name__ == "__main__":
    with open("output/sh_cdp_n_det.txt", 'r') as f:
        output = f.read()
        attributes = {'Command' : 'sh cdp ne det', 'Vendor' : 'cisco_ios'}
        index_file='index'
        templ_path="templates"
        result=parse_command_dynamic(output, attributes, index_file, templ_path)
        pprint(result)
 
