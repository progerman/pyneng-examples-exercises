access_template = ['switchport mode access',
'switchport access vlan',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}


#print('access.items()', type(access.items()), access.items())

for  vlan  in access.items():

    #print('intf',intf)
    print('vlan',vlan)
    #print('interface FastEthernet' + intf)
    
    #for command in access_template:
        
        #if command.endswith('access vlan'):
            
            #print(' {} {}'.format(command, vlan))
    #else:
        #print(' {}'.format(command))
