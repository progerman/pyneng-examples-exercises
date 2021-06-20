# -*- coding: utf-8 -*-

"""
Задание 22.2a

Скопировать класс CiscoTelnet из задания 22.2 и изменить
метод send_show_command добавив три параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей,
  полученный после обработки с помощью TextFSM.
  При parse=True должен возвращаться список словарей, а parse=False обычный вывод.
  Значение по умолчанию - True.
* templates - путь к каталогу с шаблонами. Значение по умолчанию - "templates"
* index - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"


Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_22_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command("sh ip int br", parse=True)
Out[4]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'}]

In [5]: r1.send_show_command("sh ip int br", parse=False)
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status
Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up
up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up...'


"""

import telnetlib
from pprint import pprint
from tabulate import tabulate
import textfsm
from textfsm import clitable

class CiscoTelnet:
    def __init__(self, **params):
        self.params = params
        ip, username, password, secret = params.values()
        self.telnet = telnetlib.Telnet(ip) 
        self.telnet.read_until(b'Username')
        self.telnet.write(self._write_line(username))
        self.telnet.read_until(b'Password')
        self.telnet.write(self._write_line(password))
        self.telnet.read_until(b'>')
        self.telnet.write(b'enable\n')
        self.telnet.read_until(b'Password')
        self.telnet.write(self._write_line(secret))
        self.telnet.read_until(b'#')
        
        
    def _write_line(self,line):
        return f"{line}\n".encode("utf-8")
        
        
    def send_show_command(self, command, parse = True, templates = 'templates', index = 'index'):
        if parse:
            command_to_bite_encode = self._write_line(command)
            self.telnet.write(command_to_bite_encode)
            command_output = self.telnet.read_until(b'#').decode('utf-8')
            attributes = {'Command' : f'{command}', 'Vendor' : 'cisco_ios'}
            cli_table = clitable.CliTable(index, templates)
            cli_table.ParseCmd(command_output,  attributes)
            result_dict = {}
            parse_result_list = []
            for j in cli_table:
                result_dict = dict(zip(cli_table.header, j))
                parse_result_list.append(result_dict)
            return parse_result_list
        else:
            command_to_bite_encode = self._write_line(command)
            self.telnet.write(command_to_bite_encode)
            return self.telnet.read_until(b'#').decode('utf-8')


if __name__ == '__main__':
    r1_params = {
            'ip': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'
                }
    connect_telnet = CiscoTelnet(**r1_params)
    pprint(connect_telnet.send_show_command("sh ip int br" ))
    
    
    
    
