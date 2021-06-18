# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


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
    
    
    def add_link(self, link_1, link_2):
        print('-'*50)
        if self.topology.get(link_1) == link_2:
            print('Такое соединение существует')
        else:
            if self.topology.get(link_1) or self.topology.get(link_2):
                print('Cоединение с одним из портов существует')
            else:
                self.topology[link_1] = link_2
                print(f'добавлено соединение {link_1}: {link_2}')
                    
                    

if __name__ == '__main__':
    top = Topology(topology_example)
    print('-'*20,'top.topology after','-'*20)
    pprint(top.topology)
    #top.delete_node('SW1')
    #top.delete_link(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
    top.add_link(("R3", "Eth0/10"), ("R7", "Eth0/0"))
    print('-'*20,'top.topology beafor','-'*20)
    pprint(top.topology)
    
    
    
    
    
    
