# -*- coding: utf-8 -*-

"""
Задание 22.1b

Изменить класс Topology из задания 22.1a или 22.1.

Добавить метод delete_link, который удаляет указанное соединение.
Метод должен удалять и "обратное" соединение, если оно есть (ниже пример).

Если такого соединения нет, выводится сообщение "Такого соединения нет".

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

Удаление линка:
In [9]: t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление "обратного" линка:
в словаре есть запись ``('R3', 'Eth0/2'): ('R5', 'Eth0/0')``, но вызов delete_link
с указанием ключа и значения в обратном порядке, должно удалять соединение:

In [11]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))

In [12]: t.topology
Out[12]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}

Если такого соединения нет, выводится сообщение:
In [13]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
Такого соединения нет

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
        #for num,key in enumerate(self.topology):
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
        
       
    
        

if __name__ == '__main__':
    top = Topology(topology_example)
    print('-'*20,'top.topology after','-'*20)
    pprint(top.topology)
    print('-'*50)
    top.delete_link(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
    print('-'*20,'top.topology beafor','-'*20)
    pprint(top.topology)
    
    
    
    
    
    
    
    
    
    
    
    
    
    









