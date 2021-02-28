# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt', 'r') as ospf_info:
       for line in ospf_info:
            line2 = line.split('\n')
            line3 = line2[0].split(',')
  
            prefix = line2[0].split(',')[0].split(' ')[-4]+'\n'
            ad_metric = line2[0].split(',')[0].split(' ')[-3][1:-1]+'\n'
            next_hop = line2[0].split(',')[0].split(' ')[-1]+'\n'
            *_, last_upd, intf = line3
            print(
            f'Prefix                {prefix}'
            f'AD/Metric             {ad_metric}'
            f'Next-Hop              {next_hop}'
            f'Last update           {last_upd.strip()}\n'
            f'Outbound Interface    {intf.strip()}\n')
            
