# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    port_access_dict={}
    port_trunk_dict={}
    cfg_line=[]
    
    with open(config_filename, 'r') as cfg:
        for lst in cfg:
            cfg_line.append(lst)
        for indx in range(len(cfg_line)):
            interface_line=cfg_line[indx].strip()
            if interface_line.startswith('interface') and 'switchport' in cfg_line[indx+2].strip():
                vlans_line=cfg_line[indx+2].strip()
                interface_line=interface_line.split(' ')[1]
                vlan_id_list=[]
                if 'switchport access vlan' in vlans_line:
                    port_access_dict[interface_line]=int(vlans_line.split(' ')[-1])
                elif 'switchport trunk allowed vlan' in vlans_line:
                    for  vlan_id_filter in vlans_line.split(',')[0].split(' ') + vlans_line.split(',')[1::]:
                       if vlan_id_filter.isdigit() == True :
                        vlan_id_list.append(int(vlan_id_filter))
                        port_trunk_dict[interface_line]=vlan_id_list
    return port_access_dict , port_trunk_dict

int_vlans_config=get_int_vlan_map('config_sw1.txt')




print (int_vlans_config)
