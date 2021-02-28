# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

name_file=argv
if name_file[1::] != 0:
    with open(''.join(name_file[1]), 'r') as doc_1 , open(''.join(name_file[2]), 'w') as dest_doc: #python task_7_2b.py config_sw1.txt config.txt
        for list1 in doc_1:
            for ignore_list in ignore:
                if list1.startswith('!') == True: break
                elif list1.find(ignore_list) != -1: break
                elif list1 == '\n' : break
            else:dest_doc.write(list1)
else:print('enter file name')
