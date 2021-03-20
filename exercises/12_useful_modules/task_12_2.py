# -*- coding: utf-8 -*-
import ipaddress
from pprint import pprint
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

test_ip_list=['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132', '10.1.1.1-345','192.168.13.a-10']







def convert_ranges_to_ip_list(ip_adreses):
    result_ip_renge=[]
    intermediate_ip_range=[]
    for one_ip_adress in ip_adreses:
        try:
            if ipaddress.IPv4Address(one_ip_adress).version  == 4 :
                result_ip_renge.append(one_ip_adress)
            
        
        except:
            
            intermediate_ip_range.append(one_ip_adress)
            
    for ip in  intermediate_ip_range:       
        if '-' in one_ip_adress :
            ips=ip.split('-')
            try:
                if (ipaddress.IPv4Address(ips[0]).version  == 4 and 
                    ipaddress.IPv4Address(ips[1]).version  == 4 ):
                    gain_ip=int(ips[1].split('.')[-1])-int(ips[0].split('.')[-1])
                    for i in range(gain_ip+1):
                        result_ip_renge.append(str(ipaddress.IPv4Address(ips[0])+i))
           
                    
            except:
                try:
                    if ipaddress.IPv4Address(ips[0]).version  == 4 and 0 < int(ips[1]) < 255:
                        gain_ip = int(ips[1])-int(ips[0].split('.')[-1])
                        for i in range(gain_ip+1):
                            result_ip_renge.append(str(ipaddress.IPv4Address(ips[0])+i))
                    else:print('false ip adress',ip )
                    
                except: print('false ip adress',ip )
        
        
    
    return result_ip_renge



pprint(convert_ranges_to_ip_list(test_ip_list))









