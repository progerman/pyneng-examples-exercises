# -*- coding: utf-8 -*-
"""
Задание 18.2c

Скопировать функцию send_config_commands из задания 18.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка, спросить пользователя надо ли выполнять
остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию,
  поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = correct_commands + commands_with_errors 




import yaml
import netmiko
from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_config_commands(dev, commands, error_case, log=True):
    try:
        question=True
        with ConnectHandler(**dev) as ssh:
            if log:print('-'*50 , f' , Подключаюсь к {list(dev.values())[1]}')
            ssh.enable()
            result_send_command_ok = {}
            result_send_command_erro = {}
            result = []
            result1 = []
            result2 = []
            
            for command in commands:
                output = ssh.send_config_set(command)
                
                for err_str in error_case :
                    if err_str in output and question:
                        print(f'Команда {command} выполнилась с ошибкой {err_str} на устройстве {list(dev.values())[1]}')
                        result_send_command_erro[command]=output
                        result2.append(result_send_command_erro)
                        question = input('Продолжать выполнять команды? [y]/n: ')
                        if question == ('n' or 'no') :
                            question=False
                            print('Выполнение команд остановлено')
                        else:question=True
                        break
                if result_send_command_erro.get(command) == None and question:
                    result_send_command_ok[command]=output
                    result1.append(result_send_command_ok)
                    print(f'Команда {command} выполнилась успешно на устройстве {list(dev.values())[1]}')
                
                #print('Выполнение команд остановлено')
                #break
        return result , result1 , result2
        
        
         
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    

if __name__ == "__main__":
    
    error_case=['Invalid input detected', 'Incomplete command', 'Ambiguous command']
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        res=send_config_commands(dev, commands, error_case)
        #for i in res[0]:
            #print (i)
        for j in res[1]:
            pprint(j)
            break
        for m in res[2]:
            pprint(m)
            break













