# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
            
            
            if interface_line.startswith('interface FastEthernet'): 
             
                
                vlans_line=cfg_line[indx+2].strip()
                
                interface_line=interface_line.split(' ')[1]
               
                     
                vlan_id_list=[]
                if 'switchport access vlan' in vlans_line:
                    port_access_dict[interface_line]=int(vlans_line.split(' ')[-1])
                    
                elif 'duplex' in vlans_line:
                    port_access_dict[interface_line]=1
                    
                    
                elif 'switchport trunk allowed vlan' in vlans_line:
                    for  vlan_id_filter in vlans_line.split(',')[0].split(' ') + vlans_line.split(',')[1::]:
                       if vlan_id_filter.isdigit() == True :
                        vlan_id_list.append(int(vlan_id_filter))
                        port_trunk_dict[interface_line]=vlan_id_list
                
    return port_access_dict , port_trunk_dict

int_vlans_config=get_int_vlan_map('config_sw2.txt')




print (int_vlans_config)
