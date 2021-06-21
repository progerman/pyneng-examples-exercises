# -*- coding: utf-8 -*-

"""
Задание 22.2c

Скопировать класс CiscoTelnet из задания 22.2b и изменить метод send_config_commands
добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:
* strict=True значит, что при обнаружении ошибки, необходимо сгенерировать
  исключение ValueError (значение по умолчанию)
* strict=False значит, что при обнаружении ошибки, надо только вывести
  на стандартный поток вывода сообщене об ошибке

Метод дожен возвращать вывод аналогичный методу send_config_set
у netmiko (пример вывода ниже). Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:
In [1]: from task_22_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:

In [7]: print(r1.send_config_commands(commands, strict=False))
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
При выполнении команды "a" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "a"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

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
        self.ip = ip
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
            
            
    def send_config_commands(self, command, strict = True):
        if type(command) == str:
            command_to_bite_encode = self._write_line(command)
            self.telnet.write(self._write_line('conf t'))
            print(self.telnet.read_until(b'#').decode('utf-8'))
            self.telnet.write(command_to_bite_encode)
            return self.telnet.read_until(b'#').decode('utf-8')
        else:
            result = []
            result_err = []
            self.telnet.write(self._write_line('conf t'))
            self.telnet.read_until(b'#').decode('utf-8')
            for line in command:
                command_to_bite_encode = self._write_line(line)
                self.telnet.write(command_to_bite_encode)
                output_command = self.telnet.read_until(b'#').decode('utf-8')
                error_line = self.error_line_detect(output_command)
                if  error_line  and strict:
                    raise ValueError(f"При выполнении команды {line} на устройстве {self.ip} возникла ошибка -> {error_line}")
                elif  error_line  and strict == False:
                    result_err.append(f"При выполнении команды {line} на устройстве {self.ip} возникла ошибка -> {error_line}")
                result.append(output_command)
            result_err.append( '\n'.join(result))
            return '\n'.join(result_err)
            
            
    def error_line_detect(self,error_output):
        template = "templates/cisco_dev_err_detect.template"
        with open(template) as template:
            fsm = textfsm.TextFSM(template)
            parse_result = fsm.ParseText(error_output)
            try:
                return parse_result[0][0]
            except:
                return False
           

if __name__ == '__main__':
    r1_params = {
            'ip': '192.168.100.1',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'
                }
    connect_telnet = CiscoTelnet(**r1_params)
    #pprint(connect_telnet.send_show_command("sh ip int br" ))
    print(connect_telnet.send_config_commands(['ip http server', 'logging buffered 20010','rlogging buffered 20010', 'logging', "a" ], strict = False))



'''
"templates/sh_ip_int_br.template"


Value error (.*)

Start
  ^%${error} -> Record
'''

