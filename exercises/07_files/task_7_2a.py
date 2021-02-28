# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]


from sys import argv

name_file=argv
if name_file[1::] != 0:
    with open(''.join(name_file[1::]), 'r') as doc_1:
        for list1 in doc_1:
            for ignore_list in ignore:
                if list1.startswith('!') == True: break
                elif list1.find(ignore_list) != -1: break
            else:print(list1.strip('\n'))
else:print('enter file name')
