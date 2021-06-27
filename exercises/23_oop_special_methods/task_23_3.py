# -*- coding: utf-8 -*-

"""
Задание 23.3

Скопировать и изменить класс Topology из задания 22.1x.

Добавить метод, который позволит выполнять сложение двух экземпляров класса Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

Создание двух топологий:

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

Суммирование топологий:

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Проверка, что исходные топологии не изменились:

In [9]: t1.topology
Out[9]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [10]: t2.topology
Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
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

topology_example2 = {
    ("R1", "Eth0/4"): ("R7", "Eth0/0"),
    ("R1", "Eth0/6"): ("R9", "Eth0/0"),
}


from pprint import pprint

#def unique_network_map(topology_dict):
    #new_dict = {}
    #result_unique_items_dict = {}
    #i = 0
    #for key,value in topology_dict.items():
        #if topology_dict.get(value) == key:
            #new_dict[key] = value
        #else:result_unique_items_dict[key] = value
    #for key , value in new_dict.items():
        #i += 1
        #if i <= int(len(new_dict)/2):
            #result_unique_items_dict[key] = value
          
    #return result_unique_items_dict   


class Topology:
    
    def __init__(self, topology):
        self.topology = self._unique_network_map(topology)
        
    def __add__(self, other):
        new_dict = self.topology.copy()
        new_dict.update(other.topology)
        return Topology(new_dict)
        
    def _unique_network_map(self,topology_dict):
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
    
    


if __name__ == '__main__':
    top_1 = Topology(topology_example)
    pprint(top_1.topology)
    print(len(top_1.topology))
    
    top_2 = Topology(topology_example2)
    pprint(top_2.topology)
    print(len(top_2.topology))
    
    top3 = top_1+top_2
    pprint(top3.topology)
    print(len(top3.topology))
    pprint(top_1.topology)



