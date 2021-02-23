# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


int_mode = input('Введите режим работы интерфейса (access/trunk):')
variant_type={'access':'Введите номер VLAN:', 'trunk':'ведите разрешенные VLANы:'}
int_type = input('Введите тип и номер интерфейса:')
vlan_num = input(variant_type[int_mode])

trunk_template[2] = trunk_template[2].format(vlan_num)
access_template[1] = access_template[1].format(vlan_num)

dict_teml={'access': access_template, 'trunk': trunk_template}

print('interface', int_type)

if int_mode == 'access':
    print((','.join(dict_teml[int_mode])).replace(',','\n'))
elif int_mode == 'trunk':
    print(
    f'{dict_teml[int_mode][0]} \n'
    f'{dict_teml[int_mode][1]} \n'
    f'{dict_teml[int_mode][2]} \n')
else:
    print('stop')
