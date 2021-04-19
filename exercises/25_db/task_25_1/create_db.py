import os
import sqlite3
import subprocess
import re
from pprint import pprint

db_file_name = 'dhcp_snooping.db'
schema_db = 'dhcp_snooping_schema.sql'

def check_db_file_exists(db_filename):
    db_exists = os.path.exists(db_filename)
    
    return db_exists


def create_db(db_name):
    if check_db_file_exists(db_name) == False: 
        print(f'Создаю базу данных {db_name}...')
        result_create_db=subprocess.run(f'sqlite3 {db_name}  .databases .quit', shell=True, stdout = subprocess.PIPE)
        print(result_create_db.stdout.decode('utf-8'))
    else: print(f'База данных {db_name} уже существует')
        
    return True


def create_connection_to_db(db_name):
    if create_db(db_name):
        print(f'Создаю коннектор к базе {db_name} ...')
        connection = sqlite3.connect(db_name)
        
    return connection



def create_schema_db(db_name, schema_db):
    connection = create_connection_to_db(db_name)
    schema_db_file=open(schema_db, 'r')
    regex = (r'create table(?P<table_name>\s+\S+\s+)(?:.*\s.)*;')
    match = re.finditer(regex, schema_db_file.read())
    
    for n,i in enumerate(match, 1):
        table_name = i.group('table_name')
        try:
            with connection:
                connection.executescript(i.group())
                print(f'\033[1;32;40m Создаю таблицу №{n} {table_name} и схему данных')
                print('\033[1;31;40m', i.group())
        except sqlite3.OperationalError:
            print(f'Таблица {table_name} уже существует')
    
    return True
    
    
    
    

if __name__ == '__main__':
    create_schema_db(db_file_name,schema_db)











