# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping,trunk_template):
    
    
    result_config_dict={}
    
    for interface, vlans in intf_vlan_mapping.items():
        vlan_id_result=[]
        result_config_list=[]
        for vlan_id in vlans:
            vlan_id_result.append(str(vlan_id))
        for config_line in trunk_template:
            if config_line.endswith('allowed vlan'):
                a = config_line + ' ' + ','.join(vlan_id_result)
                result_config_list.append(a.strip())
            else:
                result_config_list.append(config_line.strip())
                
            result_config_dict[interface]=result_config_list
        
    return result_config_dict
           
get_config=generate_trunk_config(trunk_config,trunk_mode_template)

#print(get_config)

for line2 in get_config.items():
    print(line2[0])
    
    for line3 in line2[1]:
        print(line3)
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
