# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan_id_input=input('input vlan ID: ')
vlan_list = []
list2 = []
ff = []
kk = []
with open('CAM_table.txt', 'r') as doc_1:
    for list1 in doc_1:
        list2.append(list1.split('\n'))
    for i in list2:
        for aa in i:
            indx1 = aa.strip().replace('DYNAMIC', '')
            if indx1[0:5].strip().isdigit() == True :
                vlan_list.append(int(indx1[0:5]))
                vlan_list.append(indx1)
    for ff in range(0,len(vlan_list), 2):
        kk.append(vlan_list[ff:ff+2])
        kk.sort()
    for n in kk:     
        if n[0] == int(vlan_id_input):
            print(n[1])
        
