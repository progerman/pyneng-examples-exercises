# -*- coding: utf-8 -*-

"""
Задание 22.1

Создать класс Topology, который представляет топологию сети.

При создании экземпляра класса, как аргумент передается словарь,
который описывает топологию. Словарь может содержать "дублирующиеся" соединения.
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Задача оставить только один из этих линков в итоговом словаре, не важно какой.

В каждом экземпляре должна быть создана переменная topology, в которой содержится
словарь топологии, но уже без "дублей". Переменная topology должна содержать словарь
без "дублей" сразу после создания экземпляра.

Пример создания экземпляра класса:
In [2]: top = Topology(topology_example)

После этого, должна быть доступна переменная topology:

In [3]: top.topology
Out[3]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""
from pprint import pprint


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


def unique_network_map(topology_dict):
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


class Topology:
    def __init__(self, topology):
        
        self.topology = unique_network_map(topology)


if __name__ == '__main__':
    top = Topology(topology_example)
    pprint(top.topology)
   
    
    
    
    
    
    
    
    
    
