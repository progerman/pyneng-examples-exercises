#!/usr/bin/env python3

from sys import argv


if len(argv) == 1:
    access_template = ['switchport mode access',
        'switchport access vlan {}',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable']
    print(','.join(access_template).format(5))
        
    
else:
    option1 = argv[1]
    if option1 == '-l':
        access_template = ['switchport mode access',
        'switchport access vlan {}',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable']
        print('\n'.join(access_template).format(5))
        

    else:
        print(argv [1::] ,'option not found')
        


