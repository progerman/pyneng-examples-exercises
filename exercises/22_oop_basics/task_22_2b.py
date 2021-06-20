# -*- coding: utf-8 -*-

"""
Задание 22.2b

Скопировать класс CiscoTelnet из задания 22.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного
режима и список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko
(пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

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
            
            
    def send_config_commands(self, command):
        if type(command) == str:
            command_to_bite_encode = self._write_line(command)
            self.telnet.write(self._write_line('conf t'))
            print(self.telnet.read_until(b'#').decode('utf-8'))
            self.telnet.write(command_to_bite_encode)
            return self.telnet.read_until(b'#').decode('utf-8')
            
            
        else:
            result = []
            self.telnet.write(self._write_line('conf t'))
            print(self.telnet.read_until(b'#').decode('utf-8'))
            for line in command:
                command_to_bite_encode = self._write_line(line)
                self.telnet.write(command_to_bite_encode)
                result.append(self.telnet.read_until(b'#').decode('utf-8'))
            return '\n'.join(result)
        
    

if __name__ == '__main__':
    r1_params = {
            'ip': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'
                }
    connect_telnet = CiscoTelnet(**r1_params)
    #pprint(connect_telnet.send_show_command("sh ip int br" ))
    print(connect_telnet.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))
    
    
    
