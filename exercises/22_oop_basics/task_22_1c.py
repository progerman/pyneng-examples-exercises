# -*- coding: utf-8 -*-

"""
Задание 22.1c

Изменить класс Topology из задания 22.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology_dict = topology_dict
        self.topology = self._normalize(topology_dict)
        
    def _normalize(self, topology_dict):
        new_dict = {}
        result_unique_items_dict = {}
        i = 0
        for key,value in topology_dict.items():
            if topology_dict.get(value) == key:
                new_dict[key] = value
            else:result_unique_items_dict[key] = value
        for key , value in new_dict.items():
            i += 1
            if i <= int(len(new_dict)/2):
                result_unique_items_dict[key] = value
              
        return result_unique_items_dict 
        
        
    def delete_link(self, link_1 , link_2):
        if  self.topology.get(link_1) == link_2:
            print (link_1,':',link_2)
            print(f'Удаление линка: {link_1}: {link_2}')
            del self.topology[link_1]
        elif self.topology.get(link_2) == link_1:
            print (link_2,':',link_1)
            print(f'Удаление "обратного" линка: {link_2}: {link_1}')
            del self.topology[link_2]
        else:
            print(len(self.topology) )
            print('Такого соединения нет')
        print('-'*50)
        
    def delete_node(self, node):
        len_dict_after=len(self.topology)
        for key, value in list(self.topology.items()):
            if key[0]  == node:
                del self.topology[key]
            elif value[0] == node:
                del self.topology[key]
        if  len_dict_after == len(self.topology):
            print('Такого устройства нет')
                

if __name__ == '__main__':
    top = Topology(topology_example)
    print('-'*20,'top.topology after','-'*20)
    pprint(top.topology)
    top.delete_node('SW1')
    #top.delete_link(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
    print('-'*20,'top.topology beafor','-'*20)
    pprint(top.topology)







