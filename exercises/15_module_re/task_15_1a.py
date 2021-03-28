# -*- coding: utf-8 -*-
import re
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""



def get_ip_from_cfg(file_name):
    with open(file_name) as data:
        regex_intf=(r'(interface.)(\S+\d+)' )
        regex=(r'(.ip address.)(\S+.\S+.\S+.\S+) +(\S+.\S+.\S+.\S+)')
        result_dict={}
        result_list=[]
        result_tupl=()
        for line in data:
            match = re.search(regex, line)
            match1 = re.search(regex_intf,line)
            if match1:
                a=match1.group(2)
            if match:
                result_tupl=(match.group(2),match.group(3))
                result_dict[a]=result_tupl
    return result_dict
    
    
dict1=get_ip_from_cfg('config_r1.txt')
print(dict1)
