# -*- coding: utf-8 -*-

from task_12_1 import ping_ip_addresses
from tabulate import tabulate
import subprocess
from itertools  import zip_longest 
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

true_ping=["8.8.8.8", "8.8.4.4", '127.0.0.1']
false_ping=["1.1.1",  "8.8.7.1", '10.1.1.1', '20.1.1.1', '10.4.4.7']


def print_ip_table(true_ping,false_ping):
    return(list(zip_longest((true_ping), (false_ping))))
    
    
columns = ['Reachable', 'Unreachable']
print(tabulate((print_ip_table(true_ping, false_ping)), headers = columns))

    



'''
from tabulate import tabulate


def print_ip_table(reach_ip, unreach_ip):
    table = {"Reachable": reach_ip, "Unreachable": unreach_ip}
    print(tabulate(table, headers="keys"))


if __name__ == "__main__":
    reach_ip = ["10.1.1.1", "10.1.1.2"]
    unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]
    print_ip_table(reach_ip, unreach_ip)


# вариант решения без tabulate (zip_longest не используется так как его не проходили)
def print_ip_table(reach_ip, unreach_ip):
    reach_ip = ["Reachable"] + reach_ip
    unreach_ip = ["Unreachable"] + unreach_ip
    longest = len(max(reach_ip, unreach_ip))
    shortest = len(min(reach_ip, unreach_ip))
    short_list = reach_ip if len(reach_ip) != longest else unreach_ip
    short_list = short_list.extend([""] * (longest - shortest))

    for row in zip(reach_ip, unreach_ip):
        print("{:15}{:15}".format(*row))
'''






