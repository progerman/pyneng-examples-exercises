'''
В этом примере будет разбираться вывод команды sh ip int br. Из вывода команды нам надо
получить соответствия имя интерфейса - IP-адрес. То есть имя интерфейса - это ключ словаря,
а IP-адрес - значение. При этом, соответствие надо делать только для тех интерфейсов, у
которых назначен IP-адрес'''

'Вариант1'

result = {}
with open('sh_ip_int_br.txt') as src:
    src_sp = src.read().split('\n')
    for src_lst in src_sp:
        if src_lst.startswith('Loopback') or src_lst.count('Ethernet'):
            src_lst = src_lst.split('\n')
            for src_lst2 in src_lst:
                src_lst2 = src_lst2.split(' ')
                for src_lst3 in src_lst2:
                    if src_lst3.startswith('Loopback') or src_lst3.count('Ethernet'):
                        key1 = src_lst3
                    elif src_lst3.count('.', 0, 15) == 3:
                        value1 = src_lst3
                result[key1] = value1
    print(result)


'Вариант2'
'''
result = {}
with open('sh_ip_int_br.txt') as f:
    for line in f:
        line = line.split()
        if line and line[1][0].isdigit():
            interface, address, *other = line
            result[interface] = address
print(result)

'''





