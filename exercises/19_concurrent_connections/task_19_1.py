# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess


ip_list=['192.168.100.1',
        '192.168.100.100',
        '192.168.100.2' ,
        '192.168.100.200',
        '192.168.100.3',
        '192.168.100.300',
        "1.1.1", 
        "8.8.8.8", 
        "8.8.4.4", 
        "8.8.7.1"
        ]


def pinger(ip_addr):
    #result_ping = subprocess.run(['ping', '-c', '2', '-n', f'{ip_addr}'], 
                #stdout=subprocess.PIPE, 
                #stderr=subprocess.PIPE
                #)
    result_ping = subprocess.run(['ping', '-c', '2', '-n', f'{ip_addr}'])
    
    return result_ping.returncode 

def ping_ip_addresses(ip_list,limit=3):
    ip_permyt_list=[]
    ip_deny_list=[]
    with ThreadPoolExecutor(max_workers=limit) as executor:
         result = executor.map(pinger, ip_list)
         for ip, status in zip(ip_list,result):
            if status == 0 :
                ip_permyt_list.append(ip)
            else:ip_deny_list.append(ip)
                            
    return ip_permyt_list, ip_deny_list


if __name__ == '__main__':
    
    print(ping_ip_addresses(ip_list,limit=6))
    
    






















