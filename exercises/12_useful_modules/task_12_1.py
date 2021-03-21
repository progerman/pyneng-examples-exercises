# -*- coding: utf-8 -*-

import subprocess
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



#list_of_ips = ["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]





def ping_ip_addresses(ip_list_range):
    true_ping=[]
    false_ping=[]
    
    for ip_ping in ip_list_range:
        result=subprocess.run(['ping', '-c', '1', '-n', ip_ping],stdout=subprocess.DEVNULL)
        #print(result.returncode)
        if result.returncode == 0 : 
            false_ping.append(ip_ping)
            #print(false_ping)
        else:
            true_ping.append(ip_ping)
    return false_ping,true_ping
#print(ping_ip_addresses(list_of_ips))

























