# -*- coding: utf-8 -*-
"""
Задание 20.5

Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt,
которые генерируют конфигурацию IPsec over GRE между двумя маршрутизаторами.

Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля,
а templates/gre_ipsec_vpn_2.txt - для второй.

Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах:
cisco_vpn_1.txt и cisco_vpn_2.txt.

Шаблоны надо создавать вручную, скопировав части конфига в соответствующие шаблоны.

Создать функцию create_vpn_config, которая использует эти шаблоны
для генерации конфигурации VPN на основе данных в словаре data.

Параметры функции:
* template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* template2 - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна возвращать кортеж с двумя конфигурациями (строки),
которые получены на основе шаблонов.

Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах
cisco_vpn_1.txt и cisco_vpn_2.txt.
"""
import yaml
from task_20_1 import generate_config


data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}



def create_vpn_config(template1, template2, data_dict):
    config_vpn_1=generate_config(template1,data_dict)
    config_vpn_2=generate_config(template2,data_dict)
    print(config_vpn_1)
    print('-'*100)
    print(config_vpn_2)
    print('-'*100)
    return config_vpn_1 , config_vpn_2
    
    
    
if __name__ == "__main__":
    
    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"
    print(create_vpn_config(template1, template2, data))





'''
templates/gre_ipsec_vpn_1.txt


crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
 hash sha

crypto isakmp key cisco address {{wan_ip_1}}

crypto ipsec transform-set AESSHA esp-aes esp-sha-hmac
 mode transport

crypto ipsec profile GRE
 set transform-set AESSHA

interface Tunnel {{tun_num}}
 ip address {{tun_ip_1}}
 tunnel source  {{wan_ip_1}}
 tunnel destination  {{wan_ip_2}}
 tunnel protection ipsec profile GRE
 
 --------------------------------------------------
 "templates/gre_ipsec_vpn_2.txt"
 
 
 crypto isakmp policy 10
 encr aes
 authentication pre-share
 group 5
 hash sha

crypto isakmp key cisco address {{wan_ip_2}}

crypto ipsec transform-set AESSHA esp-aes esp-sha-hmac
 mode transport

crypto ipsec profile GRE
 set transform-set AESSHA

interface Tunnel {{tun_num}}
 ip address {{tun_ip_2}}
 tunnel source  {{wan_ip_2}}
 tunnel destination  {{wan_ip_1}}
 tunnel protection ipsec profile GRE

'''
 


