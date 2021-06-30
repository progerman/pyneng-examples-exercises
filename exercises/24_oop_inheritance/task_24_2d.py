# -*- coding: utf-8 -*-

"""
Задание 24.2d

Скопировать класс MyNetmiko из задания 24.2c или задания 24.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен
работать точно так же как метод send_config_set в netmiko.
Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."
"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import textfsm
from textfsm import clitable
from pprint import pprint

device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании,
    возникла ошибка.
    """


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()
        self.ip = device_params.get('ip')
    
    def send_command(self, command,  **kwargs):
        result_send_command = super().send_command(command,  **kwargs)
        self._check_error_in_command(command, result_send_command)
        return result_send_command
        
    def send_config_set(self, commands, ignore_errors=False , **kwargs ):
        if type(commands) == str:
            command = commands
            result_send_command = super().send_config_set(command, **kwargs)
            if ignore_errors == False:
                self._check_error_in_command(command, result_send_command)
            return result_send_command
        else:
            result_list = []
            for command in commands:
                result_send_command = super().send_config_set(command, **kwargs)
                if ignore_errors == False:
                    self._check_error_in_command(command, result_send_command)
                result_list.append(result_send_command)
            return result_list
            
    def _check_error_in_command(self, command , return_command):
        result_check_error=self._error_line_detect(return_command)
        if result_check_error :
            raise  ErrorInCommand(f'При выполнении команды "{command}" на устройстве {self.ip} возникла ошибка "{result_check_error[0][0]}"')
            
    def _error_line_detect(self,output):
        template = "templates/error.template"
        with open(template) as template:
            fsm = textfsm.TextFSM(template)
            parse_result = fsm.ParseText(output)
            return parse_result
    

if __name__ == '__main__':
    r1 = MyNetmiko(**device_params)
    #print(r1.send_command('sh ip int br', strip_command=False))
    pprint(r1.send_config_set(['sh ip int bri', 'sh clock','lo'],ignore_errors=True, strip_command=False))
