# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import textfsm
from textfsm import clitable

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
    
    def send_command(self, command):
        result_send_command = super().send_command(command)
        self._check_error_in_command(command, result_send_command)
        return result_send_command
        
    def send_config_set(self, commands):
        if type(commands) == str:
            command = commands
            result_send_command = super().send_config_set(command)
            self._check_error_in_command(command, result_send_command)
            return result_send_command
        else:
            result_list = []
            for command in commands:
                result_send_command = super().send_config_set(command)
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
    #print(r1.send_command('sh ip int br'))
    print(r1.send_config_set(['interface fastEthernet 0/1', 'ip address 10.1.1.1 255.255.255.0']))





