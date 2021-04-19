import sqlite3
import yaml
import os
import re
from pprint import pprint
from create_db import create_connection_to_db ,db_file_name,create_schema_db,schema_db

yaml_file='switches.yml'

def finding_dhcp_snooping():
    dir_all =  os.listdir ()
    file_dhcp_sn_list=[]
    for i in dir_all:
        if 'dhcp_snooping.txt' in i:
            file_dhcp_sn_list.append(i)
            
    return file_dhcp_sn_list



def dhcp_snooping_parser():
    
    regex=(r'((?P<mac>(\w+|\d+|:){17})\s+(?P<ip>(\d+|\.)+)(?:.*dhcp-snooping\s+)(?P<vlan>\d+)\s+(?P<intf>.+))')
    regex_name_dev=(r'(?P<dev_name>^\w+\d+)')
    result=[]
    for i in finding_dhcp_snooping():
        
        match_dev_name=re.search(regex_name_dev,i).group('dev_name')
        
        
        with open(i) as file_dhcp_sn:
            for n in file_dhcp_sn:
                a=[]
                match=re.search(regex,n)
                if match:
                   a.append(match.group('mac','ip','vlan','intf'))
                   a.append(match_dev_name)
                   result.append(a)
                
    return result

def parser_yaml(yaml_file):
    with open(yaml_file) as yaml_file_open:
        templates = list(yaml.safe_load(yaml_file_open).values())
    return templates
    


def create_query():
    
    connection=create_connection_to_db(db_file_name)
    if create_schema_db(db_file_name,schema_db):
        print('', end='\n\n')
        print('\033[1;33;40m Добавляю данные в таблицу switches...')
        for  i in parser_yaml(yaml_file):
            for n in i.items():
                with connection:
                    row={'dev_name':n[0],
                        'location':n[1]}
                    dev_name=n[0]
                    location=n[1]
                    try:
                        print(f'\033[1;32;40m insert into switches values ({dev_name}, {location});')
                        connection.execute('insert into switches values (:dev_name, :location);', row)
                    except  sqlite3.IntegrityError:
                        print('\033[1;31;40m Возникла ошибка:sqlite3.IntegrityError: UNIQUE constraint failed: switches.hostname')
                    except sqlite3.OperationalError: 
                        print('\033[1;31;40m Таблици switches не существует')
    print('', end='\n\n')
    print('\033[1;33;40m Добавляю данные в таблицу dhcp...')
    for m in dhcp_snooping_parser():
        #dev_name=m[1]
       
       
        with connection:
            row={'mac':m[0][0],
                'ip':m[0][1],
                'vlan':m[0][2],
                'intf':m[0][3],
                'dev_name':m[1]}
            try:
                print(f'\033[1;32;40m insert into dhcp values ({m[0][0]}, {m[0][1]}, {m[0][2]}, {m[0][3]}, {m[1]});')
                connection.execute('insert into dhcp values (:mac, :ip, :vlan, :intf, :dev_name);', row)
            except sqlite3.IntegrityError:
                print('\033[1;31;40m Возникла ошибка:sqlite3.IntegrityError: UNIQUE constraint failed: switches.hostname')
        
    
    
    
    
    
    
create_query()
#pprint(parser_yaml(yaml_file))
#pprint(dhcp_snooping_parser())

