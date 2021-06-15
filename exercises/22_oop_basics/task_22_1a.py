# -*- coding: utf-8 -*-

"""
Задание 22.1a

Скопировать класс Topology из задания 22.1 и изменить его.

Перенести функциональность удаления "дублей" в метод _normalize.
При этом метод __init__ должен выглядеть таким образом:
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
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        
    def _normalize(self, topology_dict):
        return unique_network_map(topology_dict)
        
    




if __name__ == '__main__':
    top = Topology(topology_example)
    pprint(top.topology)
    
    
    
    
